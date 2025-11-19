import customtkinter as ctk
from classes import *
from validation import *
from PIL import Image

def start():
    frame1.pack()
    titulo.pack()
    subtitulo.pack()
    frame2.pack(pady = 10)
    eventos_titulo.place(relx = 0.03, rely = 0.05)
    add_button.place(relx = 0.94, rely = 0.04)
    filter_button.place(relx = 0.84, rely = 0.035)
    edit_button.place(relx = 0.88, rely = 0.04)
    frame_event_list.place(relx = 0.02, rely =0.13)
    check_no_event()

def check_no_event():
    if len(lista_eventos) != 0:
        render_grid()
    else:
        no_event_robot.pack(pady=8)
        no_event_label.pack()
        no_event_button.pack()

def anadir():
    no_event_button.forget()
    no_event_robot.forget()
    no_event_label.forget()
    frame_event_list.place_forget()
    frame_anadir.place(x=250,y=240)
    button_cerrar_anadir.place(relx = 0.93, rely = 0.04)
    eventos_opciones.place(relx = 0.08, rely = 0.1)
    salas_opciones.place(relx = 0.08, rely= 0.25)
    desde_hasta.place(relx = 0.68, rely = 0.12)
    start_hour.place(relx = 0.68, rely = 0.22)
    end_hour.place(relx = 0.85, rely = 0.22)
    confirm_button.place(relx = 0.80, rely = 0.88)

    #Radios
    rx, ry = 0.1, 0.4

    for i in range(11):
        
        radios[i].place(relx=rx, rely=ry)

        ry += 0.1

        if i == 5:
            rx = 0.5
            ry = 0.4

    event_information_button.place(relx=0.48,rely=0.05)

def confirm():
    evento = eventos_opciones.get()
    sala = salas_opciones.get()
    horario = (start_hour.get(), end_hour.get())
    inventario.clear()
    for i in radios:
        if i.get():
            inventario.append(i.cget("text"))
    full_event = [evento,sala,horario,inventario.copy()]
    if (validation(full_event[0], full_event[1], full_event[2],full_event[3]))[0]:
        lista_eventos.append(full_event)
        frame_succes.place(relx=0.4,rely=0.93)
        label_succes.pack()
        window.after(5000, success_forget)
    else: print(validation(full_event[0], full_event[1], full_event[2],full_event[3]))

def success_forget():
    frame_succes.place_forget()

def editar():
        edit_button.configure(text="Cancelar", width=40, command = cancelar)
        add_button.place_forget()

        editar_rearrange()
        
def editar_rearrange():
    for i in range(len(lista_eventos)):
        label_event_delete = ctk.CTkButton(frame_event_list, image=del_img,text="", fg_color="#251919", hover_color= "#7A6767", width=15, height=15,
                                                corner_radius=100, font=("roboto", 30, "bold"), command=lambda idx=i : eliminar(idx))
        label_event_delete.grid(row = i, column = 5, padx = 20, pady = 10)

def cancelar():
    edit_button.configure(text="Editar", command = editar), add_button.place(relx = 0.94, rely = 0.04)
    for i in frame_event_list.grid_slaves():
         if i.cget("image") == del_img:
            i.grid_forget()

def filter():
    filter_button.place_forget()
    filter_button_option.place(relx = 0.78, rely =0.045)
    filter_button_close.place(relx=0.8, rely=-0.05)

def filter_close():
    filter_button_option.place_forget()
    filter_button.place(relx = 0.84, rely = 0.035)
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

    frame_informacion.place(x=250, y=240)
    button_cerrar_information.place(relx = 0.93, rely = 0.04)
    Event_Information_Label = ctk.CTkLabel(frame_informacion, width=700, height=30, text=eventos_informacion,fg_color="#251818", corner_radius=6,font=("roboto", 25, "bold"), wraplength=690)
    Room_Information_Label = ctk.CTkLabel(frame_informacion, width=700, height=30, text=sala_informacion,fg_color= "#251818", corner_radius=6,font=("roboto", 25, "bold"), wraplength=690)
    Title_Event_Label = ctk.CTkLabel(frame_informacion, width=300, height=10, text=eventos_opciones._current_value, font=("roboto", 30, "bold"))
    Title_Room_Label = ctk.CTkLabel(frame_informacion, width=300, height=10, text=salas_opciones._current_value, font=("roboto", 30, "bold"))
    Event_Information_Label.place(relx=0.1, rely=0.22)
    Room_Information_Label.place(relx=0.1, rely =0.6)
    Title_Event_Label.place(relx = 0.05, rely = 0.1)
    Title_Room_Label.place(relx= 0.05, rely= 0.5)

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
            label_event_event = ctk.CTkLabel(frame_event_list, text=lista_eventos[i][0], font=("roboto", 20, "bold"), compound= "left")
            label_event_event.grid(row=i, column=0, padx=20, pady=15)

            label_event_room = ctk.CTkLabel(frame_event_list, text=lista_eventos[i][1], font=("roboto", 20, "bold"), compound="left")
            label_event_room.grid(row=i, column=1, padx=20, pady=15)

            label_event_hour = ctk.CTkLabel(frame_event_list,text=lista_eventos[i][2][0]+"-"+lista_eventos[i][2][1], font=("roboto", 20, "bold"), compound="left")
            label_event_hour.grid(row = i, column=2, padx=20, pady=15)

            label_event_info = ctk.CTkButton(frame_event_list, text="Info.", fg_color="#503636", hover_color="#7A6767", width=15, height=15, 
                                         corner_radius=100, font=("roboto", 20, "bold"), command= lambda idx=i : check_inventory(idx))
            label_event_info.grid(row = i, column=3, padx=20, pady=15)
            
