import qrcode





def generador():
    datos=str(input("Ingrese La Url: "))
    nombre_archivo=str(input("Ingrese el nombre del archivo(PNG): "))
    qr=qrcode.make(datos,box_size=10)
    qr.save(f"{nombre_archivo}.png")




if __name__ == "__main__":
    generador()