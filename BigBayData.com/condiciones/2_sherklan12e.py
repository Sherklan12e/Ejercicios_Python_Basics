edad = int(input('Escribe tu edad: '))

if edad >= 18:
    print('Puedes ingresar!')
elif edad < 18 and edad > 0:
    print('Eres menor de edad')
else:
    print('Esa no esa una edad ')

