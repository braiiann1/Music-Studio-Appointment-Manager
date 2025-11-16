import tkinter as tk
import customtkinter as ctk
from classes import *
from gestion import *
import threading

def start():
    frame1.pack()
    titulo.pack()
    subtitulo.pack()
    frame2.pack(pady = 10)
    eventos_titulo.place(relx = 0.03, rely = 0.05)
    add_button.place(relx = 0.95, rely = 0.03)
    filter_button.place(relx = 0.85, rely = 0.04)
    edit_button.place(relx = 0.88, rely = 0.04)
    frame_event_list.place(relx = 0.02, rely =0.13)

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
    evento = eventos_opciones._current_value
    sala = salas_opciones._current_value
    horario = (start_hour, end_hour)
    inventario.clear()
    for i in radios:
        if i._check_state:
            inventario.append(i._text)
    full_event = [evento,sala,inventario.copy()]
    lista_eventos.append(full_event)

def editar():
        edit_button.configure(text="Cancelar", width=40, command = cancelar)
        add_button.place_forget()
        for i in range(len(lista_eventos)):
             label_event_delete = ctk.CTkButton(frame_event_list, text="-", fg_color="#251919", hover_color= "#7A6767", width=15, height=15,
                                                corner_radius=100, font=("roboto", 30, "bold"), command=lambda idx=i : eliminar(idx))
             label_event_delete.grid(row = i, column = 3, padx = 20, pady = 10)

def cancelar():
    edit_button.configure(text="Editar", command = editar), add_button.place(relx = 0.95, rely = 0.03)
    for i in frame_event_list.grid_slaves():
         if i._text == "-":
            i.grid_forget()

def filter():
    filter_button.place_forget()
    filter_button_option.place(relx = 0.78, rely =0.045)
    filter_button_close.place(relx=0.8, rely=-0.05)

def filter_close():
    filter_button_option.place_forget()
    filter_button.place(relx = 0.85, rely = 0.035)
    filter_button_close.place_forget()

def informacion():
    sala_informacion: str
    eventos_informacion: str
    for i in range(len(SALAS)):
        if salas_opciones._current_value == SALAS[i].name:
            sala_informacion = SALAS[i].description
    for i in range(len(EVENTOS)):
        if eventos_opciones._current_value == EVENTOS[i].name:
            eventos_informacion = EVENTOS[i].description

    frame_informacion.place(x=260, y=240)
    button_cerrar_information.place(relx = 0.93, rely = 0.04)
    Event_Information_Label = ctk.CTkLabel(frame_informacion, width=700, height=30, text=eventos_informacion,fg_color="#251818", corner_radius=6,font=("roboto", 25, "bold"), wraplength=690)
    Room_Information_Label = ctk.CTkLabel(frame_informacion, width=700, height=30, text=sala_informacion,fg_color= "#251818", corner_radius=6,font=("roboto", 25, "bold"), wraplength=690)
    Title_Event_Label = ctk.CTkLabel(frame_informacion, width=300, height=10, text=eventos_opciones._current_value, font=("roboto", 30, "bold"))
    Title_Room_Label = ctk.CTkLabel(frame_informacion, width=300, height=10, text=salas_opciones._current_value, font=("roboto", 30, "bold"))
    Event_Information_Label.place(relx=0.1, rely=0.22)
    Room_Information_Label.place(relx=0.1, rely =0.6)
    Title_Event_Label.place(relx = 0.05, rely = 0.1)
    Title_Room_Label.place(relx= 0.02, rely= 0.45)

def anadir_cerrar():
    frame_anadir.place_forget()
    frame_event_list.place(relx=0.02, rely=0.13)
    frame_event_list._create_grid
    render_grid()

def render_grid():
    lista_eventos.reverse()
    for i in frame_event_list.winfo_children():
        i.destroy()

    for i in range(len(lista_eventos)):
            label_event_list = ctk.CTkLabel(frame_event_list, text=lista_eventos[i][0], font=("roboto", 30, "bold"), compound= "left")
            label_event_list.grid(row=i, column=0, padx=20, pady=15)
    for i in range(len(lista_eventos)):
            label_event_list = ctk.CTkLabel(frame_event_list, text=lista_eventos[i][1], font=("roboto", 30, "bold"), compound="left")
            label_event_list.grid(row=i, column=1, padx=20, pady=15)
    for i in range(len(lista_eventos)):
            label_event_button = ctk.CTkButton(frame_event_list, text="Info.", fg_color="#503636", hover_color="#7A6767", width=15, height=15, 
                                         corner_radius=100, font=("roboto", 30, "bold"), command= lambda idx=i : check_inventory(idx))
            label_event_button.grid(row = i, column=2, padx=20, pady=15)
            
def check_inventory(indice):
    current_inventory = lista_eventos[indice][2]
    print(current_inventory) 
         
def eliminar(indice):
    lista_eventos.pop(indice)
    render_grid()
    if edit_button._text == "Cancelar":
         for i in range(len(lista_eventos)):
             label_event_delete = ctk.CTkButton(frame_event_list, text="-", fg_color="#251919", hover_color= "#7A6767", width=15, height=15,
                                                corner_radius=100, font=("roboto", 30, "bold"), command=lambda idx=i : eliminar(idx))
             label_event_delete.grid(row = i, column = 3, padx = 20, pady = 15)

def informacion_cerrar():
    frame_informacion.place_forget()

def radio_press(radio):
    if radio.value == 0:
        radio.value = 1
    else: radio.value = 0

