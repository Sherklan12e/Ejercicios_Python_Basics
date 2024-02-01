capital_inicial = float(input("Ingrese el capital inicial (en euros): "))
tasa_interes = float(input("Ingrese la tasa de interés (en porcentaje): "))
ciclos = int(input("Ingrese el número de años o ciclos de inversión: "))


monto_final = capital_inicial * (1 + tasa_interes/100)**ciclos
intereses_ganados = monto_final - capital_inicial


print("\nResultados:")
print(f"Capital inicial: {capital_inicial} euros")
print(f"Tasa de interés: {tasa_interes}%")
print(f"Número de años o ciclos: {ciclos}")
print(f"Monto final después de {ciclos} años: {monto_final:.2f} euros")
print(f"Intereses ganados: {intereses_ganados:.2f} euros")

