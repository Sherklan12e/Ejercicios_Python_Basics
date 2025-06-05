# 33 Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que
# tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que
# devolver True.

def is_palindromo(palabra):
    if (palabra == palabra[::-1]):
        return True
    return False

print(is_palindromo("radas"))  # True