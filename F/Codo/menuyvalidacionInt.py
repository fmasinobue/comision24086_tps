import os
#def funcion donde imprime el menu 
def menuPrincipal(menup, cantidadCaracter=80):
    """ 
defino una funcion llamada menuPrincipal para que imprima en forma
vistosa el titulo del menu principal cuyo parametro es menup.
"""
    os.system("cls") 
    """
    borra pantalla 
    """
    cantMedio = cantidadCaracter - 2
    print("*" * cantidadCaracter)
    print(f"*{menup.center (cantMedio, " ")}*")
    print("*" * cantidadCaracter)
    """
    una vez que limpia pantalla imprime el menu principal
    """

#funcion que valida un entero
def validacionInt(menup): 
    """ funcion que retorna un entero, no permite ingresar letras 
    solo enteros """
    #continuar=True
    while True:
        numero = input(menup)
        #if numero.isdigit():
        # continuar = False #termina de preguntar xq ya ingreso con un entero
        #else:
        try:
            """ detecta errores y los corrige """
            numero = int (numero)
            if numero == 0:
                print("Código invalido, vuelva a intentar")
            elif numero != 0:
                return numero
        except: 
            print(f"Ingrese solo números ({numero})")
        #endif
    #endwhil
    #numero = int(numero)
    #return numero
#enddef 

def pausa (menup = "Presiona enter para continuar ... "):
    """
    defino funcion pausa para parar la ejecucion
    """
    input (menup)