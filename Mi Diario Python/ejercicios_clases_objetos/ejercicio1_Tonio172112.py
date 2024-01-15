# 1 Escribir una clase en python que convierta un número entero a número romano

class romano:
    numeros=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    letras=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

    resultado=""

    def __init__(self,n=0,r=""):
        self.n=n
        self.r=r
    
    def entero_a_romano(self):
        i=0
        self.resultado=""
        while self.n >0:
            if(self.n//self.numeros[i]):
                self.resultado+=self.letras[i]
                self.n-=self.numeros[i]
            else:
                i+=1
        return self.resultado
    
    def romano_a_entero(self):
        self.resultado=0
        self.r=self.r.upper()
        aux=0
        for i in range(len(self.r)):
            if(self.r[i] in self.letras):
                ind=self.letras.index(self.r[i])
                self.resultado+=self.numeros[ind]
                if(ind<aux):
                    self.resultado-=self.numeros[aux]*2
                aux=ind
            else:
                print(" El numero ingresado no es valido")
                return
        return self.resultado 

nro=romano(925)


print(nro.entero_a_romano())

rom=romano(r="CMXXXXV")

print(rom.romano_a_entero())