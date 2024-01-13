def es_palindromo(palabra):
    
    if palabra == palabra[::-1]:
        print('Es palindromo ')
        print(True)
    else:
        print('No es palindromo')
        print(False)        
palabra = 'radars'

es_palindromo(palabra)