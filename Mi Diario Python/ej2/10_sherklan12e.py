def es_bisiesto(n):
    Bisiesto = False
    if (n % 4 ==0 and n % 100 != 0 ) or n % 400 ==0:
        Bisiesto = True
        
    return Bisiesto

years = int(input('Escribe el year ej(2023): '))

print(es_bisiesto(years))
    