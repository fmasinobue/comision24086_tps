from funciones import seleccionarCategoria, agregarAlCarrito, compratarjeta, buscarJuego, cabecera,  verificar_credenciales, administracion_adm, administracion_emp
from stock import stockgeneral, categoriasjuegos
from colorama import Fore, Style
inicio = True
while inicio:      
        cabecera("Bienvenido a SalaGammer!", 100)
        print(Fore.LIGHTCYAN_EX + "1.", Fore.MAGENTA + "JUEGOS" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "2.", Fore.MAGENTA + "VENTAS" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "3.", Fore.MAGENTA + "ADMINISTRACIÓN" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "0.", Fore.MAGENTA + "SALIR" + Style.RESET_ALL)
        selMenu = str(input(Fore.LIGHTRED_EX + "Elija una opcion (0 para salir): " + Style.RESET_ALL))
        if selMenu == "1":
            print()
            cabecera("JUEGOS")
            print()
            juegos=True
            while juegos:
                print(Fore.LIGHTCYAN_EX + "1.", Fore.MAGENTA + "Buscar juego" + Style.RESET_ALL )
                print(Fore.LIGHTCYAN_EX + "2.", Fore.MAGENTA + "Lista completa" + Style.RESET_ALL)
                print(Fore.RED + "0. Salir" + Style.RESET_ALL)
                print()
                opcion=input(Fore.LIGHTCYAN_EX + "Desea ver la lista completa o buscar un juego?. Ingrese la opción numerica: "+ Style.RESET_ALL)
                if opcion == "1":
                    busqueda = input(Fore.MAGENTA + "Ingresa el nombre del juego que buscas ('0' para salir): " + Style.RESET_ALL)
                    if busqueda == "0" or busqueda == "":
                        break
                    resultados = buscarJuego(stockgeneral,busqueda)
                    if resultados:
                        print(Fore.LIGHTMAGENTA_EX + "Resultados de la búsqueda: " + Style.RESET_ALL)
                        for juego in resultados:
                            print(f"{Fore.LIGHTCYAN_EX}Nombre: {juego['Juego']}  |  Genero: {juego['Genero']}  |  Precio: {juego['Precio']}  |  Stock: {juego['Stock']}{Style.RESET_ALL}")
                        input (Fore.LIGHTRED_EX + "Presiona enter para salir" + Style.RESET_ALL) 
                    else:
                        print(f"{Fore.LIGHTRED_EX}No se encontraron resultados para el término de búsqueda {Style.RESET_ALL} ({Fore.LIGHTCYAN_EX + busqueda + Style.RESET_ALL})")  
                elif opcion=="2":
                    print()
                    print(f"{Fore.LIGHTCYAN_EX}{"-"*80}{Style.RESET_ALL}")
                    print(f"{Fore.MAGENTA}{"NOMBRE":30} {Fore.LIGHTCYAN_EX}| {Fore.MAGENTA}{"PRECIO":10} {Fore.LIGHTCYAN_EX}| {Fore.MAGENTA}{"STOCK":5}{Fore.LIGHTCYAN_EX} | {Fore.MAGENTA}{"GÉNERO":24} {Fore.LIGHTCYAN_EX}|{Style.RESET_ALL}")
                    print(f"{Fore.LIGHTCYAN_EX}{"-"*80}{Style.RESET_ALL}")
                    for juego in stockgeneral:
                        print(f"{Fore.MAGENTA}{juego["Juego"]:30} {Fore.LIGHTCYAN_EX}| {Fore.LIGHTMAGENTA_EX}{juego["Precio"]:10} {Fore.LIGHTCYAN_EX}|{Fore.LIGHTMAGENTA_EX}{juego["Stock"]:5} {Fore.LIGHTCYAN_EX} | {Fore.LIGHTMAGENTA_EX}{juego["Genero"]:24} {Fore.LIGHTCYAN_EX}|{Style.RESET_ALL}")
                        print(f"{Fore.LIGHTCYAN_EX}{"-"*80}{Style.RESET_ALL}")
                    pausa1 = input(Fore.LIGHTRED_EX + "\nPresiona enter para continuar o (s) para salir: " + Style.RESET_ALL)
                    if pausa1 == "s":
                        break
                elif opcion == "0":
                    break
                else:
                    print (Fore.LIGHTRED_EX + "Opción incorrecta" + Style.RESET_ALL)
        elif selMenu == "2":
            print()
            cabecera("VENTAS")
            print()
            carrito = []
            compras=True
            while compras ==True:
                continuar = True
                print(Fore.LIGHTCYAN_EX + "1.", Fore.MAGENTA + "Buscar por juego" + Style.RESET_ALL )
                print(Fore.LIGHTCYAN_EX + "2.", Fore.MAGENTA + "Buscar por género" + Style.RESET_ALL )
                print(Fore.LIGHTRED_EX + "0. Salir" + Style.RESET_ALL)
                print()
                juego_o_genero = input (Fore.LIGHTMAGENTA_EX + "Elija una opcion: " + Style.RESET_ALL)
                while True:
                    if juego_o_genero == "1":
                        cabecera("Busqueda por Juego")
                        busqueda = input(Fore.LIGHTMAGENTA_EX + "Ingresa el nombre del juego que buscas ('s' para salir): " + Style.RESET_ALL)
                        if busqueda == "s" or busqueda =="":
                            break
                        resultados = buscarJuego(stockgeneral, busqueda)
                        juegos_disponibles = [juego for juego in stockgeneral if juego in resultados]
                        if juegos_disponibles:
                            carrito.extend(agregarAlCarrito(juegos_disponibles))
                            print(Fore.LIGHTGREEN_EX + "\nAgregado al carrito" + Style.RESET_ALL)
                            break
                        else:
                            print(Fore.LIGHTRED_EX + "El juego no se encuentra en stock." + Style.RESET_ALL)
                            input(Fore.LIGHTRED_EX + "Presione enter para salir" + Style.RESET_ALL)
                    elif juego_o_genero == "2":
                        cabecera("Busqueda por Género")
                        genero = seleccionarCategoria()
                        if genero == "0":
                            print(Fore.LIGHTCYAN_EX + "Gracias por visitarnos. ¡Hasta luego!" + Style.RESET_ALL)
                            break
                        elif genero in categoriasjuegos:
                            juegos_disponibles = [juego for juego in stockgeneral if juego["Genero"] == genero]
                            if juegos_disponibles:
                                carrito.extend(agregarAlCarrito(juegos_disponibles))
                            else:
                                print(Fore.LIGHTRED_EX + "No hay juegos disponibles en este género en este momento." + Style.RESET_ALL)
                                input(Fore.LIGHTRED_EX + "Presione enter para salir" + Style.RESET_ALL)

                        else:
                            print(Fore.LIGHTRED_EX + "Género inválido. Por favor, ingresa un género válido." + Style.RESET_ALL)
                            input(Fore.LIGHTRED_EX + "Presione enter para salir" + Style.RESET_ALL)
                        break
                    elif juego_o_genero == "0":
                        break
                    else:
                        input(Fore.LIGHTRED_EX + "Seleccion Invalida, presione una tecla" + Style.RESET_ALL)
                        break
                print(Fore.LIGHTCYAN_EX + "Resumen del carrito:" + Style.RESET_ALL)
                total = 0
                for juego, precio in carrito:
                    print(f"{Fore.LIGHTMAGENTA_EX}{juego}: ${precio}{Style.RESET_ALL}")
                    total += precio
                print(f"{Fore.LIGHTCYAN_EX}Total a pagar: {Fore.GREEN}${total}{Style.RESET_ALL}")
                if total == 0:
                   break 
                while continuar:
                    salir = 0
                    continuar1 = input(Fore.LIGHTMAGENTA_EX + "¿Desea agregar otro juego al carrito? (s/n): " + Style.RESET_ALL)
                    if continuar1.lower() != "s" and continuar1.lower() != "n":
                        print(Fore.LIGHTRED_EX + "Opcion Incorrecta. Ingresa s/n" + Style.RESET_ALL)
                        continuar = True
                    elif continuar1.lower() == "n":
                        compratarjeta()
                        compras = False
                        carrito=[]
                        input (Fore.LIGHTRED_EX + "Presione enter para salir" + Style.RESET_ALL)
                        break
                    elif continuar1.lower() == "s":
                        continuar == False
                        break
        elif selMenu == "3":
            ingreso=True
            while ingreso:
                usuario = input(Fore.LIGHTCYAN_EX + "Ingrese su Usuario de Administrador: " + Style.RESET_ALL)
                clave = input(Fore.LIGHTCYAN_EX + "Ingrese su clave (Solo admite números): " + Style.RESET_ALL)
                acceso, tipo_usuario = verificar_credenciales(usuario, clave)
                if acceso:
                    print(Fore.LIGHTGREEN_EX + "Inicio de sesión exitoso como", Fore.MAGENTA + tipo_usuario + Style.RESET_ALL)
                    if tipo_usuario == "empleado":
                        administracion_emp()
                        break
                    elif tipo_usuario == "administrador":
                        administracion_adm()
                        break
                else:
                    print (Fore.LIGHTRED_EX + "Acceso no autorizado" + Style.RESET_ALL)                              
        elif selMenu == "0":
            break
        else:
            print(Fore.LIGHTRED_EX + "Opcion ingresada no admitida (1.JUEGOS, 2.BUSCAR, 3.ADMINISTRACIÖN, 0.SALIR)" + Style.RESET_ALL)

