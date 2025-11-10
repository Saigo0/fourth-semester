listaA = [0] * 5
listaB = [0] * 5
listaC = [0] * 10

for i in range(5):
    listaA[i] = i
    listaB[i] = i / 4

for i in range(10):
    if i % 2 == 0:
        listaC[i] = listaA[int(i/2)]
    else:
        listaC[i] = listaB[int(i/2)]


print("Lista A:", listaA)
print("Lista B:", listaB)
print("Lista C:", listaC)