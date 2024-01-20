"""
Ejercicio 7
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

"""
import os

def mostrar_mayores(lista,e):
    for edad in lista:
        if(edad>e):
            print(f" Persona Numero {lista.index(edad)+1}: {edad} años")
    input(" Pulse Enter para continuar . . . ")
    os.system('cls||clear')   

def asignar_edades(lista,n):
    for i in range(n):
        while True:
            os.system('cls||clear')
            try:
                v=int(input(f" Ingrese la edad de la persona {i+1}: "))
                if(v<=0 or v>=150):
                    raise ValueError()
                break
            except ValueError:
                print(" Ingrese una edad valida, mayor a 0 y menor a 150.")
                input(" Pulse Enter para continuar . . . ")
        lista.append(v)
    os.system('cls||clear')
    print(f" Las edades de las {n} personas fueron guardadas exitosamente")
    input(" Pulse Enter para continuar . . . ")
    os.system('cls||clear')   

while True:
    edades=[]
    error=0
    os.system('cls||clear')
    print("\t\t\t\t\t--Ejercicio 7--\n\n")
    while True:
        try:
            if(error==1):
                print(" Ingrese un numero valido, mayor a 0")
                error=0
            else:
                print("\n")
            n=int(input(" Ingrese la cantidad de personas: "))
            if(n<=0):
                raise ValueError()
            break
        except ValueError:
            error=1
        
    asignar_edades(edades,n)

    while True:
        try:
            if(error==1):
                print(" Ingrese una edad valida, mayor a 0 y menor a 150")
                error=0
            else:
                print("\n")
            e=int(input(" Ingrese la edad de las personas a mostrar (mayor a): "))
            if(e<=0 or e>=150):
                raise ValueError()
            break
        except ValueError:
            error=1
    print(f" Las personas mayores a {e} años son: ")
    mostrar_mayores(edades,e)
    while True:
        dec=input(" ¿Desea volver a usar el programa? (Y/N)\n\t").upper().strip()
        if(dec=='Y' or dec=='SI'):
            break
        elif(dec=='N' or dec=='NO'):
            print("\n\t\t Programa Finalizado . . . ")
            input(" Pulse Enter para continuar . . . ")
            exit()
        else:
            print(" Ingrese una opcion valida del menu.")
            input(" Pulse Enter para continuar . . . ")

    
