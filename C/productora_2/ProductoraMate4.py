# ===========================================#
#                   _
#                  | |
#                  | |
#                 _|_|_
#                //   \\
#               ||     ||
#               ||     ||
#                \\___//
#                 `---´
#                               
# ===========================================#

import os
from colorama import init, Fore, Style
from funciones_mate_2 import cabecera, creditos, enterpara_continuar, alta_empleado, baja_empleados, modificar_empleados, lista_empleados, buscar_empleados
init(autoreset=True)



# FUNCION DE VALIDACION INT
def validacionInt(leyenda, permiteEnter=False):
    while True:
        numero = input(Fore.YELLOW + leyenda)
        if permiteEnter and numero == "":
            return numero
        try:
            numero = int(numero)
            return numero
        except ValueError:
            print(Fore.RED + f"INGRESA SOLO N° POR FAVOR: ({numero})")


       
TOPE = 3
accesook = False
intentos = 1

while intentos <= TOPE:
    intentos += 1
    saludo1 = "¡BIENVENIDOS A PRODUCTORA MATE!"
    cabecera(saludo1, 55)
    #print(Fore.YELLOW + saludo1.center(80))
    usuario = input(Fore.YELLOW + "Por favor, ingrese su usuario: ")
    contraseña = input(Fore.YELLOW + "Por favor, ingrese su contraseña: ")
    
    if usuario == "admin_mate" and contraseña == "1234" or True:
        print(Fore.GREEN + "Accediendo al Sistema...")
        accesook = True
        break
    else:
        print(Fore.RED + "¡ACCESO DENEGADO AL SISTEMA!. (Usuario o contraseña incorrectos.)")
        print(Fore.YELLOW + "intenta de nuevo...")

while accesook:
    cabecera("MENU PRINCIPAL DE MATE PRODUCTORA", 55)
    print(Fore.CYAN + f"""
        {Fore.YELLOW}1. EMPLEADOS
        {Fore.YELLOW}2. CASTING
        {Fore.YELLOW}3. PROYECTOS
        {Fore.YELLOW}4. STOCK MATERIALES
        {Fore.YELLOW}5. CREDITOS
        {Fore.RED}0. SALIR DE MATE """)
    
    opcionElegida = validacionInt("Opcion: ")

    if opcionElegida == 0:
        print(Fore.GREEN + "SALIENDO DEL SISTEMA ...")
        break
    elif opcionElegida == 1:
        cabecera("EMPLEADOS", 55)
        print(Fore.YELLOW + "En este sector puedes realizar el manejo de tus empleados")
        print(Fore.CYAN + f""" 
            {Fore.RED}0 - Para volver al menú anterior
            {Fore.YELLOW}1 - Dar de alta un empleado
            {Fore.YELLOW}2 - Dar de baja un empleado
            {Fore.YELLOW}3 - Modificar datos de un empleado
            {Fore.YELLOW}4 - Buscar un empleado
            {Fore.YELLOW}5 - Ver lista de empleados 
            
            """)
        #manejo_empleados= validacionInt(Fore.YELLOW + "Elegí una opción del menú: ")
        manejo_empleados = input(Fore.YELLOW + "Elegí una opción del menú: ")

        if manejo_empleados == "1":
            alta_empleado()
        elif manejo_empleados == "2":
            baja_empleados()
        elif manejo_empleados == "3":
            modificar_empleados()
        elif manejo_empleados == "4":
            buscar_empleados()
        elif manejo_empleados == "5":
            lista_empleados()
        elif manejo_empleados == "0":
            print(Fore.GREEN + "Volviendo al menú principal...")
            #print(accesook)
        else:
            print(Fore.RED + "La opción elegida es incorrecta, vuelve a elegir")
    elif opcionElegida == 2:
        cabecera("CASTING", 55)
    elif opcionElegida == 3:
        cabecera("PROYECTOS", 55)
    elif opcionElegida == 4:
        cabecera("STOCK MATERIALES", 55)
    elif opcionElegida == 5:
        cabecera("CREDITOS", 55)
        creditos ()
    else:
        print(Fore.RED + "INGRESA UNA OPCION VALIDA POR FAVOR...")

print(Fore.GREEN + "CHAU, HASTA MAÑANA...")