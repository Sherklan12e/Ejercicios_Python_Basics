# Hacer un programa que imprima una tabla de multiplicar del 2 al 9 . Cada uno debe 
# mostrar sus valores multiplicados del 1 al 9 inclusive

for i in range(2,9+1):
    for x in range(2,12+1):
        print(f' {i} * {x}   {i * x} ')
    print('=======================')