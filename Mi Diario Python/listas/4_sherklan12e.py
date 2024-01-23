from typing import List , Union
#A
def duplicado(lista: Union[List[str],List[int]] )-> bool:
    logintud = len(lista)
    for i in range(logintud):
        for j in range(i+1, logintud):
            if lista[i] ==lista[j]:
                return True
        
    return False
#B














def Generador_de_numero(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i+1, n):
            if lista[i] == lista[j]:
                return True
    return False

lista = [1,4,5,2,4]
print(Generador_de_numero(lista))