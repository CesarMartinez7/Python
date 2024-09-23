import random
import time
import pyfiglet
import datetime
import os
import qrcode
import random


#BASE DE DATOS O BIBLIOTECA, RECONOCE EL NOMBRE COMO CLAVE Y LA CONTRASEÑA COMO VALOR.
usuario_contraseñas = {"esney": "esney"}
saldo_usuario={"juan":3232}


#FECHA
def fecha():
    fechiña=datetime.datetime.now()
    formato=fechiña.strftime("%H:%M:%S")
    return formato,fechiña    

hora,_=fecha()
_,fechiña=fecha()
print(f"Hora:                      {hora}")
print(f"Fecha and hora:            {fechiña}")

#Titulo


retiro=pyfiglet.figlet_format("RETIRO",font="slant")
efecty=pyfiglet.figlet_format("efecty",font="slant")
cuatro_0_cuatro=pyfiglet.figlet_format("404 ERROR : (")
opcion_2=pyfiglet.figlet_format("VER   SALDO  ")
registro_logo=pyfiglet.figlet_format("REGISTRO   ")

#CODIGO PARA RETIRO QR
codigo_retiro=random.randint(111111,999999)
#Opciones retiro





def cupon(saldo_usuario,usuario_registrado):
    while True:
        cupones2={"milldolares":1000,
          "cesar":200,
          "python":500,
          "pythonbest":50}
        prueba_cupon=str(input("Digite su codigo de saldo:"))
        if prueba_cupon in cupones2:
            cargando()
            print("Verificando..")
            saldo_usuario[usuario_registrado]+=cupones2[prueba_cupon]
            print("Codigo canjeado correctamente\nSu saldo actual es:")
            print(f"${saldo_usuario[usuario_registrado]}")
            return saldo_usuario[usuario_registrado]
        else:
            os.system("cls")
            print(cuatro_0_cuatro)
            print(f"{cuatro_0_cuatro}\nSu codigo no esta disponible actualmente, intente otra vez")
            continue
               

def cargando():
    for i in range(1,2):
        print("     Cargando.")
        time.sleep(1.0)
        os.system("cls")
        print("     Cargando..")
        time.sleep(1.0)
        os.system("cls")
        print("     Cargando...")
        time.sleep(1.0)
        os.system("cls")
# RETIRO QR
def retiro_qr(nombre,fechiña,usuario):
    codigo=qrcode.make(f"Este es su numero de retiro: {codigo_retiro}\nRetirado por: {usuario}\nNumero de referencia:\nFecha y hora de retiro: {fechiña}\nPara mas informacion entre al siguiente link:\nhttps://www.nequi.com.co/")
    codigo.save(f"{nombre}qr_code.png")
    
#RETIRO QR MEJORADO
import qrcode

def retiro_qr_mejorado(codigo_retiro):
    qr = qrcode.QRCode()
    qr.add_data(codigo_retiro)
    qr.make()
    qr.print_ascii()


def cuenta_regresiva():
    contador=6
    while contador!=0:
        contador-=1
        print(f"La aplicacion se cerrara en:{contador}")
        time.sleep(1.0)
        os.system("cls")
        if contador==0:
            break

usuario_seguridad={"juan":1212}
def registro_de_caja(usuario_seguridad):
    codigo_seguridad=str(input("Inserte su codigo de seguridad :"))
    usuario_seguridad=[usuario_registrado]=codigo_seguridad
    breakpoint()
    return usuario_seguridad

def caja_seguridad(usuario_contraseñas,usuario_registrado):
    if codigo_seguridad not in usuario_seguridad or usuario_seguridad!=usuario_registrado:
        print("no esta")
    else:
        print("codigo se seguridad correcto")
    
    codigo_seguridad=str("Inserte codigo de seguridad para su bolsillo ")
    usuario_seguridad={"juan":1212}
    
    
    
    
    
    
    
# SALDO RETIRO
def retirar_saldo(saldo,saldo_usuario):
    cargando()
    cantidad_retiro=float(input("Cuanto desea retirar: "))
    if cantidad_retiro<=saldo_usuario[usuario_registrado]:
        opciones_retiro=int(input("Que opciones de retiro desea :\n 1. Corresponsal \n 2. Efecty\n 3. SuperGiros\nSeleccione su opcion:"))
        if opciones_retiro==1:
            codigo_retiro=random.randint(11111,99999)
            print(codigo_retiro)
            verificar_code=int(input("Ponga su codigo de seguridad: "))
            breakpoint()
            if codigo_retiro==verificar_code:
                print("Un momento...")
                cargando()
                saldo_usuario[usuario_registrado]-=cantidad_retiro
                print("Retiro exitoso")
                breakpoint()
                print(f"Tu saldo final es :{saldo_usuario[usuario_registrado]}")
            else:
                print("Codigo incorrecto")
        elif opciones_retiro==2:
            print(efecty)
            print("Acerca a tu corresponsal mas cercano de Efecty y da tu nombre de registro junto con tu numero de referencia asignado")
            retiro_qr_mejorado(codigo_retiro)
    else:
        print("Tu cantidad a retirar es mucho mas alta que tu saldo, intente otra vez")
        print(f"Saldo :{saldo_usuario[usuario_registrado]} \nTu cantidad a retirar{cantidad_retiro}")
    
        
