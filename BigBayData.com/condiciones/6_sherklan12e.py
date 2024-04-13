# #Calcula sabiendo el valor de una factura cuanto será el precio final para el cliente, sabiendo que…

# Por norma general, el IVA aplicado es de un 21%. Sin embargo, en restaurantes es el 10%.

# Calcular el precio final según IVA aplicado. Pista: Pide al usuario que tipo de factura es.
precio = int(input("Ingrese el precio: "))

print(""" 
    1) iva 
    2) restaurantes 
    
    """)

tipo = int(input("Ingrese el tipo de factura: "))


if tipo == 1:
    precio = precio * 0.21
elif tipo == 2 :
    precio = precio * 0.10
else:
    print("Eso no es un tipo de factura, ! porfavor ingrese el tipo de factura")
