nombre = "eduardo ismael"
apellido = "Garcia"
#nombre_completo =  nombre + " " + apellido
#nombre_completo = 'Mr. %s %s .' %(nombre, apellido) resultado lo mismo
#nombre_completo = 'Mr. {} {} .'.format(nombre, apellido)
nombre_completo = f'Mr {nombre} {apellido} {"Perez"}' 
print(nombre_completo, sep="-" ) #sep="" es par aseparar o como quieres que se separe