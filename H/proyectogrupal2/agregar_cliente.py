import os
import json
import getpass
from colorama import init, Fore, Back, Style, Cursor
init(autoreset=True)
from time import sleep

# Se define variable para guardar clientes

clientes = []

# Se define variable para limpiar pantalla

def enter_continuar ():
    input(Fore.GREEN + Style.BRIGHT + "\n Presione enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")
    print(Style.RESET_ALL)
    return

# Se define variable para mostrar        
def mostrar(clientes):
    print(Fore.YELLOW + Style.BRIGHT + "LISTADO DE CLIENTES ACTUALIZADO")
    print("-" * 120)
    print(f"{'dni':^10} {'nombre':^15} {'email':^25} {'telefono':^15} {'profesion':^20} {'disponibilidad':^20}")
    print("-" * 120)
    for cliente in clientes:
        print(f"{cliente['dni']:^10} {cliente['nombre']:^15} {cliente['email']:^25} {cliente['telefono']:^15} {cliente['profesion']:^20} {cliente['disponibilidad']:^20}")
    print("-" * 120)
    enter_continuar()   
    return clientes

# Funcion para agregar clientes

def agregar_cliente(clientes):
    while True:
        dni = input('\nIngrese el número del DNI del cliente: ')
        nombre = input('Ingrese el nombre del cliente: ').capitalize()
        email = input('Ingrese el correo electrónico del cliente: ').lower()
        telefono = input('Ingrese el número de teléfono del cliente: ')
        profesion = input('Ingrese la profesión del cliente: ').capitalize()
        disponibilidad = input('Ingrese la disponibilidad del cliente: ').capitalize()

        cliente = {
            "dni": dni,
            "nombre":nombre,
            "email": email,
            "telefono": telefono,
            "profesion": profesion,
            "disponibilidad": disponibilidad
            }

        clientes.append(cliente)
        
        #clientes[dni] = [nombre, email, telefono, profesion, disponibilidad]
        print(Fore.BLUE + Style.BRIGHT + 'Cliente agregado con éxito!')

        archivo = open("clientes_db.json", "w")
        json.dump(clientes, archivo, indent=4)
        archivo.close()

        mostrar(clientes)
        

        continuar = input('¿Desea agregar otro cliente? S/N: ').upper()
        if continuar == "N":
            break
        
    return clientes    
    
    


