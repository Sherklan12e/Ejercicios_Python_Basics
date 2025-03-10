# 21)Crear una función recursiva que permita calcular el factorial de un número. Realiza un 
# programa principal donde se lea un entero y se muestre el resultado del factorial.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    num = int(input("Introduce un número entero: "))
    print(f"El factorial de {num} es {factorial(num)}")
    
#Esto es una prueba