import subprocess
import customtkinter as ctk
from pyperclip import copy
import pyperclip
import tkinter

#FUENTES
custom_font = ("Helvetica", 20, "bold")
custom_font_informacion=("Helvetica",10,"bold")


# GETTER DE EL ENTRY DEL USUARIO
def guardar_datos():
    global text
    text=entrada.get()
    print(text)
    


#PARA CERRAR LA PANTALLA CON EL BOTON
def cerrar_pantalla():
    app.destroy()
    

# CONSULTA Y MANEJO DE LA CONTRASEÑA    
def consulta_contraseña():
    name_wifi=text
    result=subprocess.run(["netsh","wlan","show","profile",name_wifi,"key=clear"],
                          stdout=subprocess.PIPE,)
    salida=result.stdout.decode("latin1")
    for linea in salida.split("\n"):
        if "Key Content" in linea or "Contenido de la clave" in linea:
            # print(f"La Contraseña de {name_wifi} ES :   {linea.split(":")[1].strip()}")
            global contraseña_texto
            contraseña_texto=str(linea.split(":")[1].strip())
            print(contraseña_texto)
            copy(contraseña_texto)
            return contraseña_texto
        else:
            print("No estas conectado a esa red o mejor espera")

#APP TKINTER
app=ctk.CTk()
app.title("HACKER WIFI")

ctk.set_appearance_mode("Light")  # Cambia a modo oscuro

encabezado=ctk.CTkLabel(app,text="HACKER WIFI ▬▬ι═══════ﺤ",font=custom_font,width=350,height=100)
encabezado.pack(pady=10)

informacion=ctk.CTkLabel(app,text="Si el nombre de la red es exactamente igual, el programa copiara automaticamente la contraseña",font=custom_font_informacion)
informacion.pack()


entrada=ctk.CTkEntry(app,placeholder_text_color="white",width=200,placeholder_text="Nombre de red")
entrada.pack(pady=10)



app.geometry("480x300")
app.resizable(False,False)


boton_enviar = ctk.CTkButton(app, text="Enviar", command=guardar_datos)
boton_enviar.pack( pady=2, padx=20)

# Crear botón Cerrar
boton_cerrar = ctk.CTkButton(app, text="Cerrar", command=cerrar_pantalla)
boton_cerrar.pack( pady=2, padx=1)




# FINAL APP TKINTER
app.mainloop()



# Mejora de hacer que no se ejecute esto y se copie automaticamente despues de cerrar con pyperclip pero desde la interfaz de tkinter
consulta_contraseña()

# CAMBIOS A REALIZAR


#PONER EL LOS BOTONES EN COLUMNAS PARA QUE SE VEA MAS ORDENADO
