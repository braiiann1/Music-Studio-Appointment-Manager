from classes import *
from datetime import timedelta
import calendar
import time

cantidades: dict

def only_possible(evento:str, sala:str):
    return (False,f"{evento} solo es posible en {sala}")

def dependant(equipo, eventosala):
    return (False,f"{equipo} es imprescindible para {eventosala}")

def incompatible(equipo):
    return (False,f"{equipo} no es compatible con la sala seleccionada")

def excluyentes(equipo1, equipo2):
    return (False,f"{equipo1} es incompatible con {equipo2}")


def buscar_hueco(evento: list, lista_eventos: list, message: str):

    print("busca hueco...")

    event_start_hour = timedelta(days= int(evento[4][0]),hours=int(evento[2][0][0]+evento[2][0][1]), minutes=int(evento[2][0][3]+evento[2][0][4]))
    event_end_hour = timedelta(days= int(evento[4][1]),hours=int(evento[2][1][0]+evento[2][1][1]), minutes=int(evento[2][1][3]+evento[2][1][4]))

    #Duracion del evento para el cual se busca hueco
    full_intervalo = event_end_hour - event_start_hour + timedelta(minutes=1)
    print("intervalo:", full_intervalo)

    for i in range(len(lista_eventos)):
        try:
            ev = lista_eventos[i]
            if not isinstance(ev, (list, tuple)) or len(ev) < 7:
                continue
            end_time = ev[2][1]
            #Hago el tiempo inicio a partir de end_time
            t0 = timedelta(hours=int(end_time[0:2]), minutes=int(end_time[3:5])) + timedelta(minutes=1)
        except Exception:
            #Horario invalido
            continue

        #Formato para hora_inicio
        horasi = t0.seconds //3600
        minutosi = (t0.seconds%3600)//60
        hora_inicio = f"{horasi:02d}:{minutosi:02d}"

        #t1 sera hora de finalizacion del evento
        t1 = t0 + full_intervalo
        #formato para lograr hora_final
        dias = t1.days
        horas = t1.seconds //3600
        minutos = (t1.seconds%3600)//60
        hora_final = f"{horas:02d}:{minutos:02d}"


        print("hora_inicio:", hora_inicio)
        print("hora_final:", hora_final)
        print("dias_intervalo:", dias)
        
        start_day_candidate = int(lista_eventos[i][4][1])
        end_day_candidate = start_day_candidate + dias

        #Si dia final > dias del mes
        try:
            month_i = int(lista_eventos[i][5])
            year_i = int(lista_eventos[i][6])
            days_in_month = calendar.monthrange(year_i, month_i)[1]
        except Exception:
            #Mes/Ano mal formateadp
            days_in_month = None

        if days_in_month is not None and end_day_candidate > days_in_month:
            # Move the suggested slot to the next month preserving the overflow days
            overflow = end_day_candidate - days_in_month
            next_month = month_i + 1
            next_year = year_i
            if next_month > 12:
                next_month = 1
                next_year += 1

            new_event = (evento[0], evento[1], (hora_inicio, hora_final), evento[3], (str(1), str(overflow)), str(next_month), str(next_year))
        else:
            new_event = (evento[0], evento[1], (hora_inicio, hora_final), evento[3], (lista_eventos[i][4][1], str(end_day_candidate)), lista_eventos[i][5], lista_eventos[i][6])

        print(new_event)

        validation_result = validation(new_event[0], new_event[1], new_event[2], new_event[3], new_event[4], new_event[5], new_event[6], lista_eventos)
        if validation_result[0]:
            
            return (False, "forbello", message, new_event)
    return (False, "no_hueco", message)

def revisar_cantidades(evento:list, lista_eventos:list) -> tuple:
    start_day = int(evento[4][0])
    end_day = int(evento[4][1])
    dias_intervalo = list(range(start_day, end_day + 1))

    overlapping = [evento]

    def time_to_minutes(t: str) -> int:
        #Formato
        return int(t[0:2]) * 60 + int(t[3:5])

    start_e = time_to_minutes(evento[2][0])
    end_e = time_to_minutes(evento[2][1])

    #Recorro la lista de eventos y detecto si hay colision
    for i in lista_eventos:
        #Mismo anio y mismo mes
        try:
            if int(i[6]) != int(evento[6]) or i[5] != evento[5]:
                continue
        except Exception:
            continue

        #Mismo dia
        try:
            start_i = int(i[4][0])
            end_i = int(i[4][1])
        except Exception:
            continue

        #Si no hay interseccion en dias
        if not (set(range(start_i, end_i + 1)).intersection(dias_intervalo)):
            continue

        #Convierto horas a minutos
        s_i = time_to_minutes(i[2][0])
        e_i = time_to_minutes(i[2][1])

        #Colision si (end_i <= start_e or start_i >= end_e)
        if not (e_i <= start_e or s_i >= end_e):
            overlapping.append(i)

    #Diccionario para almacenar la cantidad utilizada en funcion al recurso
    usados = {}

    for ev in overlapping:
        # Recorro el inventario de cada evento
        for j in ev[3]:
            if j in usados:
                usados[j] += 1
            else:
                usados[j] = 1

    # Tiro cantidad del inventario con cantidad en classes
    for equipo, cant in usados.items():
        for eq in EQUIPOS:
            if eq.name == equipo:
                if cant > eq.quantity:
                    return (False, "forbello", f"{equipo}, no puede exceder una cantidad superior a {eq.quantity}")

    return (True, "Evento anadido con exito :D")

