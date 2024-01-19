#Ejercicio 7
#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

edades = []
for i in range(10):
    edad = int(input("Ingresa una edad: "))
    edades.append(edad)

edades_mayores_a_20 = [edad for edad in edades if edad > 20]

print(f"Edades mayores a 20 años: {edades_mayores_a_20}")