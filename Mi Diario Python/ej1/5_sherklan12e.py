def sumar(listasuma):
    suma = 0
    for i in listasuma:
        suma = suma + i
        
    return suma
def multiplicar(listamultiplicar):
    multi = 1
    for  i in listamultiplicar:
        multi = i * multi
        
    return multi

lista = [1,2,3,4]

multiplica = multiplicar(lista)
suma = sumar(lista)

print(multiplica)
print(suma)
    