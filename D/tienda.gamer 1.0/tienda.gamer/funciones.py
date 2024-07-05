from stock import categoriasjuegos,stockgeneral
from empleados import listaEmpleados, listaAdministradores
from colorama import Fore, Back, Style
import os
total = 0
articulostotal = 0

def cabecera(leyenda, cantidadCaracter=80):
    os.system("cls")
    cantMedio = cantidadCaracter - 2
    print(Fore.MAGENTA + "#"*cantidadCaracter + Style.RESET_ALL)
    print(f"{Fore.MAGENTA}#{Back.CYAN}{leyenda.center(cantMedio," ")}{Style.RESET_ALL}{Fore.MAGENTA}#")
    print("#"*cantidadCaracter)

def seleccionarCategoria():
    print(Fore.LIGHTCYAN_EX + "Selecciona un género de juegos:" + Style.RESET_ALL)
    for i, genero in enumerate(categoriasjuegos, 1):
        print(f"{Fore.LIGHTCYAN_EX}[{i}]. {Fore.LIGHTMAGENTA_EX}{genero}{Style.RESET_ALL}")
    
    while True:
        opcion = input(Fore.LIGHTCYAN_EX + "Ingresa el número del género deseado o 's' para salir: " + Style.RESET_ALL).strip().lower()     
        if opcion == "s":
            return False
        elif opcion.isdigit():
            indice = int(opcion) - 1
            if 0 <= indice < len(categoriasjuegos):
                return categoriasjuegos[indice]
            else:
                print(Fore.LIGHTRED_EX + "Número de género inválido. Por favor, ingresa un número válido." + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + "Entrada inválida. Por favor, ingresa un número de género válido o 's' para salir." + Style.RESET_ALL)
            
def buscarJuego(lista, nombre):
    resultados = []
    for juego in lista:
        if nombre.lower() in juego["Juego"].lower():
            resultados.append(juego)
    return resultados

def agregarAlCarrito(juegos):
    global total
    global articulostotal
    carrito = []
    while True:
        print(Fore.MAGENTA + "Juegos disponibles:" + Style.RESET_ALL)
        for i, juego in enumerate(juegos, 1):
            print(f"{Fore.LIGHTCYAN_EX}{i}.{Fore.LIGHTMAGENTA_EX}{juego['Juego']}: ${juego['Precio']} - Stock: {juego['Stock']}{Style.RESET_ALL}")
        opcion = input(Fore.LIGHTCYAN_EX + "\nIngrese el número del juego que desea agregar al carrito  ('s' para salir): " + Style.RESET_ALL)
        if opcion == "s":
            break
        elif opcion == "":
            print(Fore.LIGHTRED_EX + "Seleccione una opcion númerica" + Style.RESET_ALL)
            pausa3 = input(Fore.LIGHTMAGENTA_EX + "\nPresione enter para continuar" + Style.RESET_ALL)
        if opcion.isdigit() and 0 < int(opcion) <= len(juegos):
            juego_seleccionado = juegos[int(opcion) - 1]
            if juego_seleccionado['Stock'] > 0:
                carrito.append((juego_seleccionado['Juego'], juego_seleccionado['Precio']))
                print(f"{Fore.LIGHTGREEN_EX}'{juego_seleccionado['Juego']}' agregado al carrito.{Style.RESET_ALL}")
                juego_seleccionado['Stock'] -= 1
                total += juego_seleccionado['Precio']
                articulostotal += 1  
            else:
                print(Fore.LIGHTRED_EX + "¡Lo siento, este juego está agotado!" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + "Opción inválida. Por favor, ingrese un número válido." + Style.RESET_ALL)
    return carrito

