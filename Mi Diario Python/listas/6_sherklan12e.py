def leer_archivo(arc):
    
    try:
        with open(arc,'r') as file:
            letras = file.read()
            separado = letras.split()
            return separado
    except FileNotFoundError:
        print(f"El archivo '{arc}' no se encontró.")
        return []

nuevalista = leer_archivo('C:/Users/dev/Documents/ejercices/Mi Diario Python/listas/6_sherklan12e.txt')  
print(nuevalista)      