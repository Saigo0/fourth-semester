vetor = [0] * 16

for i in range(len(vetor)):
    vetor[i] = i

if len(vetor) % 2 == 0:
    controleIndice = int(len(vetor) / 2)
else:
    controleIndice = int(len(vetor) / 2 + 1)

for i in range(controleIndice):
    aux = vetor[i]
    vetor[i] = vetor[i+8]
    vetor[i+8] = aux

print(vetor)