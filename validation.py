from classes import *


def only_possible(evento:str, sala:str):
    return (False,f"{evento} solo es posible en {sala}")

def dependant(equipo, eventosala):
    return (False,f"{equipo} es imprescindible para {eventosala}")

def incompatible(equipo):
    return (False,f"{equipo} no es compatible con la sala seleccionada")

def excluyentes(equipo1, equipo2):
    return (False,f"{equipo1} es incompatible con {equipo2}")

def validation(event,room, hour, inventory):

    #Validacion por fecha/hora
    if len(hour[0]) == 0 or len(hour[1]) == 0:
        return (False,"Debe asignar la hora de incio y culminacion")

    if int(str(hour[0][0]) + str (hour[0][1])) > 23 or int(str(hour[0][3]) + str (hour[0][4])) > 59:
        return (False, "Formato de hora incorrecto")

    if len(hour[0]) != 5 or len(hour[1]) != 5:
        return (False,"Formato incorrecto para la hora")
    
    if int(str(hour[0][0]) + str(hour[0][1]) + str(hour[0][3]) + str(hour[0][4])) > int(str(hour[1][0]) + str(hour[1][1]) + str(hour[1][3]) + str(hour[1][4])): #and day_start == day end 
        return (False,"Fecha inicial no puede ser mayor a la fecha de inicio")
    
#   if day_start > day_end:
#       return (False,"Dia inicial no puede ser mayor a dia de fin")

#   if month_start != month_end:
#       return (False,"Mes inicial no puede ser mayor a mes de fin")
    

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
            return only_possible(EVENTOS[3].name, event)
        
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


    return (True, "Evento anadido con exito")