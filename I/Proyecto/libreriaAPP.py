import os #os.system("cls") escribe cls en consola automaticamente y la limpia
import json

from misModulos import validarSiNumero, agregar, buscarNombre, buscarAutor, eliminar_libro, editar_libro, buscarGenero, tablaDeLibros, login
from decoraciones import mostrarCabecera, mostrarFinPrograma
from decoraciones import mostrarMenuPrincipal, mostrarMenuInventario
from decoraciones import mostrarMenuBuscar

d = os.path.dirname(__file__) #almacena la direccion de la carpeta en una variable
os.chdir(d)                   #cambia la direccion de trabajo por la de la variable d
try:
    arch = open("libros.json","r") #abre en forma de lectura el json
    libros = json.load(arch)       #almnacena el json en una variable
    arch.close()                   #cierra el json
except:
    libros = []
    
accesoPermitido = False
accesoPermitido = login() #funcion para logear



while accesoPermitido:
    mostrarCabecera(" M E N U    P R I N C I P A L ")
    mostrarMenuPrincipal()
    opcionMenuPrincipal = validarSiNumero(" Seleccione una Opción :  ")
    if opcionMenuPrincipal == 0:
        mostrarFinPrograma()
        break #while 
    elif opcionMenuPrincipal == 1:
        mostrarCabecera(" I N V E N T A R I O ")
        mostrarMenuInventario()
        opcionMenuInventario = validarSiNumero(" Seleccione una Opción :  ")
        
        if opcionMenuInventario == 1:
            mostrarCabecera(" A G R E G A R    L I B R O ")
            agregar(libros)
            input("     Enter para continuar")
        elif opcionMenuInventario == 2:
            mostrarCabecera(" M O D I F I C A R    L I B R O ")
            libros = editar_libro(titulo=input("Ingrese el titulo del libro: "))
            input("     Enter para continuar")
        elif opcionMenuInventario == 3:
            mostrarCabecera(" E L I M I N A R    L I B R O ")
            libros = eliminar_libro(titulo=input("Ingrese el titulo del libro a eliminar: "))
            input("     Enter para continuar")
        elif opcionMenuInventario == 0:
            print() #no hace falta codigo para volver al menu principal
        else:
            print(" OPCIÓN INCORRECTA... VOLVAMOS A EMPEZAR.")
            input("     Enter para continuar")
        #endif
            
    elif opcionMenuPrincipal == 2:
        mostrarCabecera(" B U S C A R    L I B R O S ")
        mostrarMenuBuscar()
        opcionMenuBuscar = validarSiNumero("    Seleccione una Opción :  ")
        
        if opcionMenuBuscar == 1:
            mostrarCabecera(" B U S C A R    P O R    T I T U L O ")
            buscarNombre(libros)
            input("     Enter para continuar")
        elif opcionMenuBuscar == 2:
            mostrarCabecera(" B U S C A R    P O R    A U T O R ")
            buscarAutor(libros)
            input("     Enter para continuar")
        elif opcionMenuBuscar == 3:
            mostrarCabecera(" B U S C A R    P O R    G É N E R O ")
            buscarGenero(libros)
            input("     Enter para continuar")
        elif opcionMenuBuscar == 4:
            mostrarCabecera(" T O D O S   L O S   L I B R O S ")
            tablaDeLibros(libros)
            input("     Enter para continuar")
        elif opcionMenuBuscar == 0:
            print() #no hace falta codigo para volver al menu principal
        else:
            print(" OPCIÓN INCORRECTA... VOLVAMOS A EMPEZAR.")
            input("     Enter para continuar")
        #endif
                
    # elif opcionMenuPrincipal == 3:
    #     mostrarCabecera(" S O L I C I T A R    L I B R O S ")
    #     #falta codigo
    #     input("     Enter para continuar")
        
    # elif opcionMenuPrincipal == 4:
    #     mostrarCabecera(" C A R R I T O   DE   C O M P R A S ")
    #     #falta codigo
    #     input("     Enter para continuar")  
          
    elif opcionMenuPrincipal == 3:
        mostrarCabecera(" C R E D I T O S ! ! ! ")
        print("VALENTINA GUILLÉN")
        print("ELIZABETH GIRIBALDI JATIP")
        print("KEVIN EMERSON LAIME HUANCA")
        print("SERGIO SEGADE")
        print("FERNANDO SEBASTIAN GOMEZ")
        print("HWA SUNG KIM")
        input("     Enter para continuar")
        
    else:
        print(" OPCIÓN INCORRECTA... VOLVAMOS A EMPEZAR.")
        input("     Enter para continuar")
        
print("fin")


