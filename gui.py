import customtkinter as ctk
from datetime import datetime
from PIL import Image


#Funciones de botones

def anadir():
    print(add_button._text)

def eliminar():
    print(remove_button._text)

def verall():
    print(full_list_button._text)

def informacion():
    print(information_button._text)

def actual_time(actual_time):
    tiempoactual = tiempoactual.strftime("%H:%M:%S")
    return actual_time

tiempoactual=datetime.now()

#Seteo de GUI

ctk.set_appearance_mode("dark")

ctk.DrawEngine.preferred_drawing_method="circle_shapes"

window = ctk.CTk(fg_color="#160F0F")

imagen = Image.open("/home/braian/PROYECTO/Codigo/background.jpg")

global_font = ctk.CTkFont("liberation sans", size=40)

fondo_ctk = ctk.CTkImage(light_image= imagen, dark_image = imagen, size=(1280,720))
label_fondo = ctk.CTkLabel(window, image=fondo_ctk)

window.geometry("1280x720")


window.minsize(width=1280, height=720)
window.maxsize(width=1280, height=720)

window.title("Gestor de Turnos")

frame1 = ctk.CTkFrame(window, fg_color="#221515", width=600, corner_radius=30)
frame2 = ctk.CTkFrame(window, fg_color="#221515", corner_radius=30)
frame3 = ctk.CTkFrame(window, fg_color="#221515", corner_radius=30)

titulo = ctk.CTkLabel(frame1, width=500, height=70, text='Estudio Musical "Botaos Gang"', font=("liberation sans", 25, "bold"))
subtitulo = ctk.CTkLabel(frame1, text="Gestor de turnos", font=("liberation sans", 20))
hora = ctk.CTkLabel(window, text=())

add_button = ctk.CTkButton(frame2, width=260, height=130, text="Anadir", corner_radius=14, fg_color="#332323", hover_color="#523939", command=anadir, font=global_font)
remove_button = ctk.CTkButton(frame2, width=260, height=130, text="Remover", corner_radius=14, fg_color="#332323", hover_color="#523939", font=global_font, command=eliminar)
full_list_button = ctk.CTkButton(frame3, width=260, height=130, text="Ver todos", corner_radius=14, fg_color="#332323", hover_color="#523939",font=global_font, command=verall)
information_button = ctk.CTkButton(frame3, width=260, height=130, text="Informacion", corner_radius=14, fg_color="#332323", hover_color="#523939", font=global_font, command=informacion)
add_button.configure(ctk.CTkFont("helvetica"))

add_button.pack(padx=60, pady= 50, side="left")
remove_button.pack(padx=60, pady=50, side="right")
full_list_button.pack(padx=60, pady=50, side="left")
information_button.pack(padx=60, pady=50, side="right")


#Empaqueteos
frame1.pack()
frame2.pack(pady=40)
frame3.pack()
titulo.pack()
subtitulo.pack()
label_fondo.place(relx=0, rely=0)
hora.place(relx = 0.8, rely = 0.1)

window.mainloop()