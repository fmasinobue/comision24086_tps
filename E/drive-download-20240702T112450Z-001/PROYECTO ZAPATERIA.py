import json
import os

from colorama import init,  Fore

from moduloTituloYmenu import titulo, menu, submenu, altaProducto , eliminarProducto, modificacionStock, stockTotal, infoProducto   
from accesoYvalidacion import acceso, validacionNumero
from stock import productos

d = os.path.dirname(__file__)
os.chdir(d)

archivo = open("zapateria.json" , "r")

productos= json.load(archivo)

archivo.close()

init()
titulo("  Proyecto Zapateria  ")

ingresosMax=3
intentos=0

while intentos<ingresosMax:
    usuario= input("Usuario: ")
    contraseña = input("Contraseña:")
    if usuario== "zapateria" and contraseña == "zap123":
        print ("Acceso concedido")
        accesoConcedido=True
        break
    else:
        print (Fore.LIGHTRED_EX, "Credenciales invalidas", Fore.LIGHTBLUE_EX ) 


    intentos=intentos + 1
print("")
print("")

if intentos==ingresosMax:
    accesoConcedido=False
    print("Acceso denegado")


while accesoConcedido==True:

    menu("GESTION DE PRODUCTOS")
    
    print("[1] Modificacion de stock")
    print("[2] Visualizacion del stock")
    print("[3] Créditos")
    print("[0] Salir del sistema")


    opcionPrimaria = validacionNumero ("Opcion: ")
    print()
    
    if opcionPrimaria == 0:
        accesoConcedido = False
        print("Saliendo del sistema.")

    elif opcionPrimaria == 1:
        submenu("Modificacion de Stock")
        print("[1] Agregar producto")
        print("[2] Eliminar producto")
        print("[3] Modificar producto")

        opcionSecundaria= validacionNumero ("Opcion: ")
        print()

        if opcionSecundaria == 1:
            altaProducto(productos)

        elif opcionSecundaria == 2: 
            print("Elimine el producto")
           
            eliminarProducto(productos)
            

        elif opcionSecundaria == 3:
            modificacionStock(productos)
            input("Presione Enter para continuar")
        #endif
  
    elif opcionPrimaria == 2:
        submenu("Visualizacion de Stock")
        print("[1] Ver stock total")
        print("[2] Filtrar por categoria")
        print("[3] Informacion detallada por producto")

        opcionSecundaria = validacionNumero ("Opcion: ")
        print()
        
        if opcionSecundaria == 1:
           stockTotal(productos)
           
           input("Presione Enter para continuar")
        
          
        elif opcionSecundaria == 2: 
            print("*"*30)
            print("Filtrar por categoria".center(30," "))
            print("*"*30)
            print("[1] Producto")
            print("[2] Color")
            print("[3] Talle")
            
            opcionTercera = validacionNumero("Opcion: ")

            if opcionTercera == 1:

                productoElegido = input("¿Qué producto desea buscar?: ").lower()
                productoEncontrado=False 
                for stock in productos:
                    if productoElegido.endswith('s'):
                        
                        productoElegido=productoElegido[:-1]
                        
                    if stock["tipo"].lower() == productoElegido or stock["tipo"].lower() == productoElegido+'s':
                        productoEncontrado=True
                        print(f"{stock["tipo"]}\tColor: {stock["color"]}\tTalle: {stock["talles"]}\tPrecio: {stock["precio"]}\tEn stock: {stock["stock disponible"]}")
                if productoEncontrado==False:
                    print()
                    print(Fore.LIGHTRED_EX, "Lo siento, no tenemos ese producto", Fore.LIGHTMAGENTA_EX)   
                print()
                print()
                input("Presione Enter para continuar")

            elif opcionTercera == 2:
                colorElegido = input("¿Qué color desea buscar?: ")
                colorEncontrado=False               
                for stock in productos:
                    if colorElegido == stock["color"]:
                        colorEncontrado=True
                        print(f"{stock["color"]}\tProducto: {stock["tipo"]}\tTalle: {stock["talles"]}\tPrecio: {stock["precio"]}\tEn stock: {stock["stock disponible"]}")
                
                if colorEncontrado==False:
                    print()
                    print("Lo siento, no tenemos ese color")   
                
                print()
                print()
                input("Presione Enter para continuar")

            elif opcionTercera == 3:
                talleElegido = validacionNumero("¿Qué talle desea buscar?: ")
                talleEncontrado=False
                for stock in productos:
                    if talleElegido == stock["talles"]:
                        talleEncontrado=True   
                        print(f"{stock["talles"]}\tProducto: {stock["tipo"]}\tColor: {stock["color"]}\tPrecio: {stock["precio"]}\tEn stock: {stock["stock disponible"]}")
                if talleEncontrado==False:
                    print()
                    print("Lo siento, no tenemos ese talle")         
                print()         
                print()
                input("Presione Enter para continuar")
               
            #endif
        elif opcionSecundaria == 3:
            print("Informacion del producto")
            infoProducto(productos)
            print()
            print()
            input("Presione Enter para continuar")

    elif opcionPrimaria == 3:
        menu("Creditos")
        print ("-" * 60)
        print(f"|{"Carolina Carugati".center(58," ")}|")
        print ("-" * 60)
        print(f"|{"Victoria Saenz".center(58," ")}|")
        print ("-" * 60)
        print(f"|{"Aldana Chaparro".center(58," ")}|")
        print ("-" * 60)
        print(f"|{"Mariana Fritz".center(58," ")}|")
        print("-"*60)
        input("Presione Enter para continuar")
            

        #endif
    #endif
#endwhile

print("Fin del programa")




