# 8 Adivina el número:
# Genera un número aleatorio y pide al usuario que lo adivine.

import random

adivina = int(input("Adivina el numero random: "))
numero = random.randint(0,9)
print(f"Numero random: {numero}")

if adivina == numero:
    print("Adivinaste el numero")
else:
    print("No adivinaste el numero")