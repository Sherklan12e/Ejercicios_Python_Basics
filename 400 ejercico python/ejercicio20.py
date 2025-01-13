# 20)Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y 
# te devuelve Verdadero si el nombre de usuario es “usuario1”      y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado 
# hacer login y si no se ha podido hacer login incremente este valor.      Crear un programa principal donde se pida un nombre de usuario y una contraseña y se 
# intente hacer login, solamente tenemos tres oportunidades       para intentarlo
def Login(username , password , attempts):
    if username == "useruario1" and password == "asdaasd":
        return True

    return False, attempts + 1

def main():
    max_attempts = 3
    attempts = 0 

    while attempts < max_attempts:
        username = input("Ingrese su nombre: ")
        password = input("Ingrese su contraseña: ")

        success, attempts = Login(username,password, attempts)
        if success:
            print("Logeado con exito")
            break
        else:
            remaining = max_attempts - attempts
            print(f"error , {remaining} intentos restantes")
    if attempts >= max_attempts:
        print("Te pasaste de intentos")

if __name__ == '__main__':
    main()