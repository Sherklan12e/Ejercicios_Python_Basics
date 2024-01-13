#5 Construir un pequeño programa que convierta números binarios en enteros.

def bin_dec(binario):
    counter=0
    resultado=0
    binario=str(binario)
    binario=binario[::-1]
    for n in binario:
        n=int(n)
        if(n!=1 and n!=0):
            return print(" El numero ingresado no esta en sistema binario, ingrese un numero con 0 y 1")
        if(n==1):
            resultado+=2**counter
        counter+=1
    return resultado
print(bin_dec(1111))