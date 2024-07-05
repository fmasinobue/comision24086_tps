import json
import os



from primerModulo import titulo, cabecera, validarInt, accederAlSistema, limpiarPantalla, creditos
from ABM import altaPelicula, modificacionPelicula, bajaPelicula
from consultas import consultaTitulo,  consultaCategoria, consultaAnio, consultaClasificacion, listadoCompleto


d = os.path.dirname(__file__)
os.chdir(d)

try:
    archivo = open("peliculas.json", "r")
    peliculas = json.load(archivo)
    archivo.close()
except FileNotFoundError:
    peliculas = []

try:
    registro = open("credenciales.json", "r")
    credenciales = json.load(registro)
    registro.close()
except FileNotFoundError:
    credenciales =[]

print("🎦 Bienvenido a Movieland 🎦\nIngrese sus datos para acceder al sistema.")
accesoAlSistema = accederAlSistema(credenciales)

limpiarPantalla()


while accesoAlSistema:
    titulo("Movieland")
    print()
    
    print("1] Gestión de películas")
    print("2] Buscar película")
    print("3] Listado de películas")
    print("4] Créditos")
    print("Presione 0 para salir")

    opcionUsuario = validarInt("Ingrese la opción deseada (1,2,3,4,0): ")
    if opcionUsuario == 0:
        break

    elif opcionUsuario == 1:
        cabecera("Gestión de películas")
        print("1] Alta de películas")
        print("2] Modificación de películas")
        print("3] Baja de películas")
        print("Presione 0 para volver al menú principal")
        opcionSubmenu = validarInt("Ingrese la opción deseada (1,2,3,0): ")
        if opcionSubmenu == 0:
            continue
        elif opcionSubmenu == 1: #Alta de películas
            peliculas = altaPelicula(peliculas)
        elif opcionSubmenu == 2: #Modificación de películas
            peliculas = modificacionPelicula(peliculas)
        elif opcionSubmenu ==  3: #Baja de películas
            peliculas = bajaPelicula(peliculas)
 

    elif opcionUsuario == 2:
        cabecera("Buscar películas")
        print("1] Buscar por nombre")
        print("2] Buscar por género")
        print("3] Buscar por año")
        print("4] Buscar por clasificación")
        print("Presione 0 para retroceder.")
        opcionSubmenu = validarInt("Ingrese la opción deseada (1,2,3,4,0): ")
        if opcionSubmenu == 0:
            continue
        elif opcionSubmenu ==1:
            consultaTitulo(peliculas)
        elif opcionSubmenu ==2:
            consultaCategoria(peliculas)
        elif opcionSubmenu ==3:
            consultaAnio(peliculas)
        elif opcionSubmenu ==4:
            consultaClasificacion(peliculas)

            

    elif opcionUsuario == 3:
        print()
        cabecera("Listado de películas")
        listadoCompleto(peliculas)
        
    elif opcionUsuario == 4:
        cabecera("Créditos")
        creditos()

    else:
        print("Ingrese una opción válida.")
        limpiarPantalla()
       

cabecera("Programa finalizado")
print()
print()
