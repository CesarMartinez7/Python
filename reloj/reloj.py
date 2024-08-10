import customtkinter
import tkinter
import datetime

hora_actualizada = None
fecha_actualizada = None

def actu_hora():
    global hora_actualizada
    hora_fecha=datetime.datetime.now()
    hora=hora_fecha.strftime("%H:%M:%S")
    hora_actualizada=hora
    label.configure(text=hora_actualizada)
    label.after(1000,actu_hora)


def change_color():
    app._set_appearance_mode("Light")


app=customtkinter.CTk()
app.title("Reloj Digital")
app.resizable(False,False)
label=customtkinter.CTkLabel(app,text="",font=("console",100))

boton=customtkinter.CTkButton(app,text="Cambiar color",command=change_color)

label.pack()
app.geometry("400x160")
boton.pack()    
actu_hora()

app.mainloop()
