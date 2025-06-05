# 30)- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
# devuelve False.


def es_vocal(letra):
    if letra.lower() in "aeiou":
        return True
    return False

palabra = input("Ingrese una palabra: ")

print(es_vocal(palabra))