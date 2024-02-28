class NumerosRomanosPOO:
    def __init__(self, numero):
        self.numero = numero
    
    def convertirromano(self):
        valores_romanos = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

        numeroRomanos = ''
        for valor, simbolo in sorted(valores_romanos.items(), reverse=True):
            while self.numero >= valor:
                numeroRomanos += simbolo
                self.numero -= valor
        return numeroRomanos

roma = 34
converti = NumerosRomanosPOO(roma)
print(converti.convertirromano())
