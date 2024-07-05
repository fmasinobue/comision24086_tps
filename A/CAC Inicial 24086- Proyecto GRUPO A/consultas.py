import json
import os

from colorama import Fore, Back, Style, init


from primerModulo import cabecera, validarInt, limpiarPantalla

""" una película
{
    "id_pelicula": 1,
    "titulo": "Cadena perpetua",
    "anio": 1994,
    "clasificacion": "+16", "+13", "+7", "ATP"
    "categoria": "Drama", "Aventura", "Comedia", "Infantil", "Suspenso"
}

"""
init()

def consultaTitulo(listado):
    cabecera("Consulta por nombre de película")
    criterio = input("Escriba el nombre de la película: ")
    peliculaNoEncontrada=False

    for pelicula in listado: 
        if criterio.lower() in pelicula["titulo"].lower():
            print(f"""Los datos de la película {Style.BRIGHT + Fore.GREEN + pelicula["titulo"] + Style.RESET_ALL} son:
                    Identificación: {pelicula["id_pelicula"]},
                    Año: {pelicula["anio"]},
                    Clasificación: {pelicula["clasificacion"]},
                    Categoría: {pelicula["categoria"]}
                    """)
            peliculaNoEncontrada=True
    if not peliculaNoEncontrada:
        print("La búsqueda no arrojó resultados")

    limpiarPantalla()



def consultaCategoria(listado):
    cabecera("Consulta de películas por categoría")
    print("Categorías disponibles: Suspenso | Drama | Infantil | Comedia | Aventura ")
    categoriaConsulta=input("Escriba la categoría a consultar: ")
    print()
    resultado = 0
   
    for pelicula in listado:
        if categoriaConsulta.lower() == pelicula["categoria"].lower():
            resultado = resultado + 1
    
    print(Style.BRIGHT + Fore.GREEN + f"Se encontraron {resultado} películas de {categoriaConsulta}:" + Style.RESET_ALL)
    
    for pelicula in listado:
        if categoriaConsulta.lower() == pelicula["categoria"].lower():
            print()
            print(f"Título: {pelicula["titulo"].ljust(45, " ")}  Año: {pelicula["anio"]}\t\t Clasificación: {pelicula["clasificacion"]}")
            
    print()
    limpiarPantalla()




def consultaAnio(listado):
    cabecera("Consulta de películas por año")
    anioConsulta = validarInt("Escribe el año que desea consultar: ")
    print("Las películas para el año consultado son:")
    print()
    print()
    print(Back.MAGENTA + Fore.RED +"-"*96 + Back.RESET)
    print(Back.MAGENTA + Fore.RED + "|", "Título".center(46), "|", "Calificación".center(20),"|" ,"Género".center(20), "|" + Back.RESET)
    print(Back.MAGENTA + Fore.RED + "-"*96  + Back.RESET + Style.RESET_ALL )
    print("|", " "*46, "|", " "*20, "|", " "* 20, "|")

    for item in listado: 
        if item["anio"] == anioConsulta:
            print(f"|{item["titulo"].center(47)} | {item["categoria"].center(20)} | {item["clasificacion"].center(20)} |")
    
    print("-"*96)
    print()
    limpiarPantalla()


 

def consultaClasificacion(listado):
    cabecera("Consulta de películas por su clasificación")
    print("Clasificación: ATP | +7 | +13 | +16 ")
    print()
    clasificacionConsulta=input("Escriba la clasificación a buscar: ")
    resultado = 0
    for pelicula in listado:
        if clasificacionConsulta.lower() == pelicula["clasificacion"].lower():
            resultado = resultado + 1
    print(Style.BRIGHT+ Fore.CYAN + f"Se encontraron {resultado} resultados:" + Style.RESET_ALL)

    for pelicula in listado:
        if clasificacionConsulta.lower() == pelicula["clasificacion"].lower():
            print()
            print(f"Título: {pelicula["titulo"].ljust(50," ")}| Año: {pelicula["anio"]}\t\t| Categoria: {pelicula["categoria"]}")
    print()
    limpiarPantalla()

###########################################################################################################################

def listadoCompleto(listado):
    
    for pelicula in listado:
        id = str(pelicula["id_pelicula"])
        anio = str(pelicula["anio"])
        print()
        print(f"{id.ljust(6," ")} {pelicula["titulo"].ljust(50, " ")} {anio.ljust(8, " ")}", end=" ")
        print(f"{pelicula["clasificacion"].ljust(10, " ")} {pelicula["categoria"].ljust(15, " ")}") 
        
    limpiarPantalla()
              

        