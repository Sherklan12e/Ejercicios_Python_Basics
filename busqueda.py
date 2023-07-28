titulo_curso = 'Curso profecional de python'
contador = titulo_curso.count('python')#El count es para saber cuantas veces existe ese algo
print(contador)#resutado 1
print("python" in titulo_curso.lower() ) #resultado True
#lower() pone las letras en minuscula
#upper() poner las letras en mayuscula
#tambien puedes negar con not
print(titulo_curso.startswith("C"))#el metodo starswith es para saber con que enpieza por ejemplo aca empieza con C y dara True
