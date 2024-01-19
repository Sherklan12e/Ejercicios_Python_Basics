
#  Escribir un programa que pida al usuario dos números 
#  enteros y muestre por pantalla la <n> entre <m> da un 
#  cociente <c> y un resto <r> donde <n> y <m> son los números
#  introducidos por el usuario, y <c> y <r> son el cociente y 
#  el resto de la división entera respectivamente.


n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))