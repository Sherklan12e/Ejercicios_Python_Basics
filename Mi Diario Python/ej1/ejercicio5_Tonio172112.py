#5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def suma_lista(lista):
    resultado=0
    for i in lista:
        resultado+=i
    return resultado
def mult_lista(lista):
    resultado=1
    for i in lista:
        resultado=resultado*i
    return resultado



mi_lista=[1,2,3,4]

print(suma_lista(mi_lista))
print(mult_lista(mi_lista))


