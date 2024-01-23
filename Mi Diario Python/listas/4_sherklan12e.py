from typing import List , Union
import random
#A
def duplicado(lista: Union[List[str],List[int]] )-> bool:
    logintud = len(lista)
    for i in range(logintud):
        for j in range(i+1, logintud):
            if lista[i] ==lista[j]:
                return True
    return False
#B
def general():
    lista= []
    for i in range(1,23+1):
        numero = random.randint(1,100)
        lista.append(numero)
        
    return lista


randomlist= general()

print(randomlist)
print(duplicado(randomlist))
