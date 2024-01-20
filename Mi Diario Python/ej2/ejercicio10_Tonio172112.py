"""
Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""

import os

def pause():
    input(" Pulse ENTER para continuar. . .")
    os.system('cls||clear')

def es_bisiesto(año):
    if((año%4==0 and año&100!=0) or año%400==0):
        return True
    else:
        return False

while True:
    os.system('cls||clear')
    try:
        año=int(input(" Ingrese el año para determinar si es bisiesto: "))
        if(año<1):
            raise ValueError
    except ValueError:
        print(" Ingrese un año mayor a 0.")
        pause()
    except:
        print(" Ocurrió un error al registrar el año ingresado.")
        pause()
    else:
        if(es_bisiesto(año)):
            print(f" El año {año} es bisiesto.")
            pause()
        else:
            print(f" El año {año} no es bisiesto.")
            pause()
        while True:
            os.system('cls||clear')
            dec=input(" ¿Desea volver a usar el programa (Y/N)\n\t").upper().strip()
            if(dec=='Y' or dec=='SI'):
                break
            elif(dec=='N' or dec=='NO'):
                print(" Programa Finalizado. . .")
                pause()
                exit()
            else:
                print(" Ingrese una opcion valida del menu (Y/N).")
                pause()
            
