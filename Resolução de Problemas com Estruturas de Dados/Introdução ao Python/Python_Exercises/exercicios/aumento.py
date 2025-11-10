lista1 = [0] * 5
lista2 = [0] * 5
lista3 = [0] * 5

for i in range(len(lista1)):
    lista2[i] = i * 400
    lista3[i] = i + 2

print(lista2)
print(lista3)

for i in range(len(lista2)):
    if lista2[i] < 2000 and lista3[i] > 5:
        lista2[i] = lista2[i] * 1.35
    elif lista2[i] < 2000:
        lista2[i] = lista2[i] * 1.15
    elif lista3[i] > 5:
        lista2[i] = lista2[i] * 1.27

print(lista2)