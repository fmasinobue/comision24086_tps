import os
from colorama import init, Fore,Style
init(autoreset=True)


def enter_continuar ():
    input(Fore.GREEN + Style.BRIGHT + "\n Presione enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")
    return

#Función Créditos

def creditos():
    print(Fore.LIGHTBLUE_EX +'''
Créditos:
    Desarrollado por Grupo H
    Versión 1.0
    Gracias por usar nuestro sistema.
    ''')
    enter_continuar()

