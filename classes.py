import json

class Eventos:
    def __init__(self, id, name, min_booking_hours, price, description):
        self.id = id
        self.name = name
        self.min_booking_hours = min_booking_hours
        self.price = price
        self.description = description

EVENTOS = [
    Eventos (901, "Grabacion de single", 1, 500,"Produccion de una  cancion destinada a lanzarse como sencillo independiente."),
    Eventos (902, "Grabacion de mixtape", 4, 3000, "Un mixtape es una recopilacion de varias canciones reunidas en un solo proyecto y difundidas de forma mas libre e informal que un album."),
    Eventos (903, "Grabacion de EP", 4, 2000, "Grabacion de un proyecto sencillo de corta duracion, pero con un trabajo productivo similar al de un album."),
    Eventos (904, "Grabacion de Album", 8, 5000, "Grabacion de un proyecto de duracion considerable, pensado para mostrar la identidad artistica de quien lo crea."),
    Eventos (905, "Grabacion de Banda Sonora/OST", 36, 20000, "Proyecto destinado a acompanar una pelicula, serie, videojuego u obra audiovisual, emplea una considerable cantidad de recursos.")
]

class Salas:
    def __init__(self, id, name, quantity, hourly_rate, min_booking_hours, description):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.hourly_rate = hourly_rate
        self.min_booking_hours = min_booking_hours # minimo requerido para la reserva
        self.description = description

SALAS = [
    Salas (1, "Sala A - Singular", 8, 500, 2, "Sala basica para proyectos sencillos de un solo artista con alguna colaboracion."),
    Salas (2, "Sala B - MultiPersonal", 5, 1000, 5, "Sala avanzada para proyectos profesionales y pulidos, ideal para bandas independientes o musicos en desarrollo, admite una amplia gama de equipamiento profesional y presenta una acustica de calidad."),
    Salas (3, "Sala C - Profesional", 2, 4000, 10, "Sala de capacidad considerable para proyectos a gran escala. Ej; Orquestas, Bandas sonoras, Coros.") ]

class Equipos_Audio:
    def __init__(self, id, name, category, quantity):
        self.id = id
        self.name = name
        self.category = category # "microfono", "instrumento", "monitor", "software de audio", "soundcard", "amplificador"
        self.quantity = quantity

EQUIPOS = [
    Equipos_Audio (101, "Microfono Profesional", "microfono", 10),
    Equipos_Audio (102, "Guitarra Fender Stratocaster", "instrumento", 1),
    Equipos_Audio (103, "Bateria Acustica Yamaha", "instrumento", 1),
    Equipos_Audio (104, "Bajo Fender American Vintage", "instrumento", 1),
    Equipos_Audio (105, "Sintetizador 808", "instrumento", 1),
    Equipos_Audio (106, "Monitores de Audio Profesional", "monitor", 3),
    Equipos_Audio (107, "Tarjeta de Sonido", "soundcard", 1),
    Equipos_Audio (108, "Antares Autotune", "software de audio", 1),
    Equipos_Audio (109, "Microfono para bateria", "microfono", 1),
    Equipos_Audio (110, "Amplificador Fender", "amplificador", 2),
    Equipos_Audio (111, "Guitarra Fender Telecaster", "instrumento", 1)
]
def meses():
    months = []
    for i in range(1,13):
        months.append(str(i))
    return months

resource_pool: dict

def revisar_cantidades():
    pass

class Event_list:
    lista_eventos = []

def save_json():
    with open("eventos.json","r",encoding="utf-8") as fp:
        Event_list.lista_eventos = json.load(fp)