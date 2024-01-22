from typing import List 

def ordenada(lista: List )-> bool:
    
    for i in range(len(lista) - 1):
        if type(lista[i]) != type(lista[i + 1]):
            
            return False
        if lista[i] > lista[i + 1]:
            
            return False
    return True
    

lista_int = [1,2,5,2,65,1,6]
lista_str = ['a','f','g','h']


print(ordenada(lista_str))