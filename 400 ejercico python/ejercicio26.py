# 26)Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción 
# vamos a utilizar dos enteros: numerador y denominador.
from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        comun_divisor = gcd(numerador, denominador)
        self.numerador = numerador // comun_divisor
        self.denominador = denominador // comun_divisor

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __sub__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador - otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __mul__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __truediv__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)

# Ejemplo de uso:
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)

suma = fraccion1 + fraccion2
resta = fraccion1 - fraccion2
multiplicacion = fraccion1 * fraccion2
division = fraccion1 / fraccion2

print(f"Fracción 1: {fraccion1}")
print(f"Fracción 2: {fraccion2}")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
