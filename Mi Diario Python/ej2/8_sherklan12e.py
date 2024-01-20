def buscar(lista , x):
    listane = []
    for i in lista:
        if x in i:
            listane.append(i)
        
    print(listane)
    
    


lista = ['nombre', 'comer','caminar','correr','programar','tomar','leer', 'llamar','amar']

print(f'Lista de palabras : {lista}\n')
print('Las palabras que empiezan con "a" \n')

for i in lista:
    if 'a' in i[0]:
        print('---',i)


elegir_usuario = input('Escribe la letra a buscar: ')
buscar(lista, elegir_usuario)