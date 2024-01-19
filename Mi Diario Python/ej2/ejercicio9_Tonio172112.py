"""
Ejercicio 9
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""

import os

def contar_vocales(palabra):
    vocales={'A':0,'E':0,'I':0,'O':0,'U':0}
    palabra=palabra.upper()
    for c in palabra:
        if(c in vocales.keys()):
            vocales[c]+=1
    for v,cant in vocales.items():
        print(f" Cantidad de letras {v} = {cant}")


while True:
    os.system("cls||clear")
    try:
        cad=input(" Ingrese su palabra: ").title().strip()
        cad=''.join([i for i in cad if (i.isalpha()) or (i.isspace())])
        cad=" ".join(cad.split())
        if(len(cad)<1):
            raise ValueError
    except ValueError:
        print(" Ingrese una palabra no caracteres especiales ni numeros.")
    except:
        print(" Ocurrió un error con la palabra ingresada.")
    else:
        print(f" Su palabra {cad} contiene: ")
        contar_vocales(cad)
        input("\n\n Presione ENTER para continuar . . .")
        while True:
            os.system('cls||clear')
            dec=input(" ¿Desea volver a utilizar el programa? (Y/N)\n ").upper().strip()
            if(dec=='Y' or dec=='SI'):
                break
            elif(dec=='N' or dec=='NO'):
                print("\n\t\t Programa Finalizado . . . ")
                input(" Pulse Enter para continuar . . . ")
                exit()
            elif(dec=='KASHIMO'):
                import webbrowser
                print(" otra mas . . .")
                webbrowser.open("https://www.youtube.com/watch?v=8nxaZ69ElEc")
                input(" Presione ENTER para continuar")
            else:
                print(" Ingrese una opcion valida del menu.")
                input(" Pulse Enter para continuar . . . ")
            