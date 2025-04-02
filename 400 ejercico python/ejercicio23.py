# 23 Escribir dos funciones que permitan calcular:       La cantidad de 
# segundos en un tiempo dado en horas, minutos y segundos.       La cantidad de horas,
# minutos y segundos de un tiempo dado en segundos.      Escribe un programa principal
# con un menú donde se pueda elegir la opción de convertir a 
# segundos, convertir a horas,minutos y segundos o salir del programa.

def to_seconds(hours, minutes, seconds):
	return hours * 3600 + minutes * 60 + seconds

def from_seconds(total_seconds):
	hours = total_seconds // 3600
	minutes = (total_seconds % 3600) // 60
	seconds = total_seconds % 60
	return hours, minutes, seconds

while True:
	print("\nMenú de conversión:")
	print("1. Convertir a segundos")
	print("2. Convertir de segundos a horas, minutos y segundos")
	print("3. Salir")
	
	option = input("Seleccione una opción (1-3): ")
	
	if option == "1":
		h = int(input("Ingrese las horas: "))
		m = int(input("Ingrese los minutos: "))
		s = int(input("Ingrese los segundos: "))
		print(f"Total en segundos: {to_seconds(h, m, s)}")
	elif option == "2":
		s = int(input("Ingrese el total de segundos: "))
		h, m, s = from_seconds(s)
		print(f"Tiempo: {h} horas, {m} minutos, {s} segundos")
	elif option == "3":
		break
	else:
		print("Opción no válida")