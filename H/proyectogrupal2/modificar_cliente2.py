import os
import json
import getpass
from colorama import init, Fore, Back, Style, Cursor
init(autoreset=True)
from time import sleep

#variable para modificar clientes

clientes = []
        

# Funciones
# Se define variable para limpiar pantalla

def enter_continuar ():
    input(Fore.GREEN + Style.BRIGHT + "\n Presione enter para continuar...")
    print(Style.RESET_ALL)
    os.system("cls" if os.name == "nt" else "clear")
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
        


# Funcion para modificar clientes
def modificar_cliente(clientes):
    print("\nModificando clientes")
    print("-"*20)
    dni = input(f"Ingrese el DNI del empleado a modificar: ")

    # Validar que el DNI sea un número entero
    if not dni.isdigit():
        print("DNI inválido. Debe ser un número.")
        enter_continuar()
        return clientes

    dni = int(dni)
 
    clienteEncontrado = False
    for cliente in clientes:
        if cliente['dni'] == dni:
            clienteEncontrado = True
            print(f"Cliente encontrado: {cliente['nombre']}")
            nombre = input(f"Ingrese nuevo nombre:  (enter para omitir) {''}").title()
            email = input(f"Ingrese nuevo correo electrónico: (enter para omitir) {''}")
            telefono = input(f"Ingrese nuevo número de teléfono: (enter para omitir) {''}")
            profesion = input(f"Ingrese nueva profesión: (oprima enter para omitir) {''}").title()
            disponibilidad = input(f"Ingrese nueva disponibilidad: (Enter para omitir) {''}").title()
            
            if nombre != "":
                cliente["nombre"] = nombre
            if email != "":
                cliente["email"] = email
            if telefono != "":
                while True:
                    try:
                        cliente["telefono"] = int(telefono)
                        break
                    except ValueError:
                        print("Número de teléfono inválido. Debe ser un número.")
                        telefono = input("Ingrese nuevo número de teléfono: (enter para omitir) ")
            if profesion != "":    
                cliente["profesion"] = profesion
            if disponibilidad != "":
                cliente["disponibilidad"] = disponibilidad
        
           
            print(Fore.BLUE + Style.BRIGHT + f'¡La modificación de {nombre} con DNI {dni} se ha realizado con éxito!')
        
            archivo = open("clientes_db.json", "w")
            json.dump(clientes, archivo, indent=4)
            archivo.close()
            
            mostrar(clientes)
            
            break

    if clienteEncontrado == False:
        print("No existe un cliente con ese DNI.")
        print(Fore.GREEN + Style.BRIGHT + "La modificación fue cancelada.")
        enter_continuar()
    return clientes
    
# while True:
#      modificar_cliente()
#      continuar = input('¿Desea modificar otro cliente? S/N: ').upper()
#      if continuar  == 'S':
#          modificar_cliente()
#      else:
#          break

#modificar_cliente()
