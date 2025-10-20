import customtkinter as ctk
from datetime import datetime
from PIL import Image

#Funciones de botones

def anadir():
    frame1.forget()
    frame2.forget()
    frame3.forget()   
    frame5.pack()
    anadir_titulo.place(y= -330)
    anadir_close_button.place(relx = 0.95)



def eliminar():
    print(remove_button._text)

def verall():
    frame1.forget()
    frame2.forget()
    frame3.forget()
    frame4.pack(pady = 5)
    verall_titulo.place(y = -330)
    verall_close_button.place(relx=0.95)

def informacion():
    print(information_button._text)

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

window = ctk.CTk(fg_color="#160F0F")

imagen = Image.open("/home/braian/PROYECTO/Codigo/background.jpg")

global_font = ctk.CTkFont("liberation sans", size=40)

fondo_ctk = ctk.CTkImage(light_image= imagen, dark_image = imagen, size=(1280,720))
label_fondo = ctk.CTkLabel(window,text="", image=fondo_ctk)

window.geometry("1280x720")


window.minsize(width=1280, height=720)
window.maxsize(width=1280, height=720)

window.title("Gestor de Turnos")

#Frames
frame1 = ctk.CTkFrame(window, fg_color="#221515", width=600, corner_radius=30)
frame2 = ctk.CTkFrame(window, fg_color="#221515", corner_radius=30)
frame3 = ctk.CTkFrame(window, fg_color="#221515", corner_radius=30)
frame4 = ctk.CTkFrame(window, fg_color="#221515", width= 1000, height= 700, corner_radius=30)
frame5 = ctk.CTkFrame(window, fg_color= "#221515" ,width= 1000, height=500, corner_radius=30)

#Labels
titulo = ctk.CTkLabel(frame1, width=500, height=70, text='Estudio Musical "Botaos Gang"', font=("liberation sans", 25, "bold"))
subtitulo = ctk.CTkLabel(frame1, text="Gestor de turnos", font=("liberation sans", 20, "bold"))
hora = ctk.CTkLabel(window, text=())
anadir_titulo = ctk.CTkLabel(frame5, text="Anadir Evento", width=999, height=499, corner_radius=30)
verall_titulo = ctk.CTkLabel(frame4, text="Lista de eventos:", width=999, height=699, font=("liberation sans", 20, "bold"), corner_radius=30)

#Botones
add_button = ctk.CTkButton(frame2, width=260, height=130, text="Anadir", corner_radius=14, fg_color="#332323", hover_color="#523939", command=anadir, font=global_font)
remove_button = ctk.CTkButton(frame2, width=260, height=130, text="Remover", corner_radius=14, fg_color="#332323", hover_color="#523939", font=global_font, command=eliminar)
full_list_button = ctk.CTkButton(frame3, width=260, height=130, text="Ver todos", corner_radius=14, fg_color="#332323", hover_color="#523939",font=global_font, command=verall)
information_button = ctk.CTkButton(frame3, width=260, height=130, text="Informacion", corner_radius=14, fg_color="#332323", hover_color="#523939", font=global_font, command=informacion)
add_button.configure(ctk.CTkFont("helvetica"))

##Cerrar
anadir_close_button = ctk.CTkButton(frame5, text="X", corner_radius=100, command=anadir_cerrar)
verall_close_button = ctk.CTkButton(frame4, text="X", corner_radius=100, command=verall_cerrar, width=30, height=30, fg_color="#160E0E")

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