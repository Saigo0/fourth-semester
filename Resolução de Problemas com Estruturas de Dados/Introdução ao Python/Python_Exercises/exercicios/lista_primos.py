lista = [3, 5, 7, 9, 11]
lista2 = [0] * 5


for i in range(len(lista2)):
    contaDivs = 0
    divMax = int(lista[i] ** (1 / 2))
    for k in range(2, divMax + 1):
        if lista[i] % k == 0:
            contaDivs += 1
            break

    if contaDivs == 0:
        lista2[i] = lista[i]

print(lista2)


