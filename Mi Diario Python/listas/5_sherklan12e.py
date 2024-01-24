# Ejercicio 5
# Escribe una función llamada "elimina_duplicados" 
# que tome una lista y devuelva una nueva lista con
# los elementos únicos de la lista original. No tienen
# porque estar en el mismo orden.

def eliminar_duplicados(lista):
    listanew = []
    bandera = True
    longitud = len(lista)
    for i in range(longitud):
        
        for j in range(i+1, longitud):
            
            if lista[i] == lista[j]:
                bandera = False
            
            
        if bandera == True:
            listanew.append(lista[i])
            
        else:
            bandera = True
    return listanew

lista = [2,3,34,45,45,4323,42,34,3,2,5,]
print(eliminar_duplicados(lista))