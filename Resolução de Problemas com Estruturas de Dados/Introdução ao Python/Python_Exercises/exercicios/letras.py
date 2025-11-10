import string

lista1 = [""] * 5
lista2 = [""] * 5
listaAlfabeto = [""] * 26
listaCont1 = [0] * 26
listaCont2 = [0] * 26
for i in range(26):
    listaAlfabeto[i] = string.ascii_lowercase[i]


for i in range(5):
    lista1[i] = str(input(f"Digite a letra da posição {i} da lista 1: ")).lower()
    letra = lista1[i]
    for j in range(26):
        if listaAlfabeto[j] == letra:
            listaCont1[j] += 1


for i in range(5):
    lista2[i] = str(input(f"Digite a letra da posição {i} da lista 2: ")).lower()
    letra = lista2[i]
    for j in range(26):
        if listaAlfabeto[j] == letra:
            listaCont2[j] += 1





if listaCont1 == listaCont2:
    print("As duas listas possuem o mesmo conteúdo")
else:
    print("As duas listas não possuem o mesmo conteúdo")

