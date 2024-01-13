"""Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla."""

current=int(input(" Ingrese el año en curso: "))

n_personas=3
nombres=[]
anos=[]
cumple=[]

for i in range(0,n_personas):
    nombres.append(input(f" Ingrese el nombre de la persona {i+1}: "))
    nombres[i]=nombres[i].strip().capitalize()
    anos.append(int(input(f" Ingrese el año de nacimiento de la persona {i+1}: ")))

for i in range(0,n_personas):
    cumple.append(current-anos[i])
    print(f" {nombres[i]} cumplirá {cumple[i]} en este año {current}")
