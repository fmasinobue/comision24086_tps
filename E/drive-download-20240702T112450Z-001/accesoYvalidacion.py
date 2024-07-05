from colorama import init, Fore

init()
def acceso(leyenda):
    
    continuar=True
    while continuar:
        numero = input(leyenda)
        if numero.isdigit():
            continuar = False
        else:
            print("No es una opcion valida")
   
    numero = int(numero)
    return numero

def validacionNumero(leyenda,esperarEnter=False):

    while True:
        opcion = input(leyenda)
        if esperarEnter==True and opcion == "":
            return opcion
        try:
           opcion = int(opcion)
           return opcion
        except:
            print(Fore.LIGHTRED_EX, f"Por favor ingrese solo números", Fore.LIGHTWHITE_EX)
 

