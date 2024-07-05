import os
import time
import json

import encabezado
from acceso_al_sistema import solicitar_credenciales
from agregar_cliente import agregar_cliente
from modificar_cliente2 import modificar_cliente
from eliminar_cliente import eliminar_cliente
from creditos import creditos


solicitar_credenciales()

#Directorio JSON
d = os.path.dirname(__file__)
os.chdir(d)

#Carga inicial de clientes desde archivo JSON
try:
    archivo = open("clientes_db.json", "r")
    clientes = json.load(archivo)
    archivo.close()
except FileNotFoundError:
    clientes = []



def titulo_menu(pagina):
    print('*'*50)
    print(f'{pagina}'.center(50))
    print('*'*50)

titulo_menu('MENÚ PRINCIPAL')



# Se define función para imprimir en pantalla el menú de opciones

def menu_principal():
    print('''
1 - Nuevo cliente
2 - Actualizar cliente
3 - Eliminar cliente
4 - Créditos
0 - Salir
          ''')
    



# Se define función de selección del usuario

def principal():
    while True:

        menu_principal()
        opcion_usuario = input('Elija una opción: ')
  
        if opcion_usuario == '1':
            agregar_cliente(clientes)

        elif opcion_usuario == '2':
            modificar_cliente(clientes)
            # actualizar_clientes

        elif opcion_usuario == '3':
            eliminar_cliente(clientes)
            # eliminar_cliente

        elif opcion_usuario == '4':
            creditos()
            # creditos

        elif opcion_usuario == '0':
            print('Cerrando programa... ¡MUCHAS GRACIAS!')
            borrarPantalla = lambda: os.system('cls')
            time.sleep(1)
            borrarPantalla()

            break

        else:
            print('La opción seleccionada no es válida. Intente nuevamente.')
            
principal()
