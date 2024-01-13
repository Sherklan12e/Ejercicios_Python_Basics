#7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
def is_palindromo(cad):
    cad=cad.upper().strip()
    if(cad==cad[::-1]):
        return True
    else:
        return False
    
print(is_palindromo("Ana"))