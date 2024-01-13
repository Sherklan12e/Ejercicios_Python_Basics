#4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def is_vocal(car):
    car=car.upper()
    if(car!='A' and car!='E' and car!='I' and car!='O' and car!='U'):
        return False
    else:
        return True
    
print(is_vocal('w'))