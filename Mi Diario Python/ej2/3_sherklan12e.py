def filtrar_palabra(lista, entero):
    nueva = []
    for i in lista:
        if len(i) > entero:
            nueva.append(i) 
    return nueva

palabras = ['hola','calla','ah','superpoder','comi']

print(filtrar_palabra(palabras, 4))