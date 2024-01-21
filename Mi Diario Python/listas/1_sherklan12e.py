def acumulada(n):
    listasuma = []
    count = 0
    for i in n:
        count += i
        listasuma.append(count)
    return listasuma

lista = [1,2,3]
print(acumulada(lista))
