import json
import os

from colorama import init, Fore

from accesoYvalidacion import validacionNumero

init()
def titulo (leyenda):
    print(Fore.LIGHTBLUE_EX, "*"*60)
    print("*"*60)
    leyenda = print(f"*{leyenda.center(58,"*")}*")
    print("*"*60)
    print("*"*60)

def menu (leyenda):
    os.system("cls")
    print (Fore.LIGHTMAGENTA_EX, "*" * 60)
    print(Fore.LIGHTYELLOW_EX, f"*{leyenda.center(58," ")}*")
    print (Fore.LIGHTMAGENTA_EX, "*"*60)

def submenu (leyenda):
    print (Fore.LIGHTMAGENTA_EX, "*"*30)
    print(f"*{leyenda.center(28," ")}*")
    print ("*"*30)

def altaProducto (alta):
    print("*"*30)
    print("Agregar producto".center(30," "))
    print("*"*30)
    while True:
        tipo = input("Producto: (s para salir) ")
        if tipo== "s":
            break
        
        codigo = validacionNumero("Codigo del Producto: ")
        color = input("Color: ")
        talles = validacionNumero("Talle: ")
        precio = validacionNumero ("Precio: ")
        stock = validacionNumero("Stock disponible: ")
        nacionalidad = input ("Nacionalidad: ")
     

        productos = {
                     "codigo":codigo,
                     "tipo":tipo,
                     "color":color,
                     "talles": talles,
                     "precio": precio,
                     "stock disponible": stock,
                     "nacionalidad":nacionalidad, 
                    }
        
        alta.append(productos)

        archivo = open("zapateria.json", "w")

        json.dump(alta, archivo, indent=4)

        archivo.close()

        return alta

def eliminarProducto (alta):

    print("*"*30)
    print("Eliminar producto".center(30, " "))
    print("*"*30)
    
    # if not alta:
    #     print("No hay productos para eliminar.")
    #     return alta
    
    while True:
        codigo_eliminar = input("Ingrese el código del producto a eliminar (s para salir): ")
        encontrado = False
        if codigo_eliminar == "s":
            break
        if codigo_eliminar.isdigit():
            codigo_eliminar = int(codigo_eliminar)

            for producto in alta:
                if producto["codigo"] == codigo_eliminar:
                    alta.remove(producto)
                    print(f"Producto con código {codigo_eliminar} eliminado correctamente.")
                    encontrado = True
                    archivo = open("zapateria.json", "w")
                    json.dump(alta, archivo, indent=4)
                    archivo.close()
                    break
        else:
            print(f"No es una opcion valida")
   
        
        
        if not encontrado:
            print(f"No se encontró ningún producto con código {codigo_eliminar}.")
    


    return alta


def modificacionStock(listado):
    print("*"*30)
    print("Modificar producto".center(30," "))
    print("*"*30)
    codigoDeseado = validacionNumero("Codigo: ")
    codigoDeseado=int(codigoDeseado)

    for articulo in listado: 
        if articulo["codigo"] == codigoDeseado:
            tipo = input(f"Nuevo producto:({articulo['tipo']}): (Enter para no cambiar) ")
            color = input(f"Nuevo color({articulo['color']}):(Enter para no cambiar) ")
            talle = validacionNumero(f"Nuevo talle({articulo['talles']}):(Enter para no cambiar) ",esperarEnter=True)
            precio = validacionNumero(f"Nuevo precio({articulo['precio']}):(Enter para no cambiar) ",esperarEnter=True)
            stock=validacionNumero(f"Nuevo stock disponible({articulo['stock disponible']}):(Enter para no cambiar) ",esperarEnter=True)
            nacionalidad= input(f"Nueva nacionalidad({articulo['nacionalidad']}):(Enter para no cambiar) ")

            if tipo != "":
                articulo["tipo"]= tipo
            if color != "":
                articulo["color"]= color
            if talle != "":
                articulo["talle"] = talle
            if precio != "":
                articulo["precio"] = precio
            if stock != "":
                articulo["stock disponible"] = stock
            if nacionalidad!="":
                articulo["nacionalidad"] = nacionalidad

            print(articulo)
            break
    archivo = open("zapateria.json", "w")

    json.dump(listado, archivo, indent=4) 

    archivo.close()

    return listado

def stockTotal(listado):
    print("*"*30)
    print("Stock total".center(30," "))
    print("*"*30)
    for stock in listado:
        if stock["stock disponible"]>0:
            print()
            print(f"Codigo: {stock["codigo"]} \tProducto: {stock["tipo"]} \tColor: {stock["color"]} \tTalle: {stock["talles"]} \tPrecio: {stock["precio"]} \tStock: {stock["stock disponible"]} \tNacionalidad: {stock["nacionalidad"]} ")
            print()
    return listado    


def infoProducto(listado):
    print("*"*30)
    print("Informacion detallada por producto".center(30," "))
    print("*"*30)
    codigoProducto = validacionNumero("Codigo: ")
    codigoProducto=int(codigoProducto)
    for stock in listado:
        if codigoProducto == stock["codigo"]:
            print()
            print(f"Codigo: {stock["codigo"]} \tProducto: {stock["tipo"]} \tColor: {stock["color"]} \tTalle: {stock["talles"]} \tPrecio: {stock["precio"]} \tStock: {stock["stock disponible"]} \tNacionalidad: {stock["nacionalidad"]} ")
            print()
    return listado   