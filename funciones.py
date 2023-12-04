def nelementos(c):
    arreglo = []
    for i in range(1,c+1):
        n = int(input(f'Ingresa el {i}: '))
        arreglo.append(n)
        
    return arreglo

def buscar(b,a):
    arreglo = b 
    numero = a
    indexx = 0
    count = 0
    for i in range(len(arreglo)):
        if arreglo[i]==numero:
            indexx = i
        else:
            count = 1 + count
            
    if count>0:
        print('El numero buscado no se encuentra en la lista ')
    else:
        print('esta en la posicion: ', indexx+1, count)
N = int(input('Escribe cuantos elementos quieres en tu arreglo: '))
vector = nelementos(N)
cuanto = int(input('pon el numero que quieres buscar: '))
buscar(vector, cuanto)