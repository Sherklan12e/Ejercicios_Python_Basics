def superporcion(lista1, lista2):
    Bandera = False
    for i in lista1:
        if i in lista2:
            Bandera = True
    
    print(Bandera)
        
        
lista1 = [34,34,234,45,34,534,23,1]
lista2 = [1,2,3,4,5,6,7,8]
superporcion(lista1, lista2)