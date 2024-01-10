def TempMedia(minima, maxima):
    
    media = (minima + maxima) / 2
    
    print(f'La temperatura media de ese dia esa: {media} ')
     
     
numero_de_dias = int(input('Escribe cuantos dias va ser: '))

for i in range(1,numero_de_dias+1):
    
    maximo = float(input(f'Escriba la temperatura maxima del dia {i}: ' ))
    minimo = float(input(f'Escribe la temperatura minima del dia {i}: '))
    TempMedia(minimo, maximo)