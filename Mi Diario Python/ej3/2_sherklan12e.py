import random

para = False 
lista = ''
while False == para:
    
    while True:
        try:
            print('DEl 2 al 9')
            cadena_long = int(input('Dime la longitud de la cadena: ')) 
            
            if cadena_long > 2 and cadena_long <= 9:
                    break    
        except:
            
            print('Inttroduce un entero!')
                
    for  i in range(1,cadena_long +1):
        while True:
            num = random.randint(1,cadena_long)
            if str(num) in lista:
                continue
            else:
                lista+=str(num)
                break
            
            
    print(lista)
    cout = 0
    while True:
        
        try:
            print('=====================\n')
            print(f'Ingresa  {cadena_long} enteros !adivina!')
            adivina = input('Intenta adivar la cadena: ')
            lista2 = ''
            if len(str(adivina)) == cadena_long:
                
                for i in range(len(lista)):
                    if adivina[i] in lista:
                        lista2 += adivina[i]
                        if adivina[i] == lista[i]:
                            cout += 1
                
                if cout == cadena_long:
                    
                    print(f'Has adivinado los {cadena_long} valores  congratulations!! ')
                    break
                else:
                    print(f'Has adivinado {cout} valores\n')
                    cout = 0
                
            else:
                continue
        except Exception as error:
            print(error)
            print(f'Ingresa {cadena_long} enteros para adivinar')
    break
            
    
    