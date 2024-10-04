import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
import sys



print(sys.executable)


class Interfaz(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.geometry("400x400")
        self.title("CREATE")
        self.iconbitmap("./crud/Python/crud/image.ico")
        self.resizable(False,True)
        self.tittle = ctk.CTkLabel(self,200,20,text="Bienvenido",font=("Times new roman",30)).pack_configure(pady=30)
        self.emailEntry = ctk.CTkEntry(self,placeholder_text="Email",width=200)
        self.emailEntry.pack(pady=20)
        self.contraseñaEntry = ctk.CTkEntry(self,placeholder_text="Contraseña",width=200,show=".")
        self.contraseñaEntry.pack()
        self.boton = ctk.CTkButton(self,text="Enviar al DB",width=200,command=self.obtener_Datos)
        self.boton.pack_configure(pady=20)
        self.buttonQUIT = ctk.CTkButton(master=self,text="Cerrar",fg_color="red",hover_color="#cc2424",command=self.Quit,width=200)
        self.buttonQUIT.pack_configure(pady=4,padx=30)
    
    
    def Quit(self):
        sys.exit()
    
    
    def obtener_Datos(self):
        if len(self.emailEntry.get()) >= 5 and len(self.contraseñaEntry.get()) >= 5:
            self.emailClean = self.emailEntry.get()
            self.contraseñaClean = self.contraseñaEntry.get()
            print(self.emailClean,self.contraseñaClean)
            self.GuardarDB(self.emailClean,self.contraseñaClean)
        else:
            self.error = messagebox.showerror(title="Error",message="Por favor rellene los campos correctamente")
    
    def GuardarDB(self,email,contraseña):
        try:
            db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="oyasumipunpun",
            database="crud")

            mycursor = db.cursor()
            sql = "INSERT INTO PERSONA (email,contraseña) values (%s,%s)"
            datos = (email,contraseña)
            mycursor.execute(sql,datos)
            db.commit()
            print("Todo insertado")
        except Exception as e:
            messagebox.showinfo(message=f"Lo sentimos el error fue {e}")
            

    
    
    
inte = Interfaz()

inte.mainloop()




