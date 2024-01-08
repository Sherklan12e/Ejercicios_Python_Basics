# 14)Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba 
# centrado en pantalla (suponiendo una anchura de 80 columnas;  pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje 
# utilizando el carácter =


def EsribirCentrado(texto):
    anchura = 80
    longitud = len(texto)
    
    
    
def EscribirCentrado(texto):
    # Longitud máxima de la línea (80 columnas)
    longitud_maxima = 80

    # Calcula la longitud del texto
    longitud_texto = len(texto)

    # Calcula la cantidad de espacios antes del texto para centrarlo
    espacios_antes = (longitud_maxima - longitud_texto) // 2

    # Imprime los espacios antes del texto y luego el texto centrado
    print(" " * espacios_antes + texto)

    # Imprime la línea subrayada con '='
    print("=" * longitud_maxima)

# Ejemplo de uso
texto_a_centrar = "Hola, esto está centrffffffffffffffffffffffffffffffffffffffffffado"
EscribirCentrado(texto_a_centrar)
