"""
Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

import os

def spac(cad):
    cad=''.join([i for i in cad if (i.isalpha()) or (i.isspace())])
    cad=" ".join(cad.split())
    return cad

def pause():
    input(" Pulse ENTER para continuar. . .")
    os.system("cls||clear")

def agregar_nombre(lista):
    while True:
        os.system('cls||clear')
        print(f"\t\t\t\t\t--Agregar nombre--\n")
        try:
            n=input("\n Ingrese el nombre a agregar a la lista (ingrese 0 para salir): ").title().strip()
            if(n=='0'):
                return
            n=spac(n)
            if(len(n)<=0):
                raise ValueError

        except ValueError:
            print(" Ingrese un nombre, sin numeros ni caracteres especiales")
            pause()
        except:
            print(" Algo salió mal al ingresar el nombre")
            pause()
        else:
            lista.append(n)
            print(f" El nombre {n} se agregó correctamente a la lista.")
            pause()
            return
    
def mostrar_elementos(lista):
    os.system("cls")
    print(f"\t\t\t\t\t--Lista Nombres--\n\n")
    if(len(lista)<1):
        print(" La lista esta vacia")
        pause()
        return
    print(" Lista:",end=" ")
    for i,a in enumerate(lista):
        print(f"{a} [{i}]",end="")
        if(i!=len(lista)-1):
            print(",",end=" ")
        if(i==len(lista)-1):
            print("\n\n") 
    pause()
    return

def eliminar(lista):
    while True:
        os.system("cls")
        if(len(lista)<1):
            print(" La lista esta vacia")
            pause()
            return 
        print(f"\t\t\t\t\t--Eliminar nombre--\n")
        try:
            busc=int(input(f" Ingrese la posicion de la lista del nombre que desea eliminar: "))
        except ValueError:
            print(" Ingrese un numero valido.")
            pause()
        else:
            if(busc<0 or busc>len(lista)-1):
                print(" El indice ingresado no se encuentra en la lista.")
                pause()
            else:
                while True:
                    dec=input(f" El indice ingresado {busc} contiene el nombre {lista[busc]}, ¿Desea eliminar ese valor? Y/N\n ").upper().strip()
                    if(dec=='Y' or dec=='SI'):
                        del lista[busc]
                        print(f" El nombre en el indice {busc} fue eliminado correctamente.")
                        pause()
                        return
                    elif(dec=='N' or dec=='NO'):
                        print(f" El nombre en el indice {busc} no fue eliminado.")
                        pause()
                        return
                    else:
                        print(" Ingrese una opcion valida (Y/N).")
                        pause()

def buscar(lista):
    while True:
        encontrados=[]
        aux=0
        os.system('cls||clear')
        print(f"\t\t\t\t\t--Buscar nombre--\n")
        if(len(lista)<1):
            print(" La lista esta vacia")
            pause()
            return 
        try:
            inc=input(" Ingrese la inicial que desea utilizar para su busqueda (ingrese 0 para salir): ").upper().strip()
            if(inc=='0'):
                return
            inc=spac(inc)
            if(len(inc)<1 or len(inc)>1):
                raise ValueError
        except ValueError:
            print(" Ingrese una sola letra como inicial, no numeros ni caracteres especiales.")
            pause()
        except:
            print(" Ocurrió un problema al buscar el nombre por su inicial.")
            pause()
        else:
            for nombre in nombres:
                if(nombre[0]==inc):
                    encontrados.append(nombre)
                else:
                    for car in nombre:
                        if(aux==1 and car==inc):
                            encontrados.append(nombre)
                        if(car==' '):
                            aux=1
                        else:
                            aux=0

            os.system("cls||clear")
            if(len(encontrados)>0):
                print(f" Los nombres que comienzan con la letra {inc} son: ")
                for i in range(len(encontrados)):
                    print(f"\t\t\t\t {encontrados[i]}")
                    if(i==len(encontrados)-1):
                        print("\n")
                pause()
                return
            else:
                print(f" Ningun nombre en la lista comienza con la letra {inc}")
                pause()
                return

nombres=[]
error=0

while True:
    os.system('cls||clear')
    print("\t\t\t\t\t--Ejercicio 8--\n\n")
    print(" 1 - Agregar Nombre a Lista.")
    print(" 2 - Buscar por Inicial.")
    print(" 3 - Eliminar Nombre.")
    print(" 4 - Mostrar Lista")
    print(" 0 - Salir.\n")
    if(error==1):
        print("\n Ingrese una opcion valida del menu.")
        error=0
    else:
        print("\n")
    menu=input("\t\t Ingrese la opcion del menu: ").upper().strip()
    if(menu.isnumeric()):
        menu=int(menu)
    else:
        menu=spac(menu)
    if(menu==1 or menu=='AGREGAR' or menu=='AGREGAR NOMBRE' or menu=='ADD'):
        agregar_nombre(nombres)
    elif(menu==2 or menu=='BUSCAR' or menu=='INICIAL' or menu=='SEARCH'):
        buscar(nombres)
    elif(menu==3 or menu=='ELIMINAR' or menu=='ELIMINAR NOMBRE' or menu=='DELETE' or menu=='DEL'):
        eliminar(nombres)
    elif(menu==4 or menu=='MOSTRAR' or menu=='LISTA' or menu=='SHOW' or menu=='LIST'):
        mostrar_elementos(nombres)
    elif(menu==0 or menu=='S' or menu=='SALIR' or menu=='EXIT'):
        print("\n\t\t Programa Finalizado . . . ")
        input(" Pulse Enter para continuar . . . ")
        exit()
    elif(menu==17 or menu=='KASHIMO'):
        import webbrowser
        print(" . . .")
        webbrowser.open("https://www.youtube.com/watch?v=Uh6dkL1M9DM")
        pause()
    else:
        error=1
