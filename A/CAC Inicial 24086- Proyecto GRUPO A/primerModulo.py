import json
import os

from colorama import Fore, Style, init
init()


def titulo(leyenda):
    init()
    print(Style.BRIGHT + Fore.MAGENTA + "*" * 105 )
    print("*" * 105 )
    print("****", " " * 95 , "****" )
    print("****", leyenda.center(95, " "), "****" )
    print("****", " " * 95 , "****" )
    print("*" * 105 )
    print("*" * 105 + Style.RESET_ALL)


def cabecera(leyenda):
    """
    Muestra el Nombre de nuestra aplicación
    """
    print(Style.BRIGHT + Fore.BLUE + "*" * 105 )
    print("****", leyenda.center(95, " "), "****" )
    print("*" * 105 + Fore.RESET)

def validarInt(opcion):
    continuar = True
    while continuar:
        numero = input(opcion)
        if numero.isdigit():
            continuar = False
        else:
            print("Solo admito números.")
    numero = int(numero)
    return numero

def limpiarPantalla(leyenda = "Presione enter para continuar."):
    input(leyenda)
    os.system("cls")

def accederAlSistema(credenciales):
    """
    Con tope de intentos, le pide a la persona su usuario y contraseña
    para acceder al sistema. Si supera el tope el acceso es denegado.
    """
    accesoAlSistema = False
    TOPE=3
    intentos =1
    while intentos <= TOPE:
        
        usuarioIngresado = input("Usuario: ")
        contraseniaIngresada = input("Contraseña: ")


        for credencial in credenciales:
            if usuarioIngresado == credencial["usuario"] and contraseniaIngresada == credencial["contrasenia"]:
                print(Fore.GREEN + f"{credencial["usuario"]} ingresando al sistema." + Fore.RESET)
                accesoAlSistema = True
                return accesoAlSistema
        print(Fore.RED + f"Usuario o contraseña incorrecta. Utilizó {intentos}/{TOPE} intentos." + Fore.RESET)
        intentos += 1

def creditos():
    print(Fore.GREEN + "💻 DANIEL IGNACIO CORDOBA" + Fore.RESET)
    print(Fore.BLUE + "💻 MARÍA LAURA MAGRI" + Fore.RESET)
    print(Fore.YELLOW + "💻 ROBERTH JOSÉ PERDOMO DE ALBA" + Fore.RESET)
    print(Fore.MAGENTA + "💻 JAZMIN REIS" + Fore.RESET)
    limpiarPantalla()


