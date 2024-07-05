
import os
import time
from modulo_dos import productos
from modulo_tres import alta_producto, cabecera, cabecera_emoji, validacion_menu, modificacion_producto, baja_producto, pausa 
#Area de inicialización de variables
acceso_al_sistema = False #Permite el acceso al bucle while del programa luego del lugueo
intentos = 0 #Tag de contador de intentos
volver_flag = False #Bandera para volver al submenú en el que se estaba trabajando y evitar volver siempre al principal
codigo_tab = "Código" #Se crea una variable str para facilitar el tabulado de la lista de productos
producto_tab = "Producto" #Se crea una variable str para facilitar el tabulado de la lista de productos
descripcion_tab = "Descripción" #Se crea una variable str para facilitar el tabulado de la lista de productos
cantidad_tab = "Cantidad" #Se crea una variable str para facilitar el tabulado de la lista de productos
codigo_test = int(25)
while intentos < 3:
    intentos = intentos + 1
    cabecera_emoji("FerreMaster - Login", 20,"🔑")
    if intentos > 1:
        print ("Usuario o Clave incorrecta") #En caso usuario y clave incorrecta imprime un aviso
        usuario = input ("Usuario: ")
        clave = input ("Clave: ")
    else:
        usuario = input ("Usuario: ") #Primer intento de logueo
        clave = input ("Clave: ")
        
    if usuario == "f" and clave == "1":
        intentos = 4 
        acceso_al_sistema = True
    else: 
        print ("<<Cierre del sistema por demasiados intentos fallidos>>")

while acceso_al_sistema: #Programa
    if volver_flag == False: #Menú principal del programa
        cabecera("Menú Principal")
    
        print ()
        print ("1. Gestión de Clientes")
        print ("2. Gestión de Proveedores")
        print ("3. Gestión de Productos")
        print ("0. Para salir")

        #opcion_principal = int(input("Opción: ")) #Ingreso de selección del menú principal

        opcion_principal = validacion_menu("Opción: ",3)

    else:
        volver_flag = False                        #En caso de que exixtan más submenús esta bandera y el tag "opción_principal volver"
        opcion_principal = opcion_principal_volver #devuelven al usuario un nivel arriba o en el nivel donde estaban cuando terminar una operación
        
    if opcion_principal == 0: #Salida del sistema
        print ("<<< Saliendo del sistema >>>")
        acceso_al_sistema = False
    elif opcion_principal == 1: #Acceso al menú de gestión de clientes desde el menú principal
        cabecera("Menú - Gestión de Clientes")
        print ()
        print ("1. Alta Nuevo Cliente")
        print ("2. Modificación de Cliente")
        print ("3. Baja de Cliente")
        print ("0. Volver")
        opcion_menu_uno = validacion_menu("Opción: ",3)
        #opcion_menu_uno = int(input("Opción: ")) #Submenú gestión de clientes
        if opcion_menu_uno  == 1: #Acceso a alta de nuevo cliente
            print ("#### Alta ####")
        elif opcion_menu_uno == 2: #Acceso modificación de cliente
            print ("#### Modificar ####")
        elif opcion_menu_uno == 3: #Acceso baja ded cliente
            print ("#### Baja ####")

    elif opcion_principal == 2: #Acceso al menú de gestión de proveedores desde el menú principal
        cabecera("Menú - Gestión de Proveedores")
        print ()
        print ("1. Alta nuevo Proveedor")
        print ("2. Modificación de Proveedor")
        print ("3. Baja de Proveedor")
        print ("0. Volver")
        opcion_menu_dos = validacion_menu("Opción: ",3)
        #opcion_menu_dos = int(input("Opción: ")) #Submenú gestión de proveedores
        if opcion_menu_dos  == 1: #Acceso a alta de nuevo proveedor
            print ("#### Alta ####")
        elif opcion_menu_dos == 2: #Acceso a modificación de proveedor
            print ("#### Modificar ####")
        elif opcion_menu_dos == 3: #Acceso a baja de proveedor
            print ("#### Baja ####")

    elif opcion_principal == 3: #Acceso al menú de gestión de productos desde el menú principal
        cabecera("Menú - Gestión de Productos")
        print ()
        print ("1. Alta Nuevo Producto")
        print ("2. Modificación de Producto")
        print ("3. Baja de Producto")
        print ("4. Listado")
        print ("5. Buscar")
        print ("0. Volver")
        #opcion_menu_tres = int(input("Opción: ")) #Submenú gestión de productos
        opcion_menu_tres = validacion_menu("Opción: ",5)
        if opcion_menu_tres == 1: #Acceso a alta de nuevo producto
            productos = alta_producto(productos)
            volver_flag = True
            opcion_principal_volver = 3

        elif opcion_menu_tres == 2: #Acceso a modificación de producto
            productos = modificacion_producto(productos)
            volver_flag = True
            opcion_principal_volver = 3
            
        elif opcion_menu_tres == 3: #Acceso a baja de producto
            productos = baja_producto(productos)
            volver_flag = True
            opcion_principal_volver = 3

        elif opcion_menu_tres == 4: #Acceso a listado de productos
             cabecera("Listado Productos",140)
             print(f'{codigo_tab.ljust(10," ")}\t{producto_tab.ljust(25," ")}\t{descripcion_tab.title().ljust(60," ")}\t{cantidad_tab}')
             for producto in productos: # [{},{},{}, []]
                 print(f'{str(producto["Código"]).ljust(10," ")}\t{producto["Producto"].upper().ljust(25," ")}\t{producto["Descripción"].title().ljust(60," ")}\t{producto["Cantidad"]}')
             input("Presiona enter para continuar ...")
             volver_flag = True
             opcion_principal_volver = 3

        elif opcion_menu_tres == 5: #Buscar producto
            criterio = input("Producto a buscar: ")
            cabecera(f"Listado de: {criterio}", 140)
            print(f'{codigo_tab.ljust(10," ")}\t{producto_tab.ljust(25," ")}\t{descripcion_tab.title().ljust(60," ")}\t{cantidad_tab}')
    
            for producto in productos:
                if criterio.lower() == producto["Producto"].lower():
                    print(f'{str(producto["Código"]).ljust(10," ")}\t{producto["Producto"].upper().ljust(25," ")}\t{producto["Descripción"].title().ljust(60," ")}\t{producto["Cantidad"]}')
    
            pausa()
            volver_flag = True
            opcion_principal_volver = 3

        elif opcion_menu_tres == 0:
             volver_flag = False