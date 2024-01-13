#6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
cadena="Hola como estas"
    # primera forma

def inversa(cad):
    return cad[::-1]
print(inversa(cadena))

    # segunda forma

def invers(cad):
    resultado=""
    for i in range(len(cad)-1,0-1,-1):
        resultado+=cad[i]
    return resultado
print(invers(cadena))