lista = [0] * 15
aux = 0
for i in range(len(lista)):
    lista[i] = i

for i in range(len(lista)):
    if i > 0:
        if lista[i] == 0 and i * (-1) > (len(lista)/2 * (-1)):
            aux = lista[i *(-1)]
            lista[i * (-1)] = 0
            lista[i] = aux
    else:
        aux = lista[-1]
        lista[-1] = 0
        lista[i] = aux

print(lista)