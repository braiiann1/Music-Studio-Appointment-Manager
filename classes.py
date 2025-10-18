import datetime

class Eventos:
    def __init__(self, id, name, min_booking_hours, price, complexity_index):
        self.id = id
        self.name = name
        self.min_booking_hours = min_booking_hours
        self.price = price
        self.complexity_index = complexity_index

EVENTOS = [
    Eventos (901, "Grabacion de single", 1, 500, 4),
    Eventos (902, "Grabacion de mixtape", 4, 3000, 5),
    Eventos (903, "Grabacion de EP", 4, 2000, 4),
    Eventos (904, "Grabacion de Album", 8, 5000, 7),
    Eventos (905, "Grabacion de Banda Sonora/OST", 36, 20000, 9)
]

class Salas:
    def __init__(self, id, name, capacity, hourly_rate, min_booking_hours, max_complexity):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.min_booking_hours = min_booking_hours # minimo requerido para la reserva
        self.max_complexity = max_complexity

SALAS = [
    Salas (1, "Sala A - Singular", 2, 500, 2, 6), # Sala para proyectos de un solo artista con alguna colaboracion
    Salas (2, "Sala B - MultiPersonal", 10, 1000, 5, 8), # Sala para proyectos profesionales o de bandas emergentes
    Salas (3, "Sala C - Profesional", 50, 4000, 10, 10) # Sala de capacidad considerable para proyectos a gran escala. Ej; Orquestas, Bandas sonoras, Coros
]

class Equipos_Audio:
    def __init__(self, id, name, category, quantity, requires_technician, setup_time):
        self.id = id
        self.name = name
        self.category = category # "microfono", "instrumento", "monitor", "software de audio", "soundcard", "amplificador"
        self.quantity = quantity
        self.requires_technician = requires_technician
        self.setup_time = setup_time # tiempo necesario para la instalacion de cada equipos

EQUIPOS = [
    Equipos_Audio (101, "Microfono Profesional", "microfono", 5, False, datetime.timedelta(minutes = 10)),
    Equipos_Audio (102, "Guitarra Fender Stratocaster", "instrumento", 1, True, datetime.timedelta(minutes=20)),
    Equipos_Audio (103, "Bateria Acustica Yamaha", "instrumento", 1, True, datetime.timedelta(minutes=40)),
    Equipos_Audio (104, "Bajo Fender American Vintage", "instrumento", 1, True, datetime.timedelta(minutes=10)),
    Equipos_Audio (105, "Sintetizador 808", "instrumento", 1, False, datetime.timedelta(minutes=5)),
    Equipos_Audio (106, "Monitores de Audio Profesional", "monitor", "3", False, datetime.timedelta(minutes=15)),
    Equipos_Audio (107, "Tarjeta de Sonido", "soundcard", "1", True, datetime.timedelta(minutes=5)),
    Equipos_Audio (108, "Antares Autotune", "software de audio", 1, True, datetime.timedelta(minutes=1)),
    Equipos_Audio (109, "Microfono para bateria Yamaha", "microfono", 1, False, datetime.timedelta(minutes=5)),
    Equipos_Audio (110, "Amplificador Fender", "amplificador", 2, True, datetime.timedelta(minutes=10)),
    Equipos_Audio (111, "Guitarra Fender Rollercaster", "instrumento", 1, True, datetime.timedelta(minutes=20))
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