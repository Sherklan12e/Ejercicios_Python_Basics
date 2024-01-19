print('Escribe binarion ejemplo: 11011 solo enteros')

numero = input('Escribe el numero binario: ')
invertido = []

for i in range(len(str(numero)),0,-1 ):
    
    invertido.append(numero[i-1])
    
contador = 1
resultado = []
for i in invertido:
    
    bina = int(i) * contador
    
    contador = 2 * contador
    
    resultado.append(bina)
suma = 0
for i in resultado:
    suma += i

print('En entero es : ',suma)