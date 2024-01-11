# 19)Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha 
# función en un programa principal que lea el radio de         una circunferencia y muestre su área y perímetro.


def area_y_perimetro_circulo(radio):
  """
  Calcula el área y el perímetro de una circunferencia.

  Parámetros:
    radio: El radio de la circunferencia.

  Devuelve:
    Un diccionario con las siguientes claves:
      area: El área de la circunferencia.
      perimetro: El perímetro de la circunferencia.
  """

  # Calculamos el área

  area = 3.14159 * radio * radio

  # Calculamos el perímetro

  perimetro = 2 * 3.14159 * radio

  # Devolvemos el resultado

  return {
    "area": area,
    "perimetro": perimetro,
  }
def main():
  """
  Programa principal que lee el radio de una circunferencia y muestra su área y perímetro.
  """

  # Solicitamos el radio

  radio = float(input("Introduce el radio de la circunferencia: "))

  # Calculamos el área y el perímetro

  datos = area_y_perimetro_circulo(radio)

  # Mostramos el resultado

  print(f"El área de la circunferencia es de {(datos["area"])}.")
  print(f"El perímetro de la circunferencia es de {(datos["perimetro"])}.")


if __name__ == "__main__":
  main()

    













