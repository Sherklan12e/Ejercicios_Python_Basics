# Escribir un programa que pregunte al usuario una cantidad a invertir,
# 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
