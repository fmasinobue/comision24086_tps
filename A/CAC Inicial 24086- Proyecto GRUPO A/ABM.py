import json
import os

from colorama import Fore, Style, init

from primerModulo import cabecera, validarInt, limpiarPantalla

""" una película
{
    "id_pelicula": 1,
    "titulo": "Cadena perpetua",
    "anio": 1994,
    "clasificacion": "+16", "+13", "+7", "ATP"
    "categoria": "Drama", "Aventura", "Infantil", "Comedia", "Suspenso"
}

"""

init() 

def escribirArchivo(listado):
    print("Comenzando la escritura al disco")
    peliculas = open("peliculas.json", "w")
    json.dump(listado, peliculas, indent=4)
    peliculas.close()
    print("Finalizada la escritura al disco")


def altaPelicula(listado):
    cabecera("Alta de películas")
   
    while True:
        nuevoidPelicula = validarInt("Nro. de Identificación de la Película Nueva (0 para salir): ")
        if nuevoidPelicula == 0:
            limpiarPantalla()
            break

        while True:   
            
            for pelicula in listado:
                
                if nuevoidPelicula == pelicula["id_pelicula"]:
                    print(Fore.RED + f"{nuevoidPelicula} ya está siendo utilizado." + Fore.RESET )
                    nuevoidPelicula = validarInt("Nro. de Identificación de la Película Nueva (0 para salir): ")

            break
            
            
        print("Escriba los datos de la nueva película ")
        titulo = input("Escriba el título de la película: ")
        anio = validarInt("Escriba el año de la película: ")
        clasificacion = input("Escriba la clasificación (+16/+13/+7/ATP):")
        categoria = input("Escriba la categoría (Infantil/Aventura/Comedia/Suspenso/Drama): ")
        pelicula = {
            "id_pelicula": nuevoidPelicula,
            "titulo": titulo,
            "anio": anio,
            "clasificacion": clasificacion,
            "categoria": categoria
        }
        listado.append(pelicula)
        escribirArchivo(listado)

        limpiarPantalla()
        return listado

def modificacionPelicula(listado):
    cabecera("Modificación de películas")
    idNoEncontrado=False
    idABuscar = validarInt("Escriba el número de identificación de la película: ")
    for item in listado: 
         
        if idABuscar == item["id_pelicula"]:
            print(Fore.YELLOW + "Los datos de la película son:" + Fore.RESET)
            print(f"""
                  Título: {item['titulo']},
                  Año: {item['anio']},
                  Clasificación: {item['clasificacion']}
                  Categoría: {item['categoria']}
                  """)
            print()
            idNuevo = input("Escribe el nuevo id: (Enter para no cambiar) ")
            tituloNuevo = input(f"Modificar Título: (Enter para no cambiar) ")
            anioNuevo = input(f"Modificar Año: (Enter para no cambiar) ")
            clasificacionNueva = input(f"Modificar Clasificación: (Enter para no cambiar) ")
            categoriaNueva = input(f"Modificar Categoría: (Enter para no cambiar) ")

            if idNuevo !="":
                item["id_pelicula"] = int(idNuevo)
            if tituloNuevo != "":
                item["titulo"]= tituloNuevo
            if anioNuevo != "":
                item["anio"]= int(anioNuevo)
            if clasificacionNueva != "":
                item["clasificacion"] = clasificacionNueva
            if categoriaNueva != "":
                item["categorria"] = categoriaNueva
            print()
            print(Fore.MAGENTA + "Los datos han sido actualizados: " + Fore.RESET)
            print(f"""
                  Id: {item['id_pelicula']},
                  Título: {item['titulo']},
                  Año: {item['anio']},
                  Clasificación: {item['clasificacion']}
                  Categoría: {item['categoria']}
                  """)
            idNoEncontrado=True

            escribirArchivo(listado)

    if not idNoEncontrado:
        print(Fore.RED + "Id no asociado a película" + Fore.RESET)

    
    limpiarPantalla()
    return listado


def bajaPelicula(listado):
    cabecera ("Dar de baja una Película")

    idABuscar = validarInt("Escriba el número de identificación de la película: ")
    for item in listado: 
        if item["id_pelicula"] == idABuscar:
            print(Fore.CYAN + "Los datos de la película son:" +  Fore.RESET)
            print(f"""
                  Título: {item['titulo']},
                  Año: {item['anio']},
                  Clasificación: {item['clasificacion']}
                  Categoría: {item['categoria']}
                  """)
            print()
            eliminaPelicula=input("¿Está seguro que desea eliminar este registro? S/n: " )
            if eliminaPelicula =="S" or eliminaPelicula =="s":
                listado.remove(item)
                #break
                escribirArchivo(listado)
                print(Fore.GREEN + "Registro eliminado correctamente" + Fore.RESET)
            else:
                print(Fore.RED + "El registro no se eliminó" + Fore.RESET)
    limpiarPantalla()
    return listado