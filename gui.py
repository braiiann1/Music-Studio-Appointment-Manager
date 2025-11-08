import tkinter as tk
import customtkinter as ctk
from classes import *

def anadir():
    frame_event_list.place_forget()
    frame_anadir.place(x=260,y=240)
    button_cerrar_anadir.place(relx = 0.93, rely = 0.04)
    eventos_opciones.place(relx = 0.08, rely = 0.1)
    salas_opciones.place(relx = 0.08, rely= 0.25)
    desde_hasta.place(relx = 0.68, rely = 0.12)
    start_hour.place(relx = 0.68, rely = 0.22)
    end_hour.place(relx = 0.83, rely = 0.22)
    confirm_button.place(relx = 0.80, rely = 0.88)
    #Izquierda
    radio1.place(relx=0.1,rely=0.4)
    radio2.place(relx=0.1,rely=0.5)
    radio3.place(relx=0.1,rely=0.6)
    radio4.place(relx=0.1,rely=0.7)
    radio5.place(relx=0.1,rely=0.8)
    radio6.place(relx=0.1,rely=0.9)
    #Derecha
    radio7.place(relx=0.5,rely=0.4)
    radio8.place(relx=0.5,rely=0.5)
    radio9.place(relx=0.5,rely=0.6)
    radio10.place(relx=0.5,rely=0.7)
    radio11.place(relx=0.5,rely=0.8)

    event_information_button.place(relx=0.48,rely=0.05)

def confirm():
    Evento = []
    Evento_inventario = []

    Evento.append(eventos_opciones._current_value)
    Evento.append(salas_opciones._current_value)

    print(Evento)

    for i in radios:
        if i._value == True:
            Evento_inventario.append(i._text)

    print(Evento_inventario)

def editar():
    if edit_button._text == "Editar":
        edit_button.configure(text="Cancelar", width=40)
        add_button.place_forget()
    else: edit_button.configure(text="Editar"), add_button.place(relx = 0.95, rely = 0.03)

def eliminar():
    pass

def informacion():
    if salas_opciones._current_value == "Sala A - Singular":
        sala_informacion = "Sala para proyectos de un solo artista con alguna colaboracion"
    elif salas_opciones._current_value == "Sala B - Multipersonal":
        sala_informacion = "Sala para proyectos profesionales o de bandas emergentes"
    elif salas_opciones._current_value == "Sala C - Profesional":
        sala_informacion = "Sala de capacidad considerable para proyectos a gran escala. Ej; Orquestas, Bandas sonoras, Coros"
    
    
    
def anadir_cerrar():
    frame_anadir.place_forget()
    frame_event_list.place(relx=0.02, rely=0.13)

def event_information():
    pass


nombre_eventos=[]
for i in range(len(EVENTOS)):
    nombre_eventos.append(EVENTOS[i].name)

nombre_salas=[]
for i in range(len(SALAS)):
    nombre_salas.append(SALAS[i].name)

radio_font = ("liberation sans", 18, "bold")

#Seteo de GUI

ctk.set_appearance_mode("dark")

ctk.DrawEngine.preferred_drawing_method="circle_shapes"

window = ctk.CTk(fg_color="#1A1111")

global_font = ctk.CTkFont("liberation sans", size=40)


window.geometry("1280x720")

window.minsize(width=1280, height=720)
window.maxsize(width=1280, height=720)

window.title("Gestor de Turnos")

#Frames
frame1 = ctk.CTkFrame(window, fg_color="#221515", width=600, corner_radius=30)
frame2 = ctk.CTkFrame(window, fg_color="#221515", width=1200, height=600, corner_radius=30)
frame_anadir = ctk.CTkFrame(window, fg_color="#3A2626", bg_color="#221515", width=800, height=400, corner_radius=50)
frame_event_list = ctk.CTkFrame(frame2, fg_color="#442B2B", bg_color="transparent", width=1150, height=500, corner_radius=40) 