def compratarjeta():
    global total
    global articulostotal
    print(f"{Fore.LIGHTCYAN_EX}La cantidad de articulos comprados es: {Fore.GREEN}{articulostotal}{Fore.LIGHTCYAN_EX}.\nEl monto total es: {Fore.GREEN}{total:.2f}${Style.RESET_ALL}")
    compra = True
    while compra:
        formaDePago = input(Fore.LIGHTCYAN_EX + "Ingresa tu forma de pago a utilizar (A Efectivo, B Credito): " + Style.RESET_ALL)
        if formaDePago == "A":
            print(f"{Fore.LIGHTMAGENTA_EX}Tu importe a abonar no tiene recargo extra!. Paga {Fore.GREEN}{total:.2f}{Fore.LIGHTMAGENTA_EX} \nCompra exitosa!. Buen día.{Style.RESET_ALL}")
            compra = False
        elif formaDePago == "B":
            total = total * 1.30
            print(f"{Fore.MAGENTA}La forma de pago que quiere utilizar cuenta con un recargo extra del 30%, dejando su monto a abonar en un total de {Fore.GREEN}{total:.2f}.{Style.RESET_ALL}")
            eleccion = True
            while eleccion:
                continuarONo = input(Fore.LIGHTCYAN_EX + "¿Desea continuar la compra? Indica 'Si' para continuar, 'No' para volver a seleccionar la forma de pago.: " + Style.RESET_ALL)
                if continuarONo == "Si":
                    print(Fore.GREEN + "Compra exitosa!. Buen día." + Style.RESET_ALL)
                    compra = False
                    eleccion = False
                elif continuarONo == "No":
                    print(Fore.MAGENTA + "Vuelve a ingresar para elegir nuevamente la forma de pago" + Style.RESET_ALL)
                    eleccion = False
                else:
                    print(Fore.RED + "Opción incorrecta, vuelve a ingresar." + Style.RESET_ALL)
        elif formaDePago != "A" and  "B":
            print(Fore.RED + "Seleccion inválida. Seleccione A o B " + Style.RESET_ALL)
        else:
            print(Fore.RED + "Forma de pago inválida. Por favor, ingresa 'A' para Efectivo o 'B' para Crédito." + Style.RESET_ALL)

def obtenerLegajo(lista, busqueda):
    for empleado in lista:
            if empleado["Legajo"] == busqueda:
                return True
    return False

def obtenerJuego(lista, busqueda):
    for juego in lista:
            if juego["Nombre"] == busqueda:
                return True
    return False
    


def nuevoEmpleado():
    empleado = True 
    empleadosalir = False
    while empleado:
        Nombre = input(Fore.LIGHTCYAN_EX + "Ingrese el Nombre ('q' para salir): " + Style.RESET_ALL)
        if Nombre == "q":
            empleadosalir = True
            break
        Apellido = input(Fore.LIGHTCYAN_EX + "Ingrese el Apellido: " + Style.RESET_ALL)
        while True:
            Edad = input(Fore.LIGHTCYAN_EX + "Ingrese la Edad: " + Style.RESET_ALL)
            if Edad.isdigit():
                int(Edad)
                break
            else:
               print(Fore.RED + "Eso no es un número" + Style.RESET_ALL) 
        while True:
            Sector = input(Fore.LIGHTCYAN_EX + "Ingrese el Sector que ocupará (Empleado/Administrador): " + Style.RESET_ALL)
            if Sector !="Empleado" and Sector != "Administrador":
                print(Fore.RED + "Sector incorrecto, vuelva a ingresar" + Style.RESET_ALL)
            else:
                break
        while True:          
            Legajo = input(Fore.LIGHTCYAN_EX + "Ingrese su número de legajo físico: " + Style.RESET_ALL)
            if Legajo.isdigit():
                Legajo = int(Legajo)
                if obtenerLegajo(listaEmpleados, Legajo):
                    print(f'{Fore.RED}El Legajo {Legajo} ya existe{Style.RESET_ALL}')
                elif obtenerLegajo(listaAdministradores, Legajo):
                    print(f'{Fore.RED}El Legajo {Legajo} ya existe{Style.RESET_ALL}')
                else:
                     print(f'{Fore.GREEN}Se puede agregar el Legajo {Legajo}{Style.RESET_ALL}')
                     break
            else:
                print(Fore.RED + "Ingrese un N° de legajo válido" + Style.RESET_ALL)
        confirmacion = True
        while confirmacion == True:
            Usuario = input(Fore.LIGHTMAGENTA_EX + "Ingrese su usuario para acceder al sistema: " + Style.RESET_ALL)
            if Usuario == "":
                print(Fore.RED + "Usuario no puede estar en blanco, ingrese nuevamente" + Style.RESET_ALL)
            else:
                while True:
                    clave = input(Fore.LIGHTCYAN_EX + "Ingrese la clave para acceder al sistema: " + Style.RESET_ALL)
                    if clave == "":
                        print(Fore.RED + "La clave no puede estar en blanco, ingrese nuevamente" + Style.RESET_ALL)
                    else:
                        confirmacion = False
                        empleado = False
                        break
    if empleadosalir == False:            
        if Sector == "Empleado":
            input(Fore.GREEN + "Empleado cargado con exito" + Style.RESET_ALL)
        else:
            print (Fore.LIGHTGREEN_EX + "Administrador cargado con exito" + Style.RESET_ALL)      

        nuevoEmpleado =  {
        "Nombre": Nombre,
        "Apellido": Apellido,
        "Edad": Edad,
        "Sector": Sector,
        "Legajo": Legajo,
        "Usuario": Usuario,
        "clave": clave
    }
        if Sector == "Empleado":
            listaEmpleados.append(nuevoEmpleado)
        elif Sector == "Administrador":
            listaAdministradores.append(nuevoEmpleado)
        return listaEmpleados,listaAdministradores



