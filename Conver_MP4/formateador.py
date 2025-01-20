from moviepy import *

import os
from shutil import move


# Formatos de entrada y salida
formatos_input = [".mpeg"]
formato_output = ".mp4"

# Crear directorio para videos convertidos
directorio_limpio = "CleanVideo"
os.makedirs(directorio_limpio, exist_ok=True)

try:
    # Listar archivos en el directorio actual
    archivos = os.listdir()
    for archivo in archivos:
        print("Verificando archivo:", archivo)
        
        # Obtener extensión del archivo
        extension = os.path.splitext(archivo)[1]
        
        if extension in formatos_input:
            print(f"Convirtiendo {archivo} a formato MP4...")
            
            # Convertir video
            video = VideoFileClip(archivo)
            archivo_salida = f"{os.path.splitext(archivo)[0]}{formato_output}"
            video.write_videofile(archivo_salida)
            video.close()
            
            # Mover archivo convertido al directorio limpio
            ruta_destino = os.path.join(directorio_limpio, os.path.basename(archivo_salida))
            if os.path.exists(ruta_destino):
                print(f"El archivo convertido ya existe en {directorio_limpio}, sobrescribiendo...")
                os.remove(ruta_destino)
            move(archivo_salida, directorio_limpio)
            
            # Eliminar archivo original
            os.remove(archivo)
            print(f"Archivo original {archivo} eliminado.")
        
        else:
            print(f"No se requiere conversión para: {archivo}")
    
    print("Proceso completado.")

except Exception as e:
    print(f"Se produjo un error: {e}")



def mover_archivos() -> None:
    for i in archivos:
        if os.path.splitext(i)[1] in [".jpg","img","png"]:
            os.makedirs("ImagenesClean",exist_ok=True)
            move(i,"ImagenesClean")


def made_egp() -> None:
    for i in archivos:
        if os.path.splitext(i)[1] == ".3gp":
            os.makedirs("Carpeta3gp",exist_ok=True)
            move(i,"Carpeta3gp")


made_egp()