#Labels
titulo = ctk.CTkLabel(frame1, width=500, height=70, text='Estudio Musical "Botaos Gang"', font=("liberation sans", 25, "bold"))
subtitulo = ctk.CTkLabel(frame1, text="Gestor de sesiones de grabacion", font=("liberation sans", 20, "bold"))

eventos_opciones = ctk.CTkOptionMenu(frame_anadir,fg_color="#2B1D1D", values=nombre_eventos,
                                   font=("liberation sans", 20, "bold"), width=315,height=42,corner_radius=29, dropdown_fg_color="#2B1D1D", 
                                   button_color="#2B1D1D",button_hover_color="#3D2A2A", dropdown_font=("liberation sans", 20, "bold"))

salas_opciones = ctk.CTkOptionMenu(frame_anadir,fg_color="#2B1D1D", values=nombre_salas,
                                   font=("liberation sans", 20, "bold"), button_hover_color="#3D2A2A", width=315,height=42,corner_radius=29, dropdown_fg_color="#2B1D1D", 
                                   button_color="#2B1D1D", dropdown_font=("liberation sans", 20, "bold"))

eventos_titulo = ctk.CTkLabel(frame2, text="Turnos:", font=("liberation sans", 20, "bold"), fg_color="#442B2B", corner_radius= 10)
desde_hasta = ctk.CTkLabel(frame_anadir, text="Horario:", font=("liberation sans", 27))

start_hour = ctk.CTkTextbox(frame_anadir, width=90, height=30)
end_hour = ctk.CTkTextbox(frame_anadir, width=90, height=30)

#Botones
add_button = ctk.CTkButton(frame2, text="+", fg_color="transparent", hover_color="#523939", width=15, height=15, command=anadir, font=("liberation sans", 30, "bold"))
edit_button = ctk.CTkButton(frame2, text="Editar", fg_color="#442B2B",hover_color="#523939", width=10, height=15, command=editar, font=("liberation sans", 20, "bold"))

confirm_button = ctk.CTkButton(frame_anadir, text="Confirmar", fg_color="#251919",hover_color="#7A6767", width=10, height=15,command=confirm, font=("liberation sans", 20, "bold"))

event_information_button = ctk.CTkButton(frame_anadir, text="i", fg_color="#251919", hover_color="#7A6767", width=15, height=10,corner_radius=100, command=event_information, font=("liberation sans", 20, "bold"))

##Radios
radio1 = ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[0].name, hover_color="#533737", font=radio_font)
radio2 = ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[1].name, hover_color="#533737", font=radio_font)
radio3 = ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[2].name, hover_color="#533737", font=radio_font)
radio4 = ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[3].name, hover_color="#533737", font=radio_font)
radio5 = ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[4].name, hover_color="#533737", font=radio_font)
radio6 = ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[5].name, hover_color="#533737", font=radio_font)
radio7 = ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[6].name, hover_color="#533737", font=radio_font)
radio8 = ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[7].name, hover_color="#533737", font=radio_font)
radio9 = ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[8].name, hover_color="#533737", font=radio_font)
radio10= ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[9].name, hover_color="#533737", font=radio_font)
radio11= ctk.CTkRadioButton(frame_anadir, text=EQUIPOS[10].name, hover_color="#533737", font=radio_font)

radios = [radio1,radio2,radio3,radio4,radio5,radio6,radio7,radio8,radio9,radio10,radio11]


##Cerrar
button_cerrar_anadir = ctk.CTkButton(frame_anadir, text="X", corner_radius=100, hover_color="#251818", command=anadir_cerrar, width=30, height=30, fg_color="#160E0E")

#Empaqueteos
frame1.pack()
titulo.pack()
subtitulo.pack()
frame2.pack(pady = 10)
eventos_titulo.place(relx = 0.03, rely = 0.05)
add_button.place(relx = 0.95, rely = 0.03)
edit_button.place(relx = 0.88, rely = 0.04)
frame_event_list.place(relx=0.02, rely=0.13)

window.mainloop()