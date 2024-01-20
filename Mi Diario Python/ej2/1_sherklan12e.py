def mayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor
    
lista = [1,65,45,72,5,2,76,87,78]

print(mayor(lista))