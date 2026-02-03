from classes import *
from datetime import timedelta
import calendar

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

    event_start_hour = timedelta(days= int(evento[4][0]),hours=int(evento[2][0][0]+evento[2][0][1]), minutes=int(evento[2][0][3]+evento[2][0][4]))
    event_end_hour = timedelta(days= int(evento[4][1]),hours=int(evento[2][1][0]+evento[2][1][1]), minutes=int(evento[2][1][3]+evento[2][1][4]))

    #Duracion del evento para el cual se busca hueco
    full_intervalo = event_end_hour - event_start_hour
    print("intervalo:", full_intervalo)
    for i in range(len(lista_eventos)):
        #t0 es la hora de finalizacion del evento en el que esta el for, que pasara a ser la hora de inicio en el hueco
        t0 = timedelta(hours=int(lista_eventos[i][2][1][0]+lista_eventos[i][2][1][1]), minutes=int(lista_eventos[i][2][1][3]+lista_eventos[i][2][1][4]))

        #formato para lograr hora_inicio
        horasi = t0.seconds //3600
        minutosi = (t0.seconds%3600)//60
        hora_inicio = f"{horasi:02d}:{minutosi:02d}"

        #t1 sera hora de finalizacion del evento
        t1 = hora_inicio + full_intervalo
        #formato para lograr hora_final
        dias = t1.days
        horas = t1.seconds //3600
        minutos = (t1.seconds%3600)//60
        hora_final = f"{horas:02d}:{minutos:02d}"


        print("hora_inicio:", hora_inicio)
        print("hora_final:", hora_final)
        print("dias_intervalo:", dias)

        #Si el dia se pasa del mes:
        if int(lista_eventos[i][4][1])+dias > calendar.monthrange(int(lista_eventos[i][6]),int(lista_eventos[i][5]))[1]:
            continue

        new_event = (evento[0], evento[1], (hora_inicio, hora_final), evento[3], lista_eventos[i][4], (lista_eventos[i][5][1],str(int(lista_eventos[i][5][1])+dias)), lista_eventos[i][6])


        if validation(new_event[0], new_event[1], new_event[2], new_event[3], new_event[4], new_event[5], new_event[6], lista_eventos):
            
            return (False,"forbello", message, new_event)

def revisar_cantidades(evento:list, lista_eventos:list) -> tuple:

    #Diccionario para almacenar la cantidad utilizada en funcion al recurso
    usados = {}

    #Recorro la lista de eventos
    for i in lista_eventos:

        #Recorro el inventario de cada evento
        for j in i[3]:
            if j in usados:
                usados[j] += 1
            else: usados[j] = 1

    #Recorro el inventario del evento nuevo
    for i in evento[3]:
        if i in usados:
            usados[j] += 1
        else: usados[j] = 1

    #Tiro cantidad del dict contra la de las clases para verificar que no haya excedente
    for i in range(len(EQUIPOS)):
        for equipo,cant in usados.items():
            if EQUIPOS[i].name == equipo:
                if cant > EQUIPOS[i].quantity:
                    return (False,f"{equipo}, no puede exceder una cantidad superior a {cant}")
              
    return(True, "Evento anadido con exito :D")

def validation(event,room, hour, inventory, days, month, year, event_list):

    if int(days[0]) > int(days[1]):
        return (False, "Dia inicial no puede ser mayor a dia de fin")

    if len(hour[0]) == 0 or len(hour[1]) == 0:
        return (False,"Debe asignar la hora de incio y culminacion")

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
    for i in event_list:
        ###Fecha de culminacion de evento i > fecha de inicio         ###Fecha de inicio < fecha de culminacion de evento i
        if int(hour[1][0]+hour[1][1]) > int(i[2][0][0]+i[2][0][1]) or int(hour[1][0]+hour[1][1]) < int(i[2][1][0]+i[2][1][1]):
            if revisar_cantidades(event, event_list)[0] != 1:
                evento_hole = [event, room, hour, inventory, days, month, year, event_list]
                return buscar_hueco(evento_hole, event_list, revisar_cantidades(evento_hole, event_list)[1])

    return (True, "Evento anadido con exito")