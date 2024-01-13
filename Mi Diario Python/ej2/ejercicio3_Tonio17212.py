# 3 Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(lista,n):
    resultado=[]
    for palabra in lista:
        if(len(palabra)>n):
            resultado.append(palabra)
    return resultado

mi_lista=["Pepe","Jose","Roberto","Alberto"]

print(filtrar_palabras(mi_lista,5))