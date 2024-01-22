def eliminar(lista):
    Newlist = []
    del lista[-1]
    del lista[0]
    for i in range(len(lista)):
        
        
        Newlist.append(lista[i])
        
    return Newlist

def media(lista):
    Newlist = []
    del lista[-1]
    del lista[0]
    for i in range(len(lista)):
        
        
        Newlist.append(lista[i])
        
    return Newlist

lista = ['Hola','jugar','correr','caminar','llorar']
print(lista)
print(eliminar(lista))
