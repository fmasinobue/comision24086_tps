import os
import json
from datetime import datetime

# from datos import *

d = os.path.dirname(__file__)
os.chdir(d)

datos_usuarios = open("datos_usuarios.json", "r")
base_de_datos_usuarios = json.load(datos_usuarios)
datos_usuarios.close()

datos_productos = open("datos_productos.json", "r")
listaDeProductos = json.load(datos_productos)
datos_productos.close()

#funciones para imprimir
def imprimirProducto(producto):
  print(f"{producto["articulo"]}".ljust(25, " "), f"{producto["categoria"]}".ljust(25, " "), f"{producto["precio"]}".ljust(25, " "), f"{producto["stock"]}")

def menuPrincipal(titulo):
  print("-"*50 + "\n|" + f"{titulo.center(48, " ")}" + "|\n" + "-"*50 )

def subMenu(titulo):
  print("-"*35 + "\n|" + f"{titulo.center(33, " ")}" + "|\n" + "-"*35 )

#funciones de login
def registro_usuario(usuarios):
    nuevo_usuario = input("Registre un nombre de usuario: ")
    while nuevo_usuario in usuarios:
        print("El nombre de usuario ya existe. Por favor, elija otro.")
        nuevo_usuario = input("Ingrese un nombre de usuario: ")
        
    contraseña_valida = False
    while not contraseña_valida:
        nueva_contraseña = input("Ingrese una contraseña con al menos 8 caracteres, una mayúscula y al menos un numero: ")
        if len(nueva_contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
        elif not any(c.isupper() for c in nueva_contraseña):
            print("La contraseña debe contener al menos una letra mayúscula.")
        elif not any(c in "123456789" for c in nueva_contraseña):
            print("La contraseña debe contener al menos un numero")
        else:
            contraseña_valida = True

    usuarios[nuevo_usuario] = nueva_contraseña
    datos_usuarios = open("datos_usuarios.json", "w")
    json.dump(usuarios, datos_usuarios, indent=4, sort_keys=True)
    datos_usuarios.close()
    print("¡Registro exitoso! Ahora puedes iniciar sesión.")
    login_usuario(usuarios)

def login_usuario(usuarios):
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    while usuario not in usuarios or usuarios[usuario] != contraseña:
        print("Nombre de usuario o contraseña incorrectos. Inténtelo de nuevo.")
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

    os.system("cls")
    print("¡Inicio de sesión exitoso! Bienvenido,", usuario)

#funciones de stock
def verStock():
  print("")
  print("STOCK TOTAL".center(50, "-"))
  print("")
  for producto in listaDeProductos:
    print(f"{producto["articulo"]}: {producto["stock"]}")
  print("".center(50, "-"))
  input("Presione ENTER para continuar...")
  os.system("cls")

def filtrar():
  print("")
  print("CATEGORIAS".center(50, "-"))
  print("")
  print("1 Hardware")
  print("2 Periféricos")
  print("3 Accesorios")
  print("4 Gaming")
  print("")
  categoria = validacionInt(input("Seleccione una opción: "))

  if categoria == 1:
    print("")
    print("ARTICULO".ljust(25, " "), "CATEGORIA".ljust(25, " "), "PRECIO".ljust(25, " "), "STOCK")
    for producto in listaDeProductos:
      if producto["categoria"] == "Hardware":
        imprimirProducto(producto)
    print("")
    input("Presione ENTER para continuar...")
    os.system("cls")

  elif categoria == 2:
    print("")
    print("ARTICULO".ljust(25, " "), "CATEGORIA".ljust(25, " "), "PRECIO".ljust(25, " "), "STOCK")
    for producto in listaDeProductos:
      if producto["categoria"] == "Perifericos":
        imprimirProducto(producto)
    print("")
    input("Presione ENTER para continuar...")
    os.system("cls")

  elif categoria == 3:
    print("")
    print("ARTICULO".ljust(25, " "), "CATEGORIA".ljust(25, " "), "PRECIO".ljust(25, " "), "STOCK")
    for producto in listaDeProductos:
      if producto["categoria"] == "Accesorios":
        imprimirProducto(producto)
    print("")
    input("Presione ENTER para continuar...")
    os.system("cls")

  elif categoria == 4:
    print("")
    print("ARTICULO".ljust(25, " "), "CATEGORIA".ljust(25, " "), "PRECIO".ljust(25, " "), "STOCK")
    for producto in listaDeProductos:
      if producto["categoria"] == "Gaming":
        imprimirProducto(producto)
    print("")
    input("Presione ENTER para continuar...")
    os.system("cls")

  else:
    os.system("cls")
    print(f"\nEntrada inválida, por favor seleccione una de las opciones\n")
    filtrar()

def detalles():

  detalles = True
  while detalles:
    print("")
    print("LISTA DE PRODUCTOS".center(50, "-"))
    print("")

    for producto in listaDeProductos:
      print(f"{listaDeProductos.index(producto) + 1} {f"{producto["articulo"]}"}")

    print("")
    seleccionDetalle = validacionInt(input("Seleccione el producto: "))

    if seleccionDetalle > len(listaDeProductos):  
      os.system("cls")
      print(f"\nEntrada inválida, por favor seleccione una de las opciones\n")
    else:
      for producto in listaDeProductos:
        if seleccionDetalle == listaDeProductos.index(producto) + 1:
          print(f"{producto["articulo"]}: {producto["descripcion"]}")
          detalles = False
          print("")
          input("Presione ENTER para continuar...")
          os.system("cls")

# funcion de validacion
def validacionInt(entrada):
  while True:
    
    try:
      entrada = int(entrada)
      break
    except:
      print("")
      print("Ingrese solo números")
      print("")

  return entrada

# Función para mostrar la lista de productos
def mostrar_productos(lista_productos):
    print("PRODUCTOS DISPONIBLES".center(50, "-"), "\n")
    for i, producto in enumerate(lista_productos, start=1):
        print(f"{i}. {producto['articulo']} - Precio: ${producto['precio']} - Stock: {producto['stock']}")
        
# Función para realizar la compra
def comprar_producto(lista_productos, indice_producto, cantidad):
    producto = lista_productos[indice_producto]
    if producto['stock'] >= cantidad:
        producto['stock'] -= cantidad
        return True
    else:
        print("Lo sentimos, no hay suficiente stock disponible.")
        return False

# Función para generar la boleta
def generar_boleta(carrito, medio_pago, cuotas_info=None):
    total = 0
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n--- Boleta ---")
    print(f"Fecha: {fecha_actual}")
    print(f"Medio de pago: {medio_pago}")
    if cuotas_info:
        print(f"Cuotas: {cuotas_info['cuotas']} - Interés: {cuotas_info['interes']}%")
    print("\n")
    
    for item in carrito:
        subtotal = item['precio'] * item['cantidad']
        iva = subtotal * 0.21
        total_producto = subtotal + iva
        print(f"Producto: {item['articulo']}")
        print(f"Cantidad: {item['cantidad']}")
        print(f"Precio unitario: ${item['precio']}")
        print(f"Subtotal: ${subtotal}")
        print(f"IVA (21%): ${iva}")
        print(f"Total producto: ${total_producto}\n")
        total += total_producto

    if cuotas_info:
        intereses = total * (cuotas_info['interes'] / 100)
        total += intereses
        print(f"Intereses por cuotas: ${intereses}")

    print(f"Total a pagar (incluido IVA y/o intereses): ${total}")
    print("¡ Gracias por su compra !")

#Gestión de Productos
#Ingreso de Categoría del producto en agregar_producto()
def lista_categoria():
  listaCategoria = {
    1: "Hardware",
    2: "Periféricos",
    3: "Accesorios",
    4: "Gaming"
  }
  print(listaCategoria)
  seleccion = validacionInt(input("Ingrese el número correspondiente a la categoría del producto (1 - 4): "))
  
  while seleccion not in listaCategoria:
    print("Entrada inválida, por favor seleccione una de las opciones")
    seleccion = validacionInt(input("Ingrese el número correspondiente a la categoría del producto (1 - 4): "))
  return listaCategoria[seleccion]

#Función Agregar Producto
def agregar_producto():
  
  while True:
    print("")
    print("AGREGAR PRODUCTO".center(50, "-"))
    print("")

    print("COMPLETE LOS CAMPOS SOLICITADOS.".center(50))
    print("")

    nombreProducto = input("Ingrese el nombre del Producto: ")
    
    categoriaProducto  = lista_categoria()

    descripcionProducto = input("Ingrese la descripción del producto: ")

    precioProducto = float(input("Ingrese el precio del producto: "))

    stockProducto = validacionInt(input("Ingrese la cantidad de stock del producto: "))

    productoNuevo = {
      "articulo": nombreProducto,
      "categoria": categoriaProducto,
      "descripcion": descripcionProducto,
      "precio": precioProducto,
      "stock": stockProducto
    }
    
    print("")                                         
    print(f"{productoNuevo}, agregado correctamente.")
    print("")

    listaDeProductos.append(productoNuevo)
    datos_productos = open("datos_productos.json", "w")
    json.dump(listaDeProductos, datos_productos, indent=4, sort_keys=True)
    datos_productos.close()

    continuar = input("¿Desea agregar otro producto? (si - no): ").strip().lower()
    if continuar == "si":
      os.system("cls")
      continue
    elif continuar == "no":
      os.system("cls")
      break

#Opciones luego de Agregar el Producto:
  ver_stock = input("¿Desea ver el Stock total? (si - no): ").strip().lower()

  if ver_stock == "si":
    verStock()
  elif ver_stock == False:
    print("Seleccione una opción válida.")
    ver_stock()
  else:
    os.system("cls")
    
  ver_filtrar = input("¿Desea ver los productos filtrados por categoría? (si - no): ").strip().lower()

  if ver_filtrar == "si":
    filtrar()
  elif ver_filtrar == False:
    print("Seleccione una opción válida.")
    ver_filtrar()
  else:
    os.system("cls")

  ver_detalles = input("¿Desea ver los DETALLES de los productos? (si - no): ").strip().lower()

  if ver_detalles == "si":
    detalles()
  elif ver_detalles == False:
    print("Seleccione una opción válida.")
    ver_detalles()
  else:
    os.system("cls")

def eliminarProducto():
  while True:
    print("")
    print("LISTA DE PRODUCTOS".center(50, "-"))
    print("")

    for producto in listaDeProductos:
      print(f"{listaDeProductos.index(producto) + 1} {f"{producto["articulo"]}"}")

    print("")
    seleccionEliminar = validacionInt(input("Seleccione el producto: "))

    if seleccionEliminar > len(listaDeProductos):  
      os.system("cls")
      print(f"\nEntrada inválida, por favor seleccione una de las opciones\n")
      continue
    else:
      for producto in listaDeProductos:
        if seleccionEliminar == listaDeProductos.index(producto) + 1:
          del listaDeProductos[seleccionEliminar - 1]
          datos_productos = open("datos_productos.json", "w")
          json.dump(listaDeProductos, datos_productos, indent=4, sort_keys=True)
          datos_productos.close()
          input("Presione ENTER para continuar...")
          os.system("cls")
          break
    
    continuar = input("¿Desea eliminar otro producto? (si - no): ").strip().lower()
    if continuar == "si":
      os.system("cls")
      continue
    elif continuar == "no":
      os.system("cls")
      break

def modificarProducto():
  while True:
    print("")
    print("LISTA DE PRODUCTOS".center(50, "-"))
    print("")

    for producto in listaDeProductos:
      print(f"{listaDeProductos.index(producto) + 1} {f"{producto["articulo"]}"}")

    print("")
    seleccionModificar = validacionInt(input("Seleccione el producto: "))

    if seleccionModificar > len(listaDeProductos):
      os.system("cls")
      print(f"\nEntrada inválida, por favor seleccione una de las opciones\n")
      continue
    else:
      for producto in listaDeProductos:
        if seleccionModificar == listaDeProductos.index(producto) + 1:
          while True:
            print("")
            print("1 Nombre del articulo")
            print("2 Categoria")
            print("3 Descripcion")
            print("4 Precio")
            print("5 Stock")
            print("")
            seleccionDato = validacionInt(input("Que dato desea modificar?: "))

            if seleccionDato == 1:
              listaDeProductos[(seleccionModificar - 1)]["articulo"] = input("Ingrese el nuevo nombre del articulo: ")
            elif seleccionDato == 2:
              listaDeProductos[(seleccionModificar - 1)]["categoria"] = lista_categoria()
            elif seleccionDato == 3:
              listaDeProductos[(seleccionModificar - 1)]["descripcion"] = input("Ingrese la nueva descripcion del articulo: ")
            elif seleccionDato == 4:
              listaDeProductos[(seleccionModificar - 1)]["precio"] = validacionInt(input("Ingrese el nuevo precio del articulo: "))
            elif seleccionDato == 5:
              listaDeProductos[seleccionModificar - 1]["stock"] = validacionInt(input("Ingrese el nuevo stock del articulo: "))
            else:
              os.system("cls")
              print("Entrada invalida, por favor seleccione una de las opciones")
              continue

            datos_productos = open("datos_productos.json", "w")
            json.dump(listaDeProductos, datos_productos, indent=4, sort_keys=True)
            datos_productos.close()
            break

    continuar = input("¿Desea modificar otro producto? (si - no): ").strip().lower()
    if continuar == "si":
      os.system("cls")
      continue
    elif continuar == "no":
      os.system("cls")
      break