def elimEmpleado():
    quitarEmpleado = True
    while quitarEmpleado:
        print(Fore.GREEN + "Eliminando Empleado" + Style.RESET_ALL)
        empleadoExiste = True
        while empleadoExiste:
            empleado_a_quitar = input (Fore.LIGHTCYAN_EX + "Número de Legajo físico: " + Style.RESET_ALL)
            empleado_encontrado = False
            for empleado in listaEmpleados:
                if empleado["Legajo"] == int(empleado_a_quitar):
                    listaEmpleados.remove(empleado)
                    empleado_encontrado = True
                    print (Fore.GREEN + "Empleado Eliminado " + Style.RESET_ALL)
                    break
            if not empleado_encontrado:
                print(Fore.RED + "Empleado no encontrado en el inventario." + Style.RESET_ALL)
            while True:
                salir = input(Fore.LIGHTCYAN_EX + "¿Desea continuar eliminando? s/n: " + Style.RESET_ALL).lower()
                if salir == "s":
                    break
                elif salir == "n":
                    quitarEmpleado = False
                    break
                else:
                    print (Fore.RED + "Opcion incorrecta" + Style.RESET_ALL)
            break

def nuevoJuego():
    juegoNuevo = True
    while juegoNuevo:
        while True:
            juegoagregadon = input (Fore.LIGHTCYAN_EX + "Ingrese el nombre del juego ('q' para salir): " + Style.RESET_ALL)
            if juegoagregadon == "q":
                juegoNuevo = False
                break
            elif juegoagregadon == "":
                input (Fore.LIGHTCYAN_EX + "No puede estar vacio este campo, presiona una tecla para volver a intentarlo" + Style.RESET_ALL)
            else:
                juego_existe = False
                for juego in stockgeneral:
                    if juego["Juego"].lower() == juegoagregadon.lower():
                        print(Fore.LIGHTCYAN_EX + "Ese juego ya existe" + Style.RESET_ALL)
                        juego_existe = True
                        break
                if not juego_existe:
                    break
        while True:
            juegoagregados = input(Fore.LIGHTCYAN_EX + "Ingrese la cantidad de stock: " + Style.RESET_ALL)
            if juegoagregados.isdigit():
                int(juegoagregados)
                break
            else:
               print(Fore.RED + "Eso no es un numero" + Style.RESET_ALL) 
        juegoagregadog = input (Fore.LIGHTCYAN_EX + "Ingrese el genero: " + Style.RESET_ALL)
        while True:
            juegoagregadop = input(Fore.LIGHTCYAN_EX + "Ingrese el valor: " + Style.RESET_ALL)
            if juegoagregadop.isdigit():
                int(juegoagregadop)
                break
            else:
               print(Fore.RED + "Eso no es un numero" + Style.RESET_ALL)        
        nuevo_juego = {
            "Juego":juegoagregadon,
            "Stock":juegoagregados,
            "Genero":juegoagregadog,
            "Precio":juegoagregadop
            } 
        stockgeneral.append(nuevo_juego)
        categoriasjuegos.append(juegoagregadog)
        print(lista_Juegos_Tab())
        break

