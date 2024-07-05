from os import system

def mostrarCabecera(titulo):
    system("cls")
    print("⭐"*25)
    print(f"⭐⭐{titulo.center(42," ")}⭐⭐")
    print("⭐"*25)

#print(mostrarCabecera(" M E N U    P R I N C I P A L "))
#print(mostrarCabecera(" I N V E N T A R I O "))
#mostrarCabecera(" B U S C A R    L I B R O S ")
#mostrarCabecera(" S O L I C I T A R    L I B R O S ")
#mostrarCabecera(" C A R R I T O   DE   C O M P R A S ")
#mostrarCabecera(" C R E D I T O S ! ! ! ")

def mostrarMenuPrincipal():   
    print("     OPCIONES:")
    print("         1 - INVENTARIO")  
    print("         2 - BUSCAR LIBROS") 
    # print("         3 - SOLICITAR LIBROS")
    # print("         4 - CARRITO DE COMPRAS")
    print("         3 - CREDITOS!!!")
    print("         0 - SALIR")
    print("⭐"*25)
    print(" ")



def mostrarMenuInventario():     
    print(" OPCIONES:")
    print("     1 - AGREGAR LIBROS")
    print("     2 - MODIFICAR LIBROS")
    print("     3 - ELIMINAR LIBROS")
    print("     0 - VOLVER AL MENÚ LIBROS")    
    print("⭐"*25)
    print(" ")


def mostrarMenuBuscar():    
    print(" OPCIONES:")
    print("     1 - BUSCAR POR TITULO")
    print("     2 - BUSCAR POR AUTOR")
    print("     3 - BUSCAR POR GÉNERO")
    print("     4 - TODOS LOS LIBROS")
    print("     0 - VOLVER AL MENÚ PRINCIPAL")    
    print("⭐"*25)
    print(" ")


def mostrarFinPrograma():    
    system("cls")
    print(" >>>>")
    print("🟪"*25) 
    print(f"🟪🟪{" F I N A L I Z A N D O    P R O G R A M A ".center(42," ")}🟪🟪")
    print("🟪"*25)
    print("         🔷  HASTA LA VISTA BABY . . .    💥🔫")
    print(" ")

