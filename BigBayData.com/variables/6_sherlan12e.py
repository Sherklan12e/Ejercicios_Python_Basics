def calcular_voltaje(intensidad, resistencia):
    voltaje = intensidad * resistencia
    return voltaje

intensidad = 3  
resistencia = 4  


voltaje_calculado = calcular_voltaje(intensidad, resistencia)

print(f"Para una intensidad de {intensidad} amperios y una resistencia de {resistencia} ohmios, el voltaje es de {voltaje_calculado} voltios.")
