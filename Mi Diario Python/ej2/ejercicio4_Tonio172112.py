#4 - Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

def n_mayus(cad):
    mayus=0
    for letra in cad:
        letra_mayus=letra.upper()
        if(letra==letra_mayus and letra!=" "):
            mayus+=1
    return mayus

cadena=input(" Ingrese una cadena: ")
print(f" La cantidad de mayusculas en su cadena ({cadena}) es: {n_mayus(cadena)}")