def elimJuegos(lista, busqueda):
    quitarsalir = True
    while quitarsalir:
        print(Fore.LIGHTCYAN_EX + "Stock Actual" + Style.RESET_ALL)
        lista_Juegos_Tab()
        juegoexiste = True
        while juegoexiste:
            juegoaquitar = input (Fore.MAGENTA + "¿Que juego desea quitar?: " + Style.RESET_ALL).lower()
            juego_encontrado = False
            for juego in lista:
                if juego["Juego"].lower() == juegoaquitar: 
                    lista.remove(juego)
                    juego_encontrado = True
                    print (Fore.GREEN + "Stock Modificado: " + Style.RESET_ALL)
                    lista_Juegos_Tab()
            if not juego_encontrado:
                print(Fore.RED + "Juego no encontrado en el inventario." + Style.RESET_ALL)
            while True:
                quitarsalir1 = input (Fore.LIGHTCYAN_EX + "¿Desea continuar eliminando? s/n: " + Style.RESET_ALL).lower()
                if quitarsalir1 == "s":
                    break
                elif quitarsalir1 == "n":
                    quitarsalir = False
                    break
                else:
                    print (Fore.RED + "Opcion incorrecta" + Style.RESET_ALL)
            break

def lista_Juegos_Tab():
    os.system("cls")
    print(f"{Fore.LIGHTMAGENTA_EX}{'NOMBRE':30} {Fore.LIGHTCYAN_EX}| {Fore.LIGHTMAGENTA_EX}{'PRECIO':10} {Fore.LIGHTCYAN_EX}| {Fore.LIGHTMAGENTA_EX}{'STOCK':5} {Fore.LIGHTCYAN_EX}| {Fore.LIGHTMAGENTA_EX}{'GÉNERO':20} {Fore.LIGHTCYAN_EX} |{Style.RESET_ALL}")
    print(f"{Fore.LIGHTCYAN_EX}{'-'*76}{Style.RESET_ALL}")
    for juego in stockgeneral:
        print(f"{Fore.LIGHTMAGENTA_EX}{juego['Juego']:30} {Fore.LIGHTCYAN_EX}| {Fore.LIGHTMAGENTA_EX}{juego['Precio']:10} {Fore.LIGHTCYAN_EX}| {Fore.LIGHTMAGENTA_EX}{juego['Stock']:5} {Fore.LIGHTCYAN_EX}| {Fore.LIGHTMAGENTA_EX}{juego['Genero']:20}  {Fore.LIGHTCYAN_EX}|{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}{'-'*76}{Style.RESET_ALL}")
    input(Fore.LIGHTMAGENTA_EX + "Presione una tecla para continuar" + Style.RESET_ALL)

