#8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(cad1,cad2):
    for i in range(0,len(cad1)):
        for y in range(0,len(cad2)):
            if(cad1[i]==cad2[y]):
                return True
    return False

cad1="Xd"
cad2="dn"

print(superposicion(cad1,cad2))