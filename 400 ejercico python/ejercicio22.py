# 22)Crear una función que calcule el MCD de dos número por el método de Euclides. El método 
# de Euclides es el siguiente: Se divide el número mayor entre el menor. Si la división es exacta, el divisor es el MCD. Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta 
# forma hasta obtener una división exacta, siendo el último divisor el MCD. Crea un programa principal que lea dos números enteros y muestre el MCD
def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        mcd = calcular_mcd(num1, num2)
        print(f"El MCD de {num1} y {num2} es {mcd}")
    except ValueError:
        print("Por favor, introduce números enteros válidos.")

if __name__ == "__main__":
    main()
