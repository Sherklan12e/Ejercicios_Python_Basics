# #try and exept



# try:    
#     edad = int(input('Escribe tu edad: '))
#     print('la edad del usuario es: ')
#     input('ingresa una tecla para continuar....') 
# except KeyboardInterrupt:
#     print('gracias por eso')
# except ValueError:
#     print('Solo enteros plis')
# hola = 'hasdfasdfasdfasdfasd'

def generador_ejemplo():
    yield 1
    yield 2
    yield 3

# Crear un generador
mi_generador = generador_ejemplo()

# Obtener valores del generador
print(next(mi_generador))  # Imprime 1
print(next(mi_generador))  # Imprime 2
print(next(mi_generador))  # Imprime 3
