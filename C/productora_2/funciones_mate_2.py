
import os

from colorama import init, Fore, Style

from empleados_mate import empleados

def cabecera(leyenda, cantidadCaracter=80):
    os.system("cls" if os.name == "nt" else "clear")
    cantMedio = cantidadCaracter - 2
    print(Fore.BLUE + "°" * cantidadCaracter)
    print(Fore.YELLOW + f"°{leyenda.center(cantMedio, ' ')}°")
    print(Fore.BLUE + "°" * cantidadCaracter)

def enterpara_continuar():
    input(Fore.YELLOW + "Presione enter para continuar")
    os.system("cls" if os.name == "nt" else "clear")  

def creditos():
    cabecera("CREDITOS", 55)
    print (Fore.CYAN +"Estos son los participantes del proyecto")
    print (Fore.BLUE + """
            1 - Nadia Fabiana Cajal - DNI 30.541.146
            2 - Celeste Vallejos - DNI 31.916.536
            3 - Juan Percaz - DNI 30.649.351
            4 - Lautaro Nahuel Machado - DNI 40.317.966""")
    
    enterpara_continuar()



def alta_empleado():
    cabecera("ALTA DE EMPLEADO", 55)
    print(Fore.CYAN + "Por favor, ingrese los siguientes datos del nuevo empleado: ")
    
    nuevo_empleado = {
        "Dni": int(input(Fore.YELLOW + "Ingrese DNI: ")),
        "Nombre": input(Fore.YELLOW + "Ingrese Nombre Completo: "),
        "Edad": int(input(Fore.YELLOW + "Ingrese la edad del empleado: ")),
        "Profesion": input(Fore.YELLOW + "Ingrese Profesión: "),
        "Proyecto": input(Fore.YELLOW + "Ingrese el Proyecto asignado: ")
    }
    
    empleados.append(nuevo_empleado)
    print(Fore.GREEN + f"Empleado agregado: {nuevo_empleado}")
    enterpara_continuar()

def baja_empleados():
    cabecera("BAJA DE EMPLEADO", 55)
    print(Fore.CYAN + "Dando de baja empleados")
    
    empleadoa_borrar = int(input(Fore.YELLOW + "Ingrese el Dni del empleado: "))
    for empleado in empleados:
        if empleado["Dni"] == empleadoa_borrar:
            empleados.remove(empleado)
            print(Fore.GREEN + f"Empleado borrado: {empleado}")
            break
    else:
        print(Fore.RED + "Empleado no encontrado")
    
    enterpara_continuar()

def modificar_empleados():
    cabecera("MODIFICAR EMPLEADO", 55)
    buscador_deempleados = int(input(Fore.YELLOW + "Ingrese el Dni del empleado: "))

    for empleado in empleados:
        if empleado["Dni"] == buscador_deempleados:
            Dni = input(Fore.YELLOW + f"Nuevo Dni({empleado['Dni']}): (Presiona Enter para no cambiar la información) ")
            Nombre = input(Fore.YELLOW + f"Nuevo Nombre({empleado['Nombre']}): (Presiona Enter para no cambiar la información) ")
            Edad = input(Fore.YELLOW + f"Nueva Edad({empleado['Edad']}): (Presiona Enter para no cambiar la información) ")
            Profesion = input(Fore.YELLOW + f"Nueva Profesión({empleado['Profesion']}): (Presiona Enter para no cambiar la información) ")
            Proyecto = input(Fore.YELLOW + f"Nuevo Proyecto({empleado['Proyecto']}): (Presiona Enter para no cambiar la información) ")

            if Dni != "":
                empleado["Dni"] = int(Dni)
            if Nombre != "":
                empleado["Nombre"] = Nombre
            if Edad != "":
                empleado["Edad"] = int(Edad)
            if Profesion != "":
                empleado["Profesion"] = Profesion
            if Proyecto != "":
                empleado["Proyecto"] = Proyecto

            print(Fore.GREEN + f"Empleado modificado: {empleado}")
            enterpara_continuar()
            break
    else:
        print(Fore.RED + "Empleado no encontrado")

def buscar_empleados():
    cabecera("BUSCAR EMPLEADO", 55)
    print(Fore.CYAN + "Búsqueda de empleados")
    empleado_busqueda = input(Fore.YELLOW + "Ingrese un nombre a buscar: ")
    
    encontrado = False
    for empleado in empleados:
        if empleado_busqueda.lower() in empleado["Nombre"].lower():
            print(Fore.CYAN + f"""Datos del empleado:
            {Fore.YELLOW}DNI: {Fore.RESET}{empleado["Dni"]}
            {Fore.YELLOW}Nombre: {Fore.RESET}{empleado["Nombre"]}
            {Fore.YELLOW}Edad: {Fore.RESET}{empleado["Edad"]}
            {Fore.YELLOW}Profesión: {Fore.RESET}{empleado["Profesion"]}
            {Fore.YELLOW}Proyecto: {Fore.RESET}{empleado["Proyecto"]}
            """)
            print(Fore.BLUE + "-" * 40)
            encontrado = True
            
    if not encontrado:
        print(Fore.RED + "No se encontraron empleados con ese nombre")
    
    enterpara_continuar()

def lista_empleados():
    cabecera("LISTA DE EMPLEADOS", 55)
    print(Fore.CYAN + "Ver lista de empleados")
    for empleado in empleados:
        print(Fore.CYAN + f"""Datos del empleado:
        {Fore.YELLOW}Dni: {Fore.RESET}{empleado["Dni"]}
        {Fore.YELLOW}Nombre: {Fore.RESET}{empleado["Nombre"]}
        {Fore.YELLOW}Edad: {Fore.RESET}{empleado["Edad"]}
        {Fore.YELLOW}Profesion: {Fore.RESET}{empleado["Profesion"]}
        {Fore.YELLOW}Proyecto: {Fore.RESET}{empleado["Proyecto"]}
        """)
        print(Fore.BLUE + "-" * 40)
    
    enterpara_continuar()