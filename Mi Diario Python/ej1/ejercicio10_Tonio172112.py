#10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
def procedimiento(lista):
    for i in lista:
        print('*'*i)

mi_lista=[4,9,5]
print(procedimiento(mi_lista))