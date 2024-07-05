import os
import json

# from datos import *
from funciones import *

d = os.path.dirname(__file__)
os.chdir(d)

letrero = """
  ____     ___  ___  _____   _    _    ____    _   _
 |  _ \    | |  | | |_   _| | |  | |  / __ \  | \ | |
 | |_) |   \ \__/ /   | |   | |__| | | |  | | |  \| |
 |  __/     \    /    | |   |  __  | | |__| | | |\  |
 |_|         |__|     |_|   |_|  |_|  \____/  |_| \_|
 
     ______     _____       ______       _    _
    |_    _|   | ____|     /  ____|     | |  | |
      |  |     | |_       |   |         | |__| |
      |  |     | __|__    |   |___      |  __  |
      |__|     |______|    \______|     |_|  |_|                    
"""

print(letrero)

print("Bienvenido a Python Tech\n")

datos_usuarios = open("datos_usuarios.json", "r")
base_de_datos_usuarios = json.load(datos_usuarios)
datos_usuarios.close()

datos_productos = open("datos_productos.json", "r")
listaDeProductos = json.load(datos_productos)
datos_productos.close()

tiene_cuenta = input("¿Ya tienes una cuenta? (si/no): ")

while tiene_cuenta.lower() not in ["si", "no"]:
    print("Por favor, responda 'si' o 'no'.")
    tiene_cuenta = input("¿Ya tienes una cuenta? (si/no): ")

if tiene_cuenta.lower() == "si":
    login_usuario(base_de_datos_usuarios)
elif tiene_cuenta.lower() == "no":
    registro_usuario(base_de_datos_usuarios) 

menu = True

while menu:
  print("")
  menuPrincipal("MENU PRINCIPAL")
  print("")
  print ("1 Gestión de productos")
  print ("2 Visualización de stock")
  print ("3 Generar pedido")
  print("0 Salir")

  print("")
  seleccionMenu = validacionInt(input("Seleccione una opción: "))
  print("")

  if seleccionMenu == 0:
    print("Gracias por usar Python Tech")
    print("")
    input("Presione ENTER para salir...")
    menu = False
  elif seleccionMenu == 1:
    #Menu de gestion de productos
    os.system("cls")
    gestion = True
    while gestion:
      print("")
      subMenu("GESTION DE PRODUCTOS")
      print("")
      print ("1 Agregar producto")
      print ("2 Eliminar producto")
      print ("3 Modificar producto")
      print ("0 Volver")

      print("")
      seleccionGestion = validacionInt(input("Seleccione una opción: "))
      print("")

      if seleccionGestion == 0:
        os.system("cls")
        gestion = False
      elif seleccionGestion == 1:
        os.system("cls")
        agregar_producto()
      elif seleccionGestion == 2:
        os.system("cls")
        eliminarProducto()
      elif seleccionGestion == 3:
        os.system("cls")
        modificarProducto()
      else:
        os.system("cls")
        print("Opción invalida")
  elif seleccionMenu == 2:
    #Menu de visualizacion de stock
    os.system("cls")
    visualizar = True
    while visualizar:
      print("")
      subMenu("VISUALIZACION DE STOCK")
      print("")
      print ("1 Ver stock total")
      print ("2 Filtrar por categoria")
      print ("3 Información detallada")
      print ("0 Volver")

      print("")
      seleccionStock = validacionInt(input("Seleccione una opción: "))
      print("")

      if seleccionStock == 0:
        os.system("cls")
        visualizar = False
      elif seleccionStock == 1:
        os.system("cls")
        verStock()
      elif seleccionStock == 2:
        os.system("cls")
        filtrar()
      elif seleccionStock == 3:
        os.system("cls")
        detalles()
      else:
        os.system("cls")
        print("Opción invalida")
  elif seleccionMenu == 3:
        carrito = []
        os.system("cls")
        # Proceso de compra
        while True:
            mostrar_productos(listaDeProductos)
            indice = validacionInt(input("\nIngrese el número del producto que desea agregar al carrito (0 para finalizar): "))
            if indice == 0:
                break
            indice -= 1
            cantidad = validacionInt(input("Ingrese la cantidad que desea comprar: "))
            if comprar_producto(listaDeProductos, indice, cantidad):
                carrito.append({'articulo': listaDeProductos[indice]['articulo'], 'precio': listaDeProductos[indice]['precio'], 'cantidad': cantidad})
                listaDeProductos[indice]["stock"] - cantidad

                datos_productos = open("datos_productos.json", "w")
                json.dump(listaDeProductos, datos_productos, indent=4, sort_keys=True)
                datos_productos.close()

                print("¡Producto añadido al carrito!")
            continuar = input("¿Desea agregar más productos al carrito? (s/n): ")
            os.system("cls")
            print("TU CARRITO".center(50, "-"))
            print("")
            for producto in carrito:
              print(f"Artículo: {producto['articulo']}", f" Precio: ${producto['precio']}", f"Cantidad: {producto['cantidad']}")
            print("")
            if continuar.lower() == 'n':
                break

        # Selección del medio de pago
        print("\nSeleccione el medio de pago:")
        medios_de_pago = ["Efectivo", "Tarjeta de débito", "Tarjeta de crédito", "Transferencia bancaria"]
        for i, medio in enumerate(medios_de_pago, start=1):
            print(f"{i}. {medio}")
        medio_pago_indice = validacionInt(input("Ingrese el número del medio de pago: ")) - 1
        medio_pago = medios_de_pago[medio_pago_indice]

        # Si se selecciona tarjeta de crédito, elegir opciones de cuotas
        cuotas_info = None
        if medio_pago == "Tarjeta de crédito":
            print("\nSeleccione la opción de cuotas:")
            opciones_cuotas = [
                {"opcion": "3 cuotas y 10% de interés", "cuotas": 3, "interes": 10},
                {"opcion": "6 cuotas y 25% de interés", "cuotas": 6, "interes": 25}
            ]
            for i, opcion in enumerate(opciones_cuotas, start=1):
                print(f"{i}. {opcion['opcion']}")
            cuotas_indice = validacionInt(input("Ingrese el número de la opción de cuotas: ")) - 1
            cuotas_info = opciones_cuotas[cuotas_indice]

        # Generar boleta
        os.system("cls")
        generar_boleta(carrito, medio_pago, cuotas_info)
        input("\nPresione ENTER para continuar...")
        os.system("cls")
  else:
    os.system("cls")
    print("Opción inválida")