class Eventos:
    def __init__(self, id, name, min_booking_hours, price, complexity_index, description):
        self.id = id
        self.name = name
        self.min_booking_hours = min_booking_hours
        self.price = price
        self.complexity_index = complexity_index
        self.description = description

EVENTOS = [
    Eventos (901, "Grabacion de single", 1, 500, 4, "Produccion de una  cancion destinada a lanzarse como sencillo independiente."),
    Eventos (902, "Grabacion de mixtape", 4, 3000, 5, "Un mixtape es una recopilacion de varias canciones reunidas en un solo proyecto y difundidas de forma mas libre e informal que un album."),
    Eventos (903, "Grabacion de EP", 4, 2000, 4, "Grabacion de un proyecto sencillo de corta duracion, pero con un trabajo productivo similar al de un album."),
    Eventos (904, "Grabacion de Album", 8, 5000, 7, "Grabacion de un proyecto de duracion considerable, pensado para mostrar la identidad artistica de quien lo crea."),
    Eventos (905, "Grabacion de Banda Sonora/OST", 36, 20000, 9, "Proyecto destinado a acompanar una pelicula, serie, videojuego u obra audiovisual, emplea una considerable cantidad de recursos.")
]

class Salas:
    def __init__(self, id, name, capacity, hourly_rate, min_booking_hours, max_complexity, description):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.min_booking_hours = min_booking_hours # minimo requerido para la reserva
        self.max_complexity = max_complexity
        self.description = description

SALAS = [
    Salas (1, "Sala A - Singular", 2, 500, 2, 6, "Sala basica para proyectos sencillos de un solo artista con alguna colaboracion."),
    Salas (2, "Sala B - MultiPersonal", 10, 1000, 5, 8, "Sala avanzada para proyectos profesionales y pulidos, ideal para bandas independientes o musicos en desarrollo, admite una amplia gama de equipamiento profesional y presenta una acustica de calidad."),
    Salas (3, "Sala C - Profesional", 50, 4000, 10, 10, "Sala de capacidad considerable para proyectos a gran escala. Ej; Orquestas, Bandas sonoras, Coros.") ]

class Equipos_Audio:
    def __init__(self, id, name, category, quantity, requires_technician):
        self.id = id
        self.name = name
        self.category = category # "microfono", "instrumento", "monitor", "software de audio", "soundcard", "amplificador"
        self.quantity = quantity
        self.requires_technician = requires_technician

EQUIPOS = [
    Equipos_Audio (101, "Microfono Profesional", "microfono", 5, False),
    Equipos_Audio (102, "Guitarra Fender Stratocaster", "instrumento", 1, True),
    Equipos_Audio (103, "Bateria Acustica Yamaha", "instrumento", 1, True,),
    Equipos_Audio (104, "Bajo Fender American Vintage", "instrumento", 1, True),
    Equipos_Audio (105, "Sintetizador 808", "instrumento", 1, False),
    Equipos_Audio (106, "Monitores de Audio Profesional", "monitor", "3", False),
    Equipos_Audio (107, "Tarjeta de Sonido", "soundcard", "1", True),
    Equipos_Audio (108, "Antares Autotune", "software de audio", 1, True),
    Equipos_Audio (109, "Microfono para bateria", "microfono", 1, False),
    Equipos_Audio (110, "Amplificador Fender", "amplificador", 2, True),
    Equipos_Audio (111, "Guitarra Fender Telecaster", "instrumento", 1, True)
]

class Tecnicos:
    def __init__(self, id, name, speciality, hourly_rate, available_hours):
        self.id = id
        self.name = name
        self.speciality = speciality # "calibracion (instrumentos, amplificador)" "masterizacion (monitores, soundcard)" "grabacion (microfono)" "produccion (software de audio)"
        self.hourly_rate = hourly_rate
        self.available_hours = available_hours # horario laboral

TECNICOS = [
    Tecnicos (201, "Luisito Lamenza", "produccion", 500, "18:00-00:00"),
    Tecnicos (202, "Jasiel La Bodega", "grabacion", 250, "12:00-16:00"),
    Tecnicos (203, "Taylor", "masterizacion", 1000, "8:00-18:00"),
    Tecnicos (204, "l' talent miliciah", "calibracion", 100, "12:00-00:00"),
    Tecnicos (205, "Pepito la curda", "produccion", 250, "12:00-18:00")
]

def dias():
    dias = []
    for i in range(1,32):
        dias.append(str(i))
    return dias

def meses():
    months = []
    for i in range(1,13):
        months.append(str(i))
    return months