#RE
def registro(usuario_contraseñas):
    print(" ")
    print("*****Registro NEQUI ;)*****")
    print(" ")
    print(registro_logo)
    
    usuario = input("Ingrese su usuario para registrarse: ")
    contraseña = input("Ingrese contraseña a registrarse: ")
    cargando()
    print("Registrandose en la Base de datos...")
    time.sleep(1.5)
    os.system("cls")
    usuario_contraseñas[usuario] = contraseña
    
    
registro(usuario_contraseñas)
usuario_registrado = input("Ingrese su usuario: ")
contraseña_registrada = input("Ingrese su contraseña: ")
    

#########

saldo=float(input("Inserte saldo: "))
saldo_usuario[usuario_registrado] = saldo
#breakpoint()





if usuario_registrado not in usuario_contraseñas or usuario_contraseñas[usuario_registrado] != contraseña_registrada:
        print("Buscando tu usuario en la base de datos...")
        time.sleep(1.0)
        os.system("cls")
        print("Tu usuario no está registrado\nCompruebe su usuario o contraseña")
        print(cuatro_0_cuatro)
else:
    print("Buscando tu usuario en la base de datos...")
    time.sleep(1.0)
    os.system("cls")
    print("Se encuentra tu usuario".title())
    time.sleep(1.0)
    print("Accediendo a la aplicación... NEQUI :)")
    time.sleep(1.0)
    os.system("cls")
    try:
        while True:
            print("Entrando a la aplicacion....")
            time.sleep(1.5)
            os.system("cls")
            print("Dirigiendose al Inicio....")
            time.sleep(2.5)
            os.system("cls")
            
            opciones=(input("1. Retiro QR \n2. VER SALDO\n3. Retirar saldo\n4. Ingresar dinero a nequi\n5. Salir\n6. Prestamo Nequi\n7. Cerrar Sesion\n8. Canjear codigo\n9. Salir\nSeleccione su opción: "))
            if opciones=="1":
                nombre=str(input("Inserte Nombre Para generar Codigo:  ")).capitalize()
                usuario=input("Nombre del retirante: ").capitalize()
                codigo_retiro=random.randint(11111,99999)
                retiro_qr(nombre,fechiña,usuario)
                comprueba_codigo_retiro=str(input("Inserte su codigo de digitos que fue generado por el QRcode: "))
                if comprueba_codigo_retiro==codigo_retiro:
                    cargando()
                    print("Retiro exitoso")
                    os.remove(f"{nombre}qr_code.png")
                else:
                    print("Intente again")
                    os.remove(f"{nombre}qr_code.png")
                    continue
            elif opciones=="2":
                print(opcion_2)
                print("Su saldo actual es de: ")
                print(saldo_usuario[usuario_registrado])
                decision=str(input("Desea salir al menu ?\n(SI/NO): ")).lower()
                if decision=="si" or "y" or "yes":
                    continue
            elif opciones=="tres" or opciones=="TRES" or opciones=="3" :
                print(retiro)
                retirar_saldo(saldo,saldo_usuario)
            elif opciones=="4":
                pass
            elif opciones=="5":
                pass
            elif opciones=="6":
                pass
            elif opciones=="7":
                pass
            elif opciones=="8":
                cupon(saldo_usuario,usuario_registrado)
            elif opciones=="9":
                cuenta_regresiva()
                break
            elif opciones=="10":
                pregunta=input("Se encuentra registrado en la clave de seguridad? (SI/NO)").lower()
                if pregunta=="si":
                    caja_seguridad(usuario_contraseñas,usuario_registrado)
                else:
                    registro_de_caja(usuario_seguridad)
                    caja_seguridad(usuario_contraseñas,usuario_registrado)
                    
                    
            else:
                print("Esa opcion no se encuentra disponible actualmente cacorrin")                 
    except KeyboardInterrupt:
        print("Sistema interrunpido")
    except ValueError:
        print("Compruebe insertando valor")
    except NameError:
        print("Name error xdd")
    except TypeError:
        print("Type error")
    else:
        print("ELSE DE TRY")
        
num=10 
print("es par " if num %2==0 else " no es par")