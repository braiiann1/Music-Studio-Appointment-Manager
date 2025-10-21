import customtkinter as ctk
from datetime import datetime
from PIL import Image

#Funciones de botones

def anadir():
    pass

def eliminar():
    pass

def informacion():
    pass

def actual_time(actual_time):
    tiempoactual = tiempoactual.strftime("%H:%M:%S")
    return actual_time

def verall_cerrar():
    frame4.forget()
    frame1.pack()
    frame2.pack(pady=40)
    frame3.pack()
    titulo.pack()
    subtitulo.pack()
    
def anadir_cerrar():
    frame5.forget()
    frame1.pack()
    frame2.pack(pady=40)
    frame3.pack()
    titulo.pack()
    subtitulo.pack()

tiempoactual=datetime.now()

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

#Labels
titulo = ctk.CTkLabel(frame1, width=500, height=70, text='Estudio Musical "Botaos Gang"', font=("liberation sans", 25, "bold"))
subtitulo = ctk.CTkLabel(frame1, text="Gestor de turnos", font=("liberation sans", 20, "bold"))

eventos_titulo = ctk.CTkLabel(frame2, text="Lista de eventos:", font=("liberation sans", 20, "bold"), fg_color="#442B2B", corner_radius= 10)

#Botones
add_button = ctk.CTkButton(frame2, text="+", fg_color="transparent", hover_color="#523939", width=15, height=15, command=anadir, font=("liberation sans", 30, "bold"))
edit_button = ctk.CTkButton(frame2, text="Editar", fg_color="#442B2B", hover_color="#523939", width=10, height=15, font=("liberation sans", 20, "bold"))
#full_list_button = ctk.CTkButton(frame3, width=260, height=130, text="Ver todos", corner_radius=14, fg_color="#332323", hover_color="#523939",font=global_font, command=verall)
#information_button = ctk.CTkButton(frame3, width=260, height=130, text="Informacion", corner_radius=14, fg_color="#332323", hover_color="#523939", font=global_font, command=informacion)


##Cerrar
###anadir_close_button = ctk.CTkButton(frame2, text="X", corner_radius=100, command=anadir_cerrar, width=30, height=30, fg_color="#160E0E")
###verall_close_button = ctk.CTkButton(frame2, text="X", corner_radius=100, command=verall_cerrar, width=30, height=30, fg_color="#160E0E")

#Empaqueteos
frame1.pack()
titulo.pack()
subtitulo.pack()
frame2.pack(pady = 10)
eventos_titulo.place(relx = 0.03, rely = 0.05)
add_button.place(relx = 0.95, rely = 0.03)
edit_button.place(relx = 0.88, rely = 0.04)


window.mainloop()