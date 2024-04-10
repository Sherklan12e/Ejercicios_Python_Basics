preciofinal = int(input("Ingrese el precio final: "))
carne_descuento = int(input("Ingrese el numero de puntos: "))
if carne_descuento  < 0:
    print("Error igrese el numero bien porfavor ")
else:

    if carne_descuento <= 100:
        preciofinal = preciofinal * 0.10
    elif carne_descuento >100 and carne_descuento <=150:
        preciofinal = preciofinal*0.12
    elif carne_descuento ==150:
        preciofinal = preciofinal * 0.15
    else:
        preciofinal = preciofinal *0.20
print("El precio final con descuento es : ", round(preciofinal))