# Guarda una contraseña como password. Crea un sistema de seguridad donde el ordenador muestra un mensaje 'Ordenador bloqueado. Contraseña incorrecta.' si el usuario falla la contraseña. En caso contrario, que muestre por pantalla 'Bienvenid@...'.
useradmin = 'dev'
password = 'thisfuk'
user = input("Ingrese el usuario: ")
ingreso = input("enter the password: ")
if user == useradmin and ingreso == password:
    print("bievenido! " + user)
    
else:
    print( 'Ordenador bloqueado. Contraseña incorrecta.' )