import os
import json
import getpass
from colorama import init, Fore, Back, Style, Cursor
init(autoreset=True)
from time import sleep

clientes = []
        

# Funciones
# Se define variable para limpiar pantalla

def enter_continuar ():
    input(Fore.GREEN + Style.BRIGHT + "\n Presione enter para continuar...")
    print(Style.RESET_ALL)
    os.system("cls" if os.name == "nt" else "clear")
    return

# Se define variable para mostrar el listado de clientes

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

# Funcion eliminar clientes

def eliminar_cliente(clientes):
    print("\nEliminando clientes")
    print("-"*20)
    dni = int(input("Ingrese el DNI del empleado: "))

    clienteEncontrado = False
    for cliente in clientes:
        if cliente['dni'] == dni:
            clienteEncontrado = True
            print(f"Cliente encontrado: {cliente['nombre']}")
            resp = input("¿Estás seguro de eliminar el cliente? (S/N): ").upper()
            if resp == "S":
                clientes.remove(cliente)
                print(Fore.BLUE + Style.BRIGHT + f"\n¡La eliminación del cliente {cliente['nombre']} con DNI {dni} se ha realizado con éxito!")

                archivo = open("clientes_db.json", "w")
                json.dump(clientes, archivo, indent=4)
                archivo.close()
                    
                print ()
                mostrar (clientes)
                
                
            else:
                print("Operación de eliminación fue cancelada.")
            enter_continuar()
            break
    if clienteEncontrado == False:
        print("No existe un cliente con ese DNI.")
        print(Fore.GREEN + Style.BRIGHT + "La modificación fue cancelada.")
        enter_continuar()  
    return clientes  
            
#eliminar_cliente()



