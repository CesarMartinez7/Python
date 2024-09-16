import customtkinter as ctk
import qrcode as qr
import tkinter as tk
from PIL import Image,ImageTk
import os


class Interfaz(ctk.CTk):
    def __init__(self,nombre_archivo):
        super().__init__()
        self.title("QR")
        self.geometry("400x420")
        self.nombre_archivo=nombre_archivo
        self.resizable(False,False)
        self.configure(bg="white")
        self.iconbitmap("./qr_tkinter/dexter.ico")


        if not os.path.exists("./qr_tkinter"):
            os.makedirs("./qr_tkinter")

        

        self.titulo=ctk.CTkLabel(self,width=400,text="Bienvenido a QRCODE 👋",font=("Console",20)).pack(pady=10,padx=20)

        self.entry=ctk.CTkEntry(self,placeholder_text="Inserte Url",width=200,corner_radius=20,height=20)
        self.entry.pack(pady=20)
        self.entry.bind("<Return>",command=self.generar_qr)

        self.botton=ctk.CTkButton(self,command=self.generar_qr,text="Generar QR CODE",hover_color="#4299D7")
        self.botton.pack(pady=20)
        

        self.cuadro=ctk.CTkLabel(self,text="")
        self.cuadro.pack()

        self.footer=ctk.CTkLabel(self,text="By Cesar Martinez")
        self.footer.pack_configure(padx=100,pady=50)
        
        
    def generar_qr(self):
        self.datos_final=self.entry.get()
        if self.datos_final:
            self.make_qr()
            self.carga()
            self.cuadro.configure(image=self.imagen_tk)
    
    def make_qr(self):
        codigo=qr.make(data=self.datos_final,box_size=2)
        codigo.save(f"./qr_tkinter/{self.nombre_archivo}.png")

    def carga(self):
        self.image=Image.open(f"./qr_tkinter/{self.nombre_archivo}.png")
        self.image=self.image.resize((240,240))
        self.imagen_tk=ImageTk.PhotoImage(self.image)

app=Interfaz("cesar")
app.mainloop()


