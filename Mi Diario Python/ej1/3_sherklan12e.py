def longitud(lista):
    count = 0 
    for i in lista:
        count = count +1
    
    return count
palabra = ['hola', 'como estas', 'Bien ', 'And you']
print(longitud(palabra))
