import os
import time


#acceso al sistema 


def solicitar_credenciales():

        TOPE = 3
        accesoPermitido = False
        intentos = 0

        while intentos <= TOPE:
                intentos = intentos + 1
                print("Accediendo al sistema")
                usuario = input("Usuario: ")
                clave = input("Clave: ")
                        #usuario = "admin"
                        #clave = "1234"


                if usuario == "admin" and clave == "1234":
                        print("\nAcceso Correcto")
                        intentos = TOPE + 1 
                        accesoPermitido = True
                        borrarPantalla = lambda: os.system('cls')
                        time.sleep(1)
                        borrarPantalla()
                        break

                elif usuario != "admin":
                        intentosRestantes = TOPE - intentos
                        print("NOMBRE DE USUARIO INCORRECTO")
                        print(f"Intentos restantes: {intentosRestantes}")

                else: 
                        intentosRestantes = TOPE - intentos
                        print("USUARIO o CONTRASEÑA INCORRECTAS ")
                        print(f"Intentos restantes: {intentosRestantes}")
                        

solicitar_credenciales()






