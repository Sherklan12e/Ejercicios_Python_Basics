# 31) Escribir una funcion sum() y una función multip() que sumen y multipliquen
# respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver
# 10 y multip([1,2,3,4])debería devolver 24.
def sum(lista):
    valor = 0
    for i in lista:
        valor = valor + i
    return valor

def multip(lista):
    valor = 1
    for i in lista:
        valor = valor * i 
    return valor

lista = [1,2,3,4]
print(f"La suma de la lista es: {sum(lista)}")
print(f"La multiplicacion de la lista es: {multip(lista)}")