import os
import time
from modulo_dos import productos

def pausa(leyenda="Presione enter para continuar..."):
    input(leyenda)

def alta_producto(productos): #Función para alta de producto
    os.system("cls")
    print("🔨"*14)
    print(f'🔨 \tALTA PRODUCTO \t  🔨')
    print("🔨"*14)
    codigo_flag = False  #Bandera que se usa en el bucle for para verificar si el código ya existe       
    while True:
        print("Presione 'q' si quiere abortar la carga de este item")
        producto = input("Producto: ")
        if producto == "q":
            break
        descripcion = input("Descripción: ")
        if descripcion == "q":
            continue
        codigo_aux = validacion_entero("Código: ")
        for codigo in productos:
            if codigo_aux == codigo["Código"]: #Verifica si el código ya existe
                print(f'| El código ya existe')
                print(f'| SE ABORTA LA CARGA DE: {producto.upper()}')
                print(f'| Por favor vuerlva a comenzar')
                codigo_flag = True
        codigo = codigo_aux
        if codigo == "q" or codigo_flag == True:
            continue
        cantidad = validacion_entero("Cantidad: ")
        if cantidad == "q":
            continue
                
        productos_temp = {
            "Código": codigo,
            "Producto": producto,
            "Descripción": descripcion,
            "Cantidad": cantidad,
            }
        productos.append(productos_temp)
        print("-"*60)
        print(f""" Producto Agregado:
            Código: {codigo}
            {producto.upper()}, {descripcion.title()}
            Cantidad: {cantidad}""")
        print("-"*60)
        continuar = input("Enter para cargar otro producto, 'q' terminar: ")
        if continuar == "q":
            break
    return productos
    
def cabecera(leyenda, cantidad_caracter=80, recuadro="#"): #función cabecera, limpia la pantalla y muestra el título
    os.system("cls")
    cant_medio = cantidad_caracter - 2
    print(recuadro*cantidad_caracter)
    print(f"{recuadro}{leyenda.center(cant_medio,' ')}{recuadro}")
    print(recuadro*cantidad_caracter)

def cabecera_emoji(leyenda_emoji, cantidad_caracter_emoji=80, recuadro_emoji="⚪"): #función cabecera, limpia la pantalla y muestra el título
    os.system("cls")
    cant_medio_emoji = cantidad_caracter_emoji*2 - 4
    print(recuadro_emoji*cantidad_caracter_emoji)
    print(f"{recuadro_emoji}{leyenda_emoji.center(cant_medio_emoji,' ')}{recuadro_emoji}")
    print(recuadro_emoji*cantidad_caracter_emoji)

def validacion_entero(leyenda, permite_enter=False): #función para validar la entrada de enteros en el código del producto
    while True:
        numero = input(leyenda)
        if permite_enter and numero == "":
            return numero
        try:
            numero = int(numero)
            return numero
        except:
            if numero == "q":
                return numero
            else:
                print(f"({numero}) No es válido '{leyenda}' solo admite números")

def validacion_menu(leyenda, opcion_max): #funcion para evitar que se rompa el programa
    while True:
        numero = input(leyenda)
        try:
            numero = int(numero)
            if numero <= opcion_max:
               return numero
        except:
            continue

def validacion_s_n(leyenda): #funcion para evitar que se rompa el programa
    while True:
        s_n = input(leyenda)
        s_n = s_n.upper()
        if s_n == "S" or s_n == "N":
            return s_n
        else:
            print(f'{s_n} No es válido (s/n)')
            continue

def modificacion_producto(productos):
    os.system("cls")
    print("🔨"*18)
    print(f'🔨 \tMODIFICACION PRODUCTO \t  🔨')
    print("🔨"*18)
    
    print("Presione 'q' si quiere abortar")
    entrada = True
    while entrada == True:
            codigo_encontrado_flag = False
            codigo_a_buscar = validacion_entero("Ingrese Código a modificar: ")
            if codigo_a_buscar == "q":
                break
            
    
            for codigo in productos: 
                if codigo["Código"] == codigo_a_buscar:
                    codigo_encontrado_flag = True
                    print("Enter para no cambiar el Item")
                    producto = input(f'Nombre actual: {codigo["Producto"]} ➡ : ')
                    descripcion = input(f'Descripción actual: {codigo["Descripción"]} ➡ : ')
                    cantidad_temp = codigo["Cantidad"]
                    cantidad = validacion_entero(f'Cantidad actual: {codigo["Cantidad"]} ➡ : ', permite_enter=True)
                    if producto != "":
                        codigo["Producto"]= producto
                    if descripcion != "":
                        codigo["Descripción"]= descripcion
                    if cantidad != "":
                        codigo["Cantidad"] = cantidad
                    if cantidad == "":
                        codigo["Cantidad"] = cantidad_temp
                    print("-"*60)
                    print(f""" Producto Modificado:
                    Código: {codigo["Código"]}
                    {codigo["Producto"].upper()}, {codigo["Descripción"].title()}
                    Cantidad: {codigo["Cantidad"]}""")
                    print("-"*60)
                    break
            if codigo_encontrado_flag == False:
                print("Codigo no encontrado")
                entrada_flag = validacion_s_n("¿Quiere volver a intentar? s/n: ")
            if codigo_encontrado_flag == True:
                entrada_flag = validacion_s_n("¿Quiere modificar otro producto? s/n: ")
            if entrada_flag == "S":
             entrada = True
            if entrada_flag == "N":
                entrada = False
    return productos

def baja_producto(productos):
    os.system("cls")
    print("🔨"*18)
    print(f'🔨 \tELIMINAR PRODUCTO \t  🔨')
    print("🔨"*18)
    print("Presione 'q' si quiere abortar")
    entrada = True
    while entrada == True:
            codigo_encontrado_flag = False
            codigo_a_buscar = validacion_entero("Ingrese Código del producto a eliminar: ")
            if codigo_a_buscar == "q":
                break
             
            for codigo in productos: 
                if codigo["Código"] == codigo_a_buscar:
                    codigo_encontrado_flag = True
                    productos.remove(codigo)
                    break
            
            if codigo_encontrado_flag == False:
                print("Codigo no encontrado")
                entrada_flag = validacion_s_n("¿Quiere volver a intentar? s/n: ")
            if codigo_encontrado_flag == True:
                for i in range(0,5,1):
                    print(f'\rEliminando{i*"."}', end="")
                    time.sleep(0.4)
                print("\nEliminado")
                entrada_flag = validacion_s_n("¿Quiere eliminar otro producto? s/n: ")
            if entrada_flag == "S":
             entrada = True
            if entrada_flag == "N":
                entrada = False
    return productos