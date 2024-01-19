bandera = True
banderas = True
count = 0
nombres = []
years = []
while True == bandera:
    while True == banderas:
        try:
            print('=========================')
            year = int(input(f'Write now year user({count +1}): '))
            nombre = input(f'What up write your names pls user({count+1}): ')
            yourOfBirth = int(input(f'year birth user({count+1}): '))
            break
            print('========================')
        except NameError: 
            print('ma')   
        except ValueError:
            print('s')
    
    
    years.append(year-yourOfBirth)
    
    nombres.append(nombre)
    
    count += 1
    if count ==3:
        print('nombre :',nombres[0], 'cumple: ', years[0])
        print('nombre :',nombres[1], 'cumple: ', years[1])
        print('nombre :',nombres[2], 'cumple: ', years[2])
        
        bandera = False
    

