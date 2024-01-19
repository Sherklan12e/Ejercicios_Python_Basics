cadena = input('Ingresa una cadena fucking usuario: ')
ma = 'ABCDEFGHIJKLOPQSRUVXYZ'
contador = 0
for i in cadena:
    if i in ma:
        contador += 1 
    
print('Las veces que hay mayuscula son : ' , contador)