def check_inventory(indice):
    current_inventory = lista_eventos[indice][3]
    print(current_inventory) 
         
def eliminar(indice):
    del lista_eventos[indice]
    render_grid()
    editar_rearrange()
    
def informacion_cerrar():
    frame_informacion.place_forget()

def radio_press(radio):
    if radio.value == 0:
        radio.value = 1
    else: radio.value = 0

def validar_start(texto:str):        
    if len(texto) == 5:
        if int(texto[3]+texto[4]) > 59:
            return False

    if texto == "":
        return True
    if len(texto) > 5:
        return False
    for i, ch in enumerate(texto):
        if i == 2 and ch != ":":
            return False
        if i != 2 and not ch.isdigit():
            return False
    return True

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

#Imagenes

add_image = Image.open("/home/braian/PROYECTO/Codigo/Images/add_event.png")
delete_image = Image.open("/home/braian/PROYECTO/Codigo/Images/delete.png")
filter_image = Image.open("/home/braian/PROYECTO/Codigo/Images/filter_list.png")
robot_image = Image.open("/home/braian/PROYECTO/Codigo/Images/no_events.png")
add_img = ctk.CTkImage(light_image=add_image, dark_image=add_image, size=(25,25))
del_img = ctk.CTkImage(light_image=delete_image, dark_image=delete_image, size=(30,30))
filter_img = ctk.CTkImage(light_image=filter_image, dark_image=filter_image, size=(30,30))
robot_img = ctk.CTkImage(light_image=robot_image, dark_image=robot_image, size=(200,200))

filtros = ["Sala A", "Sala B", "Sala C", "Album", "Mixt.", "EP", "OST"]

window = ctk.CTk(fg_color="#1D1313")

vcmd = (window.register(validar_start), "%P")

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
                                   button_color="#2B1D1D",button_hover_color="#3D2A2A", dropdown_font=("roboto", 20))
salas_opciones = ctk.CTkOptionMenu(frame_anadir,fg_color="#2B1D1D", values=nombre_salas,
                                   font=("roboto", 20, "bold"), button_hover_color="#3D2A2A", width=315,height=42,corner_radius=29, dropdown_fg_color="#2B1D1D", 
                                   button_color="#2B1D1D", dropdown_font=("roboto", 20))

eventos_titulo = ctk.CTkLabel(frame2, text="Turnos:", font=("roboto", 20, "bold"), fg_color="#442B2B", corner_radius= 10)
desde_hasta = ctk.CTkLabel(frame_anadir, text="Horario:", font=("roboto", 27))

start_hour = ctk.CTkEntry(frame_anadir, width=90, height=30, placeholder_text="00:00", validate = "key", validatecommand= vcmd)
end_hour = ctk.CTkEntry(frame_anadir, width=90, height=30, placeholder_text="00:00", validate= "key", validatecommand= vcmd)

frame_succes = ctk.CTkFrame(frame2, width=400, height=20, fg_color="transparent")
label_succes = ctk.CTkLabel(frame_succes, text="Evento anadido con exito :D", font=("roboto", 20, "bold"), corner_radius=50, bg_color="transparent", fg_color="#472828")

no_event_robot = ctk.CTkLabel(frame_event_list, width=200,height=200, corner_radius=20, image=robot_img, text="")
no_event_label = ctk.CTkLabel(frame_event_list,width=200, height=50, text="Actualmente no hay ningun turno agendado... :(", font=("roboto", 20, "bold"))
no_event_button = ctk.CTkButton(frame_event_list,width=150, height=30, fg_color="#221515", hover_color="#523939", corner_radius=15, text="Anadir turno...", font=("roboto", 20), command=anadir)

#Botones
add_button = ctk.CTkButton(frame2, text="",image=add_img, fg_color="transparent", hover_color="#523939", width=20, height=20, command=anadir, font=("roboto", 30, "bold"))
edit_button = ctk.CTkButton(frame2, text="Editar", fg_color="#442B2B", hover_color="#523939", width=10, height=15, command=editar, font=("roboto", 20, "bold"))
filter_button = ctk.CTkButton(frame2, text="", image=filter_img, fg_color="transparent", hover_color="#523939", width=10, height=15, command=filter, font=("roboto", 20, "bold"))
filter_button_option = ctk.CTkOptionMenu(frame2, fg_color="#442B2B",width=100, height=10, values=filtros,font=("roboto",20, "bold"), dropdown_fg_color="#442B2B", button_color="#442B2B")
filter_button_close = ctk.CTkButton(filter_button_option, text="x", fg_color="#251919", hover_color= "#7A6767", width=15, height=15, font=("roboto", 20, "bold"), command=filter_close)
confirm_button = ctk.CTkButton(frame_anadir, text="Confirmar", fg_color="#251919", hover_color="#7A6767", width=10, height=15, command=confirm, font=("roboto", 20, "bold"))
event_information_button = ctk.CTkButton(frame_anadir, text="i", fg_color="#251919", hover_color="#7A6767", width=15, height=10, 
                                         corner_radius=100, command=informacion, font=("roboto", 20, "bold"))

##Radios
radios = []

for i in range(11):
    radios.append(ctk.CTkCheckBox(frame_anadir, text=EQUIPOS[i].name, hover_color="#6D5757", font=radio_font, corner_radius= 90))

##Cerrar
button_cerrar_anadir = ctk.CTkButton(frame_anadir, text="X", corner_radius=100, hover_color="#251818", command=anadir_cerrar, width=30, height=30, fg_color="#160E0E")
button_cerrar_information = ctk.CTkButton(frame_informacion, text="X", corner_radius=100, hover_color="#251818", command=informacion_cerrar, width=30, height=30, fg_color="#160E0E")

start()

window.mainloop()