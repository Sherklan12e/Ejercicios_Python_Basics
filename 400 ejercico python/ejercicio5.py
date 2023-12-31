# Hacer un programa que solicite un color por teclado e imprima “Puede pasar “ si el 
# color ingresado es verde , “Precaución “ si es amarillo , “No pasar “ si es rojo o “Color 
# inválido” si es cualquier otro. 

color = input('Escribe el nombre de tu color: ')

if color=='verde':
    print('puede pasar')
elif color=='amarillo':
    print('Precaucion')
elif color == 'rojo':
    print('No pasar')
else:
    print('color invalido')