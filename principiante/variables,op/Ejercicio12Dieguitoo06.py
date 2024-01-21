# 12 Calculadora de descuento:
# Solicita al usuario el precio de un producto y un porcentaje de descuento, luego muestra el precio final.

precio = float(input("Ingresa el precio del producto: "))
descuento = int(input("Ingresa el porcentaje de descuento: "))
precio_final = precio = precio * descuento / 100

print(f"Tu precio final es de {precio_final}")
