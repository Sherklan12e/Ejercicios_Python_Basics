# Imagina que acabas de abrir una nueva cuenta de ahorros
# que te ofrece el 4% de interés al año. Estos ahorros debido 
# a intereses, que no se cobran hasta finales de año, se te 
# añaden al balance final de tu cuenta de ahorros. Escribir un 
# programa que comience leyendo la cantidad de dinero depositada 
# en la cuenta de ahorros, introducida por el usuario. Después el 
# programa debe calcular y mostrar por pantalla la cantidad de 
# ahorros tras el primer, segundo y tercer años. Redondear cada 
# antidad a dos decimales.

inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))