nombre_eventos=[]
for i in range(len(EVENTOS)):
    nombre_eventos.append(EVENTOS[i].name)

nombre_salas=[]
for i in range(len(SALAS)):
    nombre_salas.append(SALAS[i].name)

radio_font = ("roboto", 18, "bold")

#Seteo de GUI

lista_eventos:list = []
botones_eliminar: dict
inventario:list = []
label_event_list: object

filtros = ["Sala A", "Sala B", "Sala C", "Album", "Mixt.", "EP", "OST"]

window = ctk.CTk(fg_color="#1D1313")

window.geometry("1280x720")

window.minsize(width=1280, height=720)
window.maxsize(width=1280, height=720)

window.title("Gestor de Turnos")

#Frames
frame1 = ctk.CTkFrame(window, fg_color="#221515", width=600, corner_radius=30)
frame2 = ctk.CTkFrame(window, fg_color="#221515", width=1200, height=600, corner_radius=30)
frame_anadir = ctk.CTkFrame(window, fg_color="#3A2626", bg_color="#221515", width=800, height=400, corner_radius=50)
frame_event_list = ctk.CTkScrollableFrame(frame2, fg_color="#442B2B", bg_color="transparent", width=1100, height=430, corner_radius=40, scrollbar_button_color="#8A4E4E", scrollbar_button_hover_color="#BB7777")

frame_informacion = ctk.CTkFrame(window, fg_color="#3A2626", bg_color="#221515", width= 800, height=400, corner_radius=40, )

#Labels
titulo = ctk.CTkLabel(frame1, width=500, height=70, text='Estudio Musical "Botaos Gang"', font=("roboto", 25, "bold"))
subtitulo = ctk.CTkLabel(frame1, text="Gestor de sesiones de grabacion", font=("roboto", 20, "bold"))

eventos_opciones = ctk.CTkOptionMenu(frame_anadir,fg_color="#2B1D1D", values=nombre_eventos,
                                   font=("roboto", 20, "bold"), width=315,height=42,corner_radius=29, dropdown_fg_color="#2B1D1D", 
                                   button_color="#2B1D1D",button_hover_color="#3D2A2A", dropdown_font=("roboto", 20, "bold"))
salas_opciones = ctk.CTkOptionMenu(frame_anadir,fg_color="#2B1D1D", values=nombre_salas,
                                   font=("roboto", 20, "bold"), button_hover_color="#3D2A2A", width=315,height=42,corner_radius=29, dropdown_fg_color="#2B1D1D", 
                                   button_color="#2B1D1D", dropdown_font=("roboto", 20, "bold"))

eventos_titulo = ctk.CTkLabel(frame2, text="Turnos:", font=("roboto", 20, "bold"), fg_color="#442B2B", corner_radius= 10)
desde_hasta = ctk.CTkLabel(frame_anadir, text="Horario:", font=("roboto", 27))

start_hour_value = ""
end_hour_value = ""
start_hour = ctk.CTkEntry(frame_anadir, width=90, height=30, placeholder_text="00:00", textvariable=start_hour_value)
end_hour = ctk.CTkEntry(frame_anadir, width=90, height=30, placeholder_text="00:00", textvariable=end_hour_value)


#Botones
add_button = ctk.CTkButton(frame2, text="+", fg_color="transparent", hover_color="#523939", width=15, height=15, command=anadir, font=("roboto", 30, "bold"))
edit_button = ctk.CTkButton(frame2, text="Editar", fg_color="#442B2B", hover_color="#523939", width=10, height=15, command=editar, font=("roboto", 20, "bold"))
filter_button = ctk.CTkButton(frame2, text="=", fg_color="#442B2B", hover_color="#523939", width=10, height=15, command=filter, font=("roboto", 20, "bold"))
filter_button_option = ctk.CTkOptionMenu(frame2, fg_color="#442B2B",width=100, height=10, values=filtros,font=("roboto",20, "bold"), dropdown_fg_color="#442B2B", button_color="#442B2B")
filter_button_close = ctk.CTkButton(filter_button_option, text="x", fg_color="#251919", hover_color= "#7A6767", width=15, height=15,
                                                corner_radius=100, font=("roboto", 20, "bold"), command=filter_close)
confirm_button = ctk.CTkButton(frame_anadir, text="Confirmar", fg_color="#251919", hover_color="#7A6767", width=10, height=15, command=confirm, font=("roboto", 20, "bold"))
event_information_button = ctk.CTkButton(frame_anadir, text="i", fg_color="#251919", hover_color="#7A6767", width=15, height=10, 
                                         corner_radius=100, command=informacion, font=("roboto", 20, "bold"))


##Radios
radio1 = ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[0].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio2 = ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[1].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio3 = ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[2].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio4 = ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[3].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio5 = ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[4].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio6 = ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[5].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio7 = ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[6].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio8 = ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[7].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio9 = ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[8].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio10= ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[9].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radio11= ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[10].name, hover_color="#6D5757", font=radio_font, corner_radius= 90)
radios = [radio1,radio2,radio3,radio4,radio5,radio6,radio7,radio8,radio9,radio10,radio11]

##Cerrar
button_cerrar_anadir = ctk.CTkButton(frame_anadir, text="X", corner_radius=100, hover_color="#251818", command=anadir_cerrar, width=30, height=30, fg_color="#160E0E")
button_cerrar_information = ctk.CTkButton(frame_informacion, text="X", corner_radius=100, hover_color="#251818", command=informacion_cerrar, width=30, height=30, fg_color="#160E0E")

start()

window.mainloop()