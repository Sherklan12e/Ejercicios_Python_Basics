# 4 Calculadora de IMC:
# Pide al usuario que ingrese su peso y altura y calcula el Índice de Masa Corporal (IMC).

Peso = float(input("Ingrese su peso en kg: "))
Altura = float(input("Ingrese su altura en mts: "))
Masa_corporal = Peso / Altura ** 2
print(f"Su masa corporal es de: {Masa_corporal}")
