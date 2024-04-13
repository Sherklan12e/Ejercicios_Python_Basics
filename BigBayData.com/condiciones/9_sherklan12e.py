# Partiendo de la tarifa anual (que puede cambiar), nos piden que debemos calcular el precio de la tarifa de nuestro polideportivo, sabiendo las siguientes condiciones:

# Criterio 1: Si es mayor de edad y está trabajando -> Paga el 100% 
# Criterio 2: Si es menor de edad y está trabajando -> Paga el 95% 
# Criterio 3: Si es mayor de edad y no está trabajando -> Paga el 75% 
# Criterio 4: Si es menor de edad y no está trabajando -> Paga el 50%



precio = int(input("Ingrese el precio de la tarifa: "))
edad = int(input("Ingrese su edad porfavor: "))
print("""
      1) Estoy trabajando
      2) No tengo trabajo
      """)
trabaja = int(input("se ecuentra trabajando ?: "))

if edad  > 18 and trabaja ==1:
    precio = precio
    
elif edad < 18 and trabaja == 1:
    precio = precio * 0.95
elif edad > 18 and trabaja == 2:
    precio = precio * 0.75
elif edad < 18 and trabaja == 2:
    precio = precio * 0.50

print("Precio total a pagar: " , precio)