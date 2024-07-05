# 1.importo los modulos 
import json #para leer los datos de los productos en archivo productos.json.
import os # importa modulo referido al sistema

#import colorama

from menuyvalidacionInt import menuPrincipal, validacionInt, pausa
from abm import altaProducto, modificacionProducto, bajaProducto


d= os.path.dirname (__file__)
os.chdir(d)

archivo = open ("productos.json", "r") #abro json modo lectura
productos = json.load (archivo)
archivo.close()

#print (productos)

TOPE = 3 #veces permitidas para ingresar contraseña correcta
accesoPermitido = True # para q a la cuarta vez no pueda ingresar al sistema
intentos = 1 #contador

while intentos <= TOPE: #intentos de validacion
    intentos= intentos + 1
    print("Acceso al sistema")
    usuario = input("Usuario *admin*: ") 
    clave = input("Clave *1234*: ") 
    #usuario = "admin" # sacar cuando finalice el proyecto, lo pongo para prueba de sist para que ingrese directamente mas rapido para probarlo
    #clave = "1234"
    if usuario == "admin" and clave == "1234":
        print("Acceso Correcto")
        # intentos = TOPE + 1 si no estuviera el break porque vuelve falsa la condicion del bucle
        accesoPermitido = True
        break
    else:
        print("Validacion erronea")


while accesoPermitido:
#continuar = True # para q vuelva al menu principal
#while continuar: ya esta definido en if usuario
    menuPrincipal ("MENU PRINCIPAL")

    print("1 Gestion de Productos")
    print("2 Listado de Productos")
    print("3 Listado por Marca")
    print("4 Listado por Precio")
    print("5 Creditos")
    print("6 Salir")
    
    #opcionPrincipal = input("Opcion: ")
    #opcionPrincipal = int(opcionPrincipal)

    opcionPrincipal = validacionInt("Opcion: ") #para ingresar solo enteros
    
    if opcionPrincipal == 6:
        print("Saliendo del sistema ....")
        break
    
    elif opcionPrincipal == 1:
        menuPrincipal("Gestionar Productos",40)
        print("1 Alta de Productos")
        print("2 Modificacion de Productos")
        print("3 Baja de Productos")
        print("4 Menú Anterior")
        #opcionSec = int(input("Opcion: "))
        opcionSec = validacionInt("Opcion: ")
        if opcionSec == 1:
            productos = altaProducto (productos)

        elif opcionSec == 2:
            productos= modificacionProducto (productos)
            
        elif opcionSec == 3:
            print("##### BAJA ####")
            productos = bajaProducto (productos) 
        elif opcionSec == 4:
            print ("Volver")
                     
        #endif
    elif opcionPrincipal == 2:
        menuPrincipal("Listado de Productos")
        print ("Listado de Productos")
        #indice = 0 #para que me muestre todos los productos cargados
        #while indice < len (productos):
         #   print (productos[indice]) #imprime la lista de productos
        #  indice = indice + 1 
        for producto in productos: # es una lista de diccionarios
            print (f"Codigo: {producto ["Codigo"]}, Nombre {producto ["Nombre"]}, Marca: {producto ["Marca"]}, stock: {producto ["Cantidad"]}, Valor Unitario $: {producto ["Precio"]}")
        pausa ()
    
    elif opcionPrincipal == 3:
        menuPrincipal("Listado por Marca")
        marcaABuscar = input ("Ingrese la marca: ")
        for producto in productos: 
            if producto ["Marca"].lower () == marcaABuscar.lower ():
               print (f"Codigo: {producto ["Codigo"]} Nombre {producto ["Nombre"]}, Marca: {producto ["Marca"]}, stock: {producto ["Cantidad"]}, Valor Unitario $: {producto ["Precio"]}")    

    elif opcionPrincipal == 4:
        menuPrincipal("Listado por Precio")
        precioAbuscar = validacionInt("Ingrese el Precio a buscar: ")
        for producto in productos: # es una lista de diccionarios
            if producto ["Precio"] == precioAbuscar:
                print (f"Codigo: {producto ["Codigo"]} Nombre {producto ["Nombre"]}, Marca: {producto ["Marca"]}, stock: {producto ["Cantidad"]}, Valor Unitario $: {producto ["Precio"]}")
    
    elif opcionPrincipal == 5:
        menuPrincipal("Creditos")
        Creditos="*Estela Ferro\n*Claudio Fernández\n*Claudia Dos Santos Vázquez\n*Maximiliano Garabito,\n*Leonardo Souto\n*Luci\n*Euge"
        print (Creditos)
    
    pausa ()

print ("Fin del sistema")