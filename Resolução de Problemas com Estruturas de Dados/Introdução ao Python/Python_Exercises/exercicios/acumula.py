lista1 = [0] * 5
lista2 = [0] * 5

for i in range(5):
    lista1[i] = (i + 1) * 4

for i in range(5):
    if i > 0:
        lista2[i] += lista1[i] + lista1[i-1]
    else:
        lista2[i] = lista1[i]

print(lista1)
print(lista2)