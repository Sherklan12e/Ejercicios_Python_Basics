import random 
import time 

def iniciar():
    print('WELCOME')
    time.sleep(1)
    print ("Estamos en una tierra llena de dragones. Delante de nuestro,")
    print ("se ven dos cuevas. En una cueva, el dragon es amigable")
    time.sleep(1)
    print ("y compartira el tesoro contigo. El otro dragon")
    print ("es codicioso y hambriento, y te va a comer ni bien te vea.")
    print ("")
    
def cambiar():
    print('1) Cueva 1')
    print('2) Cueva 2')
    opcion = ''
    while opcion !='1' and opcion != '2':
        opcion = input('Elije una opcion')
    
    return opcion

def chequear(cambiars):
    print('Te acercas ala cueva xD')
    time.sleep(1)
    print('o no te caiste')
    print('CTMR haces un ruido de mrd')
    time.sleep(1)
    print('Escuchas algo')
    print('Oh no se acerca')
    time.sleep(1)
    print('Suspenso')
    
    dragon = random.randint(1,2)
    
    if dragon == int(cambiars):
        print('El dragon te da oro y te vas alas cariñosas GAAAAAAAAAAAAAAAAAAAAAAAA')
    elif dragon != cambiar:
        print('Te come el dragon y se roba a tu flaka Daaaaa')
        

comenzar = 'si'

while comenzar == 'si' or comenzar == 's' or comenzar == 'SI' or comenzar == 'S':
    iniciar()
    
    cambiarc = cambiar()
    
    chequear(cambiarc)
    
    print('QUieres jugar AGAIN?? prra')
    
    comenzar = input('WRITE: ')


