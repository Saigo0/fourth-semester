lista = [0] * 5

for i in range(5):
    if i % 2 == 0:
        lista[i] = -1
    else:
        lista[i] = i

for i in range(5):
    if lista[i] < 0:
        lista[i] = 0

print(lista)