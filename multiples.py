def arreglo(n):
    vector = []
    for i in range(1,n+1):
        num = int(input(f'ingresa el elemento {i}: '))
        vector.append(num)
        
    return vector

def verificar(arreglo):
    arreglo1 = list(arreglo)
    for i in range(len(arreglo)-1):
        for j in range(len(arreglo)-1):
            if arreglo[j] > arreglo[j+1]:
                pr = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = pr
    count = 0    
    count2 = 0     
    for i in range(len(arreglo)):
        if arreglo[i] == arreglo1[i]:
            count = 1 + count
        if arreglo[i] != arreglo1[i]:
            count2 = 1+ count2
     
    
    if count2==0:
        print('El arreglo esta bien')
    else:
        print('El arreglo esta mal')
        
        
n = int(input('Ingresa cuantas veces: '))
vector = arreglo(n)
verificar(vector)