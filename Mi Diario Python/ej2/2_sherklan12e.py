def mas_larga(lista):
    mayor = len(lista[0])
    mayorl = ''
    for i in range(len(lista)):
        
        
        if len(lista[i]) > mayor:

            mayor = len(lista[i])
            mayorl = lista[i]
        
    if mayor > len(mayorl):
        mas = lista[0]
    else:
        mas = mayorl
    return mas
    
palabras = ['Hohhhhhhhhhhhh' , 'hola', 'como estas', 'LMAO G']
print('La palabra mas larga es : ',mas_larga(palabras))