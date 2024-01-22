from typing import List , Union

def ordenada(lista: Union[List[str], List[int]]) -> bool:
    
    for i in range(len(lista) -1):
        
        
        if lista[i] > lista[i+1]:
            return False
        
    return True
    

lista_int = [1,2,5]
lista_str = ['s','a','g','h']


print(ordenada(lista_str))
print(ordenada(lista_int))