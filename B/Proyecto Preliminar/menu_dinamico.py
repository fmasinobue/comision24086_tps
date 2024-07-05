
import os

def cabecera (leyenda):
    os.system("cls")
    print ("###############")
    print (f"{leyenda}")
    print ("###############")

continuar = True
while continuar:

    cabecera ("Menú Principal")

    print ("1. Gestión de Clientes")
    print ("2. Gestión de Proveedores")
    print ("3. Gestión de Productos")
    print ("0 Para salir")

    opcion_principal = int(input("Opción: "))

    if opcion_principal == 0:
        print (">>> Saliendo del sistema >>>")
        continuar = False

    elif opcion_principal == 1:

        cabecera ("Menú - Gestión de Clientes")

        print ()
        print ("1. Alta Nuevo Cliente")
        print ("2. Modificación de Cliente")
        print ("3. Baja de Cliente")
        opcion_menu_uno = int(input("Opción: "))
        if opcion_menu_uno  == 1:
            print ("#### Alta ####")
        elif opcion_menu_uno == 2:
            print ("#### Modificar ####")
        elif opcion_menu_uno == 3:
            print ("#### Baja ####")

    elif opcion_principal == 2:

        cabecera ("Menú - Gestión de Proveedores")

        print ()
        print ("1. Alta nuevo Proveedor")
        print ("2. Modificación de Proveedor")
        print ("3. Baja de Proveedor")
        opcion_menu_dos = int(input("Opción: "))
        if opcion_menu_dos  == 1:
            print ("#### Alta ####")
        elif opcion_menu_dos == 2:
            print ("#### Modificar ####")
        elif opcion_menu_dos == 3:
            print ("#### Baja ####")

    elif opcion_principal == 3:
        
        cabecera ("Menú - Gestión de Productos")

        print ()
        print ("1. Alta Nuevo Producto")
        print ("2. Modificación de Producto")
        print ("3. Baja de Producto")
        opcion_menu_tres = int(input("Opción: "))
        if opcion_menu_tres == 1:
            print ("#### Alta ####")
        elif opcion_menu_tres == 2:
            print ("#### Modificar ####")
        elif opcion_menu_tres == 3:
            print ("#### Baja ####")









