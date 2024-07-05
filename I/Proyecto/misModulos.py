import os
import json
from decoraciones import mostrarCabecera, mostrarFinPrograma
from decoraciones import mostrarMenuPrincipal, mostrarMenuInventario
from decoraciones import mostrarMenuBuscar

def validarSiNumero(entrada):
    continuar = True
    while continuar:
        numero = input(entrada)
        if numero.isdigit():
            continuar = False
        else:
            print(f" Diculpas; solo admito números ({numero}) 🤷‍♂️")
    numero = int(numero)
    return numero

def login():
    mostrarCabecera(" B I E N V E N I D O ! ! ")
    return True
    Tope = 3
    intentos = 1
    while intentos <= 3:
        print()
        usuario = input("Ingrese usuario: ")
        print()
        contraseña = input("Ingrese su contraseña :")
        print()
        if usuario == "admin" and contraseña == "1234":
            return True
        else:
            os.system("cls")
            mostrarCabecera(" B I E N V E N I D O ! ! ")
            print("Usuario o Contraseña INCORRECTOS ! ! ! ")
            intentos = intentos + 1
        if intentos == 4:
            print("Exeso de intentos, cerrando programa")
            return False




def agregar(variable):
    dicc = {}
    while True:
        dicc["titulo"] = input("ingrese el titulo del nuevo libro (vacio para cancelar): ").capitalize()
        if dicc["titulo"] == "":
            return(variable)
        for libro in variable:
            if dicc["titulo"].lower() == libro["titulo"].lower():
                print("el titulo ya existe")
                repetido = True
                break #for
            else:
                repetido = False
        if repetido == False:
            break #while
    dicc["autor"] = input("ingrese el autor del nuevo libro: ").capitalize()
    dicc["genero"] = input("ingrese el genero del nuevo libro: ")
    dicc["precio"] = validarSiNumero("ingrese el precio del nuevo libro: ")
    dicc["cantidad"] = validarSiNumero("ingrese el cantidad de libros: ")
    variable.append(dicc)
    arch = open("libros.json", "w")
    json.dump(variable, arch, indent=4)
    arch.close()


def buscarNombre(variable):
    buscar = input("ingrese el nombre del libro a buscar: ")
    for libro in variable:
        if buscar.lower() == libro["titulo"].lower():
           print(f"Titulo: {libro["titulo"]} ")
           print(f"autor: {libro["autor"]}")
           print(f"genero: {libro["genero"]}")
           print(f"precio: ${libro["precio"]}")
           print(f"cantidad: {libro["cantidad"]}")
           break
    else:
        print ("No contamos con ese libro")    

    
def buscarAutor(variable):
    buscar = input ("Ingrese el autor a buscar: ")
    encontrado = False
    for libro in variable:
        if buscar.lower() in libro["autor"].lower():
           print(f"Titulo: {libro["titulo"]} ")
           print(f"autor: {libro["autor"]}")
           print(f"genero: {libro["genero"]}")
           print(f"precio: ${libro["precio"]}")
           print(f"cantidad: {libro["cantidad"]}")
           encontrado = True
    if encontrado == False:
        print ("No contamos con títulos del autor ingresado")    

def buscarGenero(variable):
    buscar = input ("Ingrese el género a buscar: ")
    encontrado = False
    print()
    for libro in variable:
        if buscar.lower() in libro["genero"].lower():
           print(f"Titulo: {libro["titulo"]} ")
           print(f"autor: {libro["autor"]}")
           print(f"genero: {libro["genero"]}")
           print(f"precio: ${libro["precio"]}")
           print(f"cantidad: {libro["cantidad"]}")
           print() 
           encontrado = True
    if encontrado == False:
        print ("No contamos con títulos del autor ingresado")    

def cargar_datos():
    try:
        with open('libros.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
        
def eliminar_libro(titulo):
    libros = cargar_datos()
    libros = [libro for libro in libros if libro['titulo'].lower() != titulo]

    with open('libros.json', 'w') as archivo:
        json.dump(libros, archivo, indent=4)
    return(libros)
    
def editar_libro(titulo):
    libros = cargar_datos()
    for libro in libros:
        if libro['titulo'].lower() == titulo:
            print(f"Editando libro con Título {titulo}:")
            print(f"Título actual: {libro['titulo']}")
            nuevo_titulo = input("Nuevo título: ")
            libro['titulo'] = nuevo_titulo
            print(f"Autor actual: {libro['autor']}")
            nuevo_autor = input("Nuevo autor: ")
            libro['autor'] = nuevo_autor
            while True:
                try:
                    nuevo_precio = int(input("Nuevo precio: "))
                    break
                except ValueError:
                    print("Por favor, ingresa un valor numérico para el precio.")
            libro['precio'] = nuevo_precio
            while True:
                try:
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    break
                except ValueError:
                    print("Por favor, ingresa un valor numérico entero para la cantidad.")
            libro['cantidad'] = nueva_cantidad
            break
    else:
        print(f"No se encontró un libro con el título '{titulo}'.")

    with open('libros.json', 'w') as archivo:
        json.dump(libros, archivo, indent=4)
    return (libros)

def tablaDeLibros(variable):
    print()
    print(f"| {" "*17}Titulo{" "*17} | {" "*8}Autor{" "*7} | {" "*5}Genero{" "*4} |   Precio   |  Cantidad  |")
    print("+","-"*40,"+","-"*20,"+","-"*15,"+","-"*10,"+","-"*8,"+")
    for libro in variable:
        print(f'| {libro["titulo"]:40} | {libro["autor"]:20} | {libro["genero"]:15} | {libro["precio"]:10} | {libro["cantidad"]:8} |')
    print()