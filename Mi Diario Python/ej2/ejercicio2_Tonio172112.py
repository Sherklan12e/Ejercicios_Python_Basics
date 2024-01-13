# 2 Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(lista):
    mayor=lista[0]
    for i in lista:
        if(len(i)>len(mayor)):
            mayor=i
    return mayor

mi_lista=["Pepe","Roberto","Jose","Robert"]

print(mas_larga(mi_lista))