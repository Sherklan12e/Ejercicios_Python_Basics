bandera = True
count = 0
lista = []
listanew = []
while True == bandera:
    edad = int(input(f'({count+1}) Escribe tu fucking edad :  '))
    
    lista.append(edad)
    count += 1
    if count==10:
        for i in lista:
            if i > 20:
                listanew.append(i)
        
        print('Las personas mayores a 20 son: ')
        for i in range(len(listanew)):
            print(f'persona {lista.index(listanew[i])+1} tiene => {listanew[i]}' )
        bandera = False