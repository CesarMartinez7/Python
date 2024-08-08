import customtkinter
import tkinter
import datetime
import pdb

def boton_call():
    hora=datetime.datetime.now()
    hora_final=hora.strftime("%H:%M:%S")
    print(hora_final)
    switch=False
    print("Boton Presionado")
    inputt.pack()
    texto=inputt.get()
    print(texto)


app=customtkinter.CTk()
app.resizable(False,False)
customtkinter.set_appearance_mode("Dark")
app.geometry("500x500")
app.title("Reloj Digital")
boton=customtkinter.CTkButton(app,text="My boton",hover_color="#5dade2",width=300,height=30,command=boton_call,fg_color=("#1a6190","#a6c0d1"))
boton.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
inputt=customtkinter.CTkEntry(master=app,placeholder_text="Usuario",placeholder_text_color="white",font=("console",10),width=400,height=23,corner_radius=10,border_color="#b3b6b7")



encabezado=customtkinter.CTkLabel(master=app, text="Reloj Digital")
encabezado.pack()
boton.pack()




app.mainloop()