def modEmpleado():
    lista_empleados()
    empleado_encontrado = False
    while True:          
            Legajo = input (Fore.LIGHTCYAN_EX + "Ingrese el Nro de legajo del empleado que desea modificar: " + Style.RESET_ALL)
            if Legajo.isdigit():
                Legajo = int(Legajo)
                if obtenerLegajo(listaEmpleados, Legajo):
                    print(f'{Fore.RED} Legajo {Legajo} encontrado{Style.RESET_ALL}')
                    empleado_encontrado = True
                    input (Fore.LIGHTCYAN_EX + "Presiona una tecla para continuar" + Style.RESET_ALL)
                    break
                elif obtenerLegajo(listaAdministradores, Legajo):
                    print(f'{Fore.RED}Legajo {Legajo} encontrado {Style.RESET_ALL}')
                    empleado_encontrado = True
                    input (Fore.LIGHTCYAN_EX + "Presiona una tecla para continuar" + Style.RESET_ALL)
                    break
                else:
                     print(f'{Fore.GREEN}No existe el Legajo {Legajo}{Style.RESET_ALL}')
                     break
            else:
                print(Fore.RED + "Ingrese un N° de legajo válido" + Style.RESET_ALL)
    if empleado_encontrado == True:
        for empleado in listaEmpleados:
            if empleado["Legajo"] == int(Legajo):
                
                opcion = input(Fore.LIGHTCYAN_EX + 'Ingrese una opción: |"Nombre"||"Apellido"||"Edad"||"Sector"||"Legajo"||"Usuario"||"Clave"|: ' + Style.RESET_ALL)
                print(f"{Fore.LIGHTMAGENTA_EX}Usted seleccionó: {Fore.LIGHTCYAN_EX}{opcion}{Style.RESET_ALL}")
                if opcion == "Edad" or "Legajo":
                    while True:
                        nuevoValor = input(Fore.MAGENTA + "¿Que valor desea asignarle?" + Style.RESET_ALL)
                        if nuevoValor.isdigit():
                            int(nuevoValor)
                            if opcion == "Edad":
                                empleado["Edad"] = nuevoValor
                                print(Fore.GREEN + "Valor modificado con éxito." + Style.RESET_ALL)
                                break
                            elif opcion == "Legajo":
                                empleado["Legajo"] = nuevoValor
                                print(Fore.GREEN + "Valor modificado con éxito." + Style.RESET_ALL)
                                break
                        else:
                            print(Fore.RED + "Coloque un numero por favor" + Style.RESET_ALL)
                else:
                    if opcion == "Nombre":
                        empleado["Nombre"] = nuevoValor
                        print(Fore.GREEN + "Valor modificado con éxito." + Style.RESET_ALL)
                    elif opcion == "Apellido":
                        empleado["Apellido"] = nuevoValor
                        print(Fore.GREEN + "Valor modificado con éxito." + Style.RESET_ALL)
                    
                    elif opcion == "Sector":
                        while True:
                            if nuevoValor != "Empleado" and nuevoValor !="Administrador":
                                print (Fore.RED + "Vuelva a ingresar el sector correctamente. Empleado o Administrador" + Style.RESET_ALL)
                            else:
                                empleado["Sector"] = nuevoValor
                                print(Fore.GREEN + "Valor modificado con éxito." + Style.RESET_ALL)
                                break            
                    elif opcion == "Usuario":
                        empleado["Usuario"] = nuevoValor
                        print(Fore.GREEN + "Valor modificado con éxito." + Style.RESET_ALL)
                    elif opcion == "Clave":
                        empleado["clave"] = nuevoValor
                        print(Fore.GREEN + "Valor modificado con éxito." + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Opcion ingresada inválida" + Style.RESET_ALL)
        if not empleado_encontrado:
            print(Fore.RED + "Empleado no encontrado." + Style.RESET_ALL)
        input(Fore.LIGHTCYAN_EX + "Presione una tecla para volver al menú." + Style.RESET_ALL)

def verificar_credenciales(usuario, clave):
    usuario = usuario.lower()
    for empleado in listaEmpleados:
        if empleado["Usuario"] == usuario and empleado["clave"] == clave:
            return True, "empleado"
    for administrador in listaAdministradores:
        if administrador["Usuario"] == usuario and administrador["clave"] == clave:
            return True, "administrador"
    return False, None
              

def administracion_emp():
    acceso1 = True
    while acceso1:
        cabecera("ADMINISTRACIÓN")
        print(f"{Fore.LIGHTCYAN_EX}1. {Fore.MAGENTA}Agregar Juego{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}2. {Fore.MAGENTA}Quitar Juego{Style.RESET_ALL}")
        print(Fore.LIGHTRED_EX + "0. Salir" + Style.RESET_ALL)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cabecera("Agregar Juego")
            nuevoJuego()
        elif opcion == "2":
            cabecera("Eliminar Juego")
            elimJuegos()
        elif opcion == "0":
            acceso1 = False
            print(Fore.LIGHTRED_EX + "Saliendo..." + Style.RESET_ALL) 
        else:
            print(Fore.RED + "Opción no válida" + Style.RESET_ALL)    

def administracion_adm():
    acceso1 = True
    while acceso1:
        cabecera("ADMINISTRACIÓN")
        print(f"{Fore.LIGHTCYAN_EX}1. {Fore.MAGENTA}Agregar Juego{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}2. {Fore.MAGENTA}Quitar Juego{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}3. {Fore.MAGENTA}Agregar Empleado{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}4. {Fore.MAGENTA}Eliminar Empleado{Style.RESET_ALL}")
        print(f"{Fore.LIGHTCYAN_EX}5. {Fore.MAGENTA}Modificar empleado{Style.RESET_ALL}")
        print(Fore.RED + "0. Salir" + Style.RESET_ALL)
        opcion = input(Fore.LIGHTCYAN_EX + "Seleccione una opción: " + Style.RESET_ALL)
        if opcion == "1":
            cabecera("Agregar Juego")
            nuevoJuego()
        elif opcion == "2":
            cabecera("Eliminar Juego")
            elimJuegos(stockgeneral, "")
           
        elif opcion == "3":
            cabecera("Agregar Empleado")
            lista_empleados()
            nuevoEmpleado()
            lista_empleados()
            input(Fore.LIGHTCYAN_EX + "Presione Enter para continuar..." + Style.RESET_ALL)
        elif opcion == "4":
            cabecera("Eliminar Empleado")
            lista_empleados()
            elimEmpleado()
            print(Fore.LIGHTCYAN_EX + "Lista de Empleados actualizada:" + Style.RESET_ALL)
            lista_empleados()
            input(Fore.LIGHTCYAN_EX + "Presione Enter para continuar..." + Style.RESET_ALL)
        elif opcion == "5":
             modEmpleado()
             lista_empleados()
             input(Fore.LIGHTCYAN_EX + "Presione Enter para continuar..." + Style.RESET_ALL)
        elif opcion == "0":
            acceso1 = False
            print(Fore.LIGHTCYAN_EX + "Saliendo..." + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + "Opción no válida" + Style.RESET_ALL)     

def lista_empleados():
    print(Fore.LIGHTCYAN_EX + "\nLista de Empleados:" + Style.RESET_ALL)
    print(f"\n{Fore.LIGHTCYAN_EX}{"NOMBRE":12} | {"APELLIDO":12} | {"EDAD":5} | {"SECTOR":15} | {"LEGAJO":6} | {"USUARIO":12} | {"CONTRASEÑA":10} |{Style.RESET_ALL}")
    for empleado in listaEmpleados:
        print(f"{Fore.MAGENTA}{empleado['Nombre']:13}  {empleado['Apellido']:13}  {empleado['Edad']:6}  {empleado['Sector']:15} {empleado['Legajo']:3} {"":6} {empleado['Usuario']:13}  {empleado['clave']:10}{Style.RESET_ALL}")
    print(Fore.LIGHTCYAN_EX + "\nLista de Administradores:" + Style.RESET_ALL)
    for empleado in listaAdministradores:
        print(f"{Fore.MAGENTA}{empleado['Nombre']:13}  {empleado['Apellido']:13}  {empleado['Edad']:6}  {empleado['Sector']:15} {empleado['Legajo']:3} {"":6} {empleado['Usuario']:13}  {empleado['clave']:10}{Style.RESET_ALL}")
            

