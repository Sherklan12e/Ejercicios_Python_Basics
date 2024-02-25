def calcular(capital, interes, anos):
    monto = capital *(1+interes/100)** anos
    return monto

capital = float(input('Ingrese la capital: '))
interes = float(input('Ingrese la tasa de interes: '))
anos = int(input('Ingrese la cantidad de years'))

print('La tasa monto final ', calcular(capital,interes,anos))
