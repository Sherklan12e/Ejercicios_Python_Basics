# )Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve 
# el valor máximo y el mínimo.        Crea un programa que pida números por teclado y muestre el máximo y el mínimo, 
# utilizando la función anterior.


def calcular(listadenumeros):
    mayor = listadenumeros[0]
    menor = listadenumeros[0]
    for i in listadenumeros:
        
        if i > mayor:
            mayor = i
        if i < menor:
            menor = i 
    print(f'El numero mayor {mayor} y el numero {menor}')


num =  int(input('Cuantas Numero vas a ingresar: '))
lista = []
for i in range(1,num+1):
    numero = int(input(f'Ingresa el numero {i}: '))
    lista.append(numero)
    
calcular(lista)