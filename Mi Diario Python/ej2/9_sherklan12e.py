
def contar_vocales(elegi):
    a = 0
    e = 0
    isf = 0
    o = 0
    u =0     
    for i in elegi:
        if 'a' == i:
            a +=1
        elif 'e' == i:
            e +=1
        elif 'i' == i:
            isf +=1
        elif 'o' == i:
            o +=1
        elif 'u' == i:
            u+=1
    
    print(f'Las voacales: \na:{a} \ne:{e} \ni:{isf} \no:{o} \nu:{u}')
    print(f'La palabra :{elegi}')


lista = ['comer','correir','yyyy', 'akkkkk', 'llllll','yyyyyy']




count = 0
listas = []
vocales = 'aeiouAEIOU'
for i in range(len(lista)):
    
        for x in lista[i]:
            if x in vocales:
                
                count += 1
        
        if count > 0:
            listas.append(lista[i])
            count = 0
print('Las palabras :', lista)
print('filtro: ',listas)

elegil = input('Escribe la palabra para contar cuantas vocales tiene: ')
contar_vocales(elegil)