import json # porque lo uso para agregar un producto al archivo productos.json
from menuyvalidacionInt import validacionInt, pausa, menuPrincipal

def escribirArchivo (listado):
    print ("Se esta escribiendo al disco")
    archivoalta = open ("productos.json", "w") 
    """
    abro el archivo productos de json en modo escritura para 
    poder dar de alta los datos de productos nuevos
    """
    json.dump (listado, archivoalta, indent = 4)
    archivoalta.close ()
    print ("Escritura finalizada")

def altaProducto (listado):
    print ("******ALTA*****")

    while True:      
        Nombre = input ("Nombre del producto:  (q para salir):  ")
        if Nombre == "q":
            break
        Codigo = validacionInt ("Ingrese el codigo del producto: ")
        Marca = input ("Marca del producto: ")
        Cantidad = validacionInt ("Ingrese la cantidad: ")
        Precio = validacionInt ("Ingrese el Precio Unitario: $ ")
        
        producto = {
            "Codigo": Codigo,
            "Nombre": Nombre,
            "Marca": Marca,
            "Cantidad": Cantidad,
            "Precio" : Precio, 
            }

        listado.append (producto)
        escribirArchivo (listado)
    return listado
    
def modificacionProducto (listado):
    nombreABuscar = input ("Ingresa el nombre: ")

    for item in listado: 
        if item ["Nombre"] == nombreABuscar: #encontre el codigo
            Nombre = input (f"Nuevo nombre ({item ['Nombre']}): (Enter para no cambiar) ")
            Marca = input (f"Nuevo nombre ({item ['Marca']}): (Enter para no cambiar) ")
            Cantidad = input (f"Nueva cantidad ({item ['Cantidad']}): (Enter para no cambiar) ")
            Precio = input (f"Nuevo precio unitario ({item ['Precio']}): (Enter para no cambiar) ")
            if Nombre != "":
                item ["Nombre"] = Nombre
            if Marca != "": 
                item ["Marca"] = Marca 
            if Cantidad != "":
                item ["Cantidad"] = Cantidad
            if Precio != "":
                item ["Precio"] = Precio
            print (item)
            pausa ()
            break
    escribirArchivo (listado)
       
    return listado    

def bajaProducto (listado):
    CodigoaBuscar = validacionInt ("Ingresa el codigo: ")
    for cod in listado: 
        if cod ["Codigo"] == CodigoaBuscar:
            print ("El producto es: ", cod ["Nombre"])
            listado.remove (cod)
            break
    escribirArchivo (listado)
    print ("Eliminado correctamente")
    pausa ()
    return listado

