class Calculadora():
    def __init__(self):
        self.valor1 = int(input('Ingrese el numero1: '))
        self.valor2 = int(input('Ingrese el numero2: '))
    def suma(self):
        self.sumar = self.valor1 + self.valor2
        print(self.sumar)
    def restar(self):
        self.rest = self.valor1 - self.valor2
        print(self.rest)
    def multi(self):
        self.multiplicar =  self.valor1 * self.valor2
        print(self.multiplicar)
    def dividir(self):
        self.divi = self.valor1 / self.valor2
        print(self.divi)
        
calculo = Calculadora()

calculo.suma()
calculo.restar()
calculo.multi()
calculo.dividir()