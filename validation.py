from classes import *


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
        if room == SALAS[1].name or room == SALAS[2].name:
            return (False,"Grabacion de Single solo es posible en la Sala A")
        
        if EQUIPOS[0].name not in inventory:
            return (False, f"{EQUIPOS[0].name} es imprescindible para {EVENTOS[0].name}")
    
    #Validacion por salas
    if room == SALAS[0].name:
        
        if EQUIPOS[2].name in inventory:
            return (False,f"{EQUIPOS[2].name} no es compatible con el tipo de sala seleccionado")
        
        if EQUIPOS[3].name in inventory:
            return (False,f"{EQUIPOS[3].name} no es compatible con el tipo de sala seleccionado")
            
        if EQUIPOS[8].name in inventory:
            return (False,f"{EQUIPOS[8].name} no es compatible con el tipo de sala seleccionado")
        
    #Validacion por recursos

    return (True, "Evento anadido con exito")