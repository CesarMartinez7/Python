import customtkinter
import tkinter
import datetime


# NO RECUERDO MUY BIEN PARA QUE ES ESTO AHORA,
hora_actualizada = None
fecha_actualizada = None


# LO QUE HACE QUE SE ACTUALIZE LA HORA
def actu_hora():
    global hora_actualizada
    hora_fecha=datetime.datetime.now()
    hora=hora_fecha.strftime("%H:%M:%S")
    hora_actualizada=hora
    label.configure(text=hora_actualizada,)
    label.after(1000,actu_hora)

# CAMBIOS DE COLORES, COLORES OSCUROS Y COLORES CLAROS ( SOLO DOS TIPO DE COLORES)
def change_color():
    if app._get_appearance_mode()=="dark" and label._text_color=="white":
        app._set_appearance_mode("light")
        boton.configure(bg_color="#183153",fg_color="#202327",text_color="#e8e8e8")
        label.configure(text_color="#202020",fg_color="#e8e8e8")
        print("MODO CLARO")
    elif app._get_appearance_mode()=="light" and label._text_color=="#202020":
        app._set_appearance_mode("dark")
        label.configure(text_color="white",fg_color="#202327")
        boton.configure(fg_color="#e8e8e8",text_color="#202020")
        print("MODO OSCURO")

#INICIALIZACION DE LA VENTANA
app=customtkinter.CTk()
app.title("Reloj Digital")
app.resizable(False,False)
label=customtkinter.CTkLabel(app,text="",font=("console",100),text_color="white",anchor="center",)

#CAMBIOS DE COLORES(DESCARTADO)
# switch=customtkinter.CTkSwitch(master=app,text="Activar",command=change_color)

# boton de cambio de color
boton=customtkinter.CTkButton(app,text="Cambiar color",command=change_color,corner_radius=0)
# switch.pack()
label.pack()
app.geometry("400x160")
boton.pack()    
#LA FUNCION QUE HACE QUE LA HORA DEL RELOJ DE ACTUALIZE CADA 1000ms(SEGUNDOS)
actu_hora()

# LO QUE HACE QUE LA VENTANA SE MANTENGA ABIERTA
app.mainloop()