def validation(event,room, hour, inventory, days, month, year, event_list):

    evento_hueco = [event,room, hour, inventory, days, month, year]
    print(evento_hueco)

    if int(days[0]) > int(days[1]):
        return (False, "Dia inicial no puede ser mayor a dia de fin")

    if len(hour[0]) == 0 or len(hour[1]) == 0:
        return (False,"Debe asignar la hora de incio y culminacion")
    
    if hour[0] == hour[1]:
        return (False,"La hora de inicio y fin no pueden ser iguales")

    if len(hour[0]) != 5 or len(hour[1]) != 5:
        return (False,"Formato incorrecto para la hora")

    if int(str(hour[0][0]) + str (hour[0][1])) > 23 or int(str(hour[0][3]) + str (hour[0][4])) > 59:
        return (False, "Formato de hora incorrecto")
    
    if int(str(hour[1][0]) + str(hour[1][1])) > 23 or int(str(hour[0][3]) + str (hour[0][4])) > 59:
        return (False, "Formato de hora incorrecto")
    
    if int(str(hour[0][0]) + str(hour[0][1]) + str(hour[0][3]) + str(hour[0][4])) > int(str(hour[1][0]) + str(hour[1][1]) + str(hour[1][3]) + str(hour[1][4])) and days[0] == days[1]:
        return (False,"Hora inicial no puede ser mayor a la hora de inicio")

    #Validacion por eventos
    if event == EVENTOS[0].name:
        if not room == SALAS[0].name:
            return only_possible(event, SALAS[0].name)
        
        if EQUIPOS[0].name not in inventory:
            return dependant(EQUIPOS[0].name, EVENTOS[0].name)
        
    if event == EVENTOS[1].name:
        if room != SALAS[0].name:
            return only_possible(event, SALAS[0].name)
        
        if EQUIPOS[0].name not in inventory:
            return dependant(EQUIPOS[0].name, event)
        
        if EQUIPOS[7].name not in inventory or EQUIPOS[6].name not in inventory:
            return (False, f"{EQUIPOS[7].name} y {EQUIPOS[6].name} son imprescindibles para {EVENTOS[1].name}")
        
    if event == EVENTOS[2].name:
        if room == SALAS[2].name:
            return (False,f"{event} no es posible en la Sala C")
        
        if EQUIPOS[0].name not in inventory:
            return dependant(EQUIPOS[0].name, event)
        
    if event == EVENTOS[3].name:
        if room != SALAS[1].name:
            return only_possible(EVENTOS[3].name, SALAS[1].name)
        
        if EQUIPOS[0].name not in inventory:
            return dependant(EQUIPOS[0].name, event)
        
        if EQUIPOS[5].name not in inventory:
            return dependant(EQUIPOS[5].name, event)
        
    if event == EVENTOS[4].name:
        if room != SALAS[2].name:
            return only_possible(event, SALAS[2].name)
        
        if EQUIPOS[10].name not in inventory:
            return dependant(EQUIPOS[10].name, event)        

    #Validacion por salas
    if room == SALAS[0].name:
        
        if EQUIPOS[2].name in inventory:
            return incompatible(EQUIPOS[2].name)
        
        if EQUIPOS[3].name in inventory:
            return incompatible(EQUIPOS[3].name)
            
        if EQUIPOS[8].name in inventory:
            return incompatible(EQUIPOS[8].name)
        
        if EQUIPOS[10].name in inventory:
            return incompatible(EQUIPOS[10].name)
    if room == SALAS[2].name:
        
        if EQUIPOS[7].name in inventory:
            return incompatible(EQUIPOS[7].name)
        
    #Validacion por recursos

    ##Excluyente
    if EQUIPOS[1].name in inventory and EQUIPOS[10].name in inventory:
        return excluyentes(EQUIPOS[1].name, EQUIPOS[10].name)
    

    ##Dependencias
    if EQUIPOS[2].name in inventory and EQUIPOS[8].name not in inventory:
        return dependant(EQUIPOS[8].name, EQUIPOS[2].name)

    if EQUIPOS[1].name in inventory and EQUIPOS[9].name not in inventory:
        return (False, "Las guitarras y bajo dependen de su amplificador")
    if EQUIPOS[3].name in inventory and EQUIPOS[9].name not in inventory:
        return (False, "Las guitarras y bajo dependen de su amplificador")
    if EQUIPOS[10].name in inventory and EQUIPOS[9].name not in inventory:
        return (False, "Las guitarras y bajo dependen de su amplificador")
    
    if EQUIPOS[7].name in inventory and EQUIPOS[6].name not in inventory:
        return (False, "El software de audio depende de la tarjeta de sonido")
    if EQUIPOS[4].name in inventory and EQUIPOS[6].name not in inventory:
        return (False, "El software de audio depende de la tarjeta de sonido")

    #Colisiones por cantidades
    is_overlapping = revisar_cantidades(evento_hueco, event_list)
    if is_overlapping[0] == False:
        return buscar_hueco(evento_hueco, event_list, is_overlapping[2])

    return (True, "Evento anadido con exito")