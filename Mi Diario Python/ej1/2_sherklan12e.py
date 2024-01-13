def max_de_tres(num1,num2,num3):
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3
    return mayor


print(max_de_tres(23,3,22))