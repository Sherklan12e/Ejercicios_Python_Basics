#Ejercicio 1 La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_list(lista):
    mayor=lista[0]
    for i in lista:
        if(i>mayor):
            mayor=i
    return mayor

mi_lista=[1,2,3,4,5,6,7,8,9,10]

print(max_list(mi_lista))