# Una juguetería tiene mucho éxito en dos de 
# sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa
# de logística les cobra por peso de cada paquete así que deben calcular el
# peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada 
# payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y
# muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))



