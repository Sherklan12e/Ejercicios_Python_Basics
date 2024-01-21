def posicionesPares(lista):
    print('==============')
    for i in range(1,len(lista) ) :
        if i %2==0:
           print(lista[i],f' Posicion par :{i}') 
    
    


listas = ['H','o','l','a','','c','o','m','o','e','s','t','a','s']


print(posicionesPares(listas))