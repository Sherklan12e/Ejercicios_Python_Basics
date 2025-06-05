# 35) Definir una función generar_n_caracteres() que tome un entero n y devuelva el carácter
# multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(n , caracter):
    resultado = ""
    for _ in range(n):
        resultado += caracter
    return resultado

print(generar_n_caracteres(5, "x"))  # Debería devolver "xxxxx"
print(generar_n_caracteres(3, "a"))  # Debería devolver "aaa"