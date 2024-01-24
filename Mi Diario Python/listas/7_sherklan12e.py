def inversas(lista):
    palabras_inversa = []
    vol = ''
    for i in lista:
        longitu = len(i)
        
        for j in range(longitu -1, -1,-1):
            
            vol += i[j]

        if vol == i:
            palabras_inversa.append(vol)
            vol = ''
        else:
            vol = ''
    return palabras_inversa
    
listas = ['radar','comer','llamar','rojar','salas']

print(inversas(listas))