# 34)Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(lista1, lista2): 
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
            
lista1 = [1, 2, 3, 4, 3]
lista2 = [5, 6, 7, 8, 9]
print(superposicion(lista1, lista2))  