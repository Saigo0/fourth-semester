from xmlrpc.client import MAXINT


maiorIndice = 0
maiorIndiceCod = ""
menorIndice = MAXINT
menorIndiceCod = ""
media = 0
mediaMq2000 = 0
cont = 0
for i in range (1, 6):

    cod = input("Digite o codigo da cidade " )
    numV = int(input("Digite o numero de veículos de passeio da cidade " ))
    numA = int(input("Digite a quantia de acidentes de trânsito com vítimas: "))
    if numA > maiorIndice:
        maiorIndice = numA
        maiorIndiceCod = cod

    if numA < menorIndice:
        menorIndice = numA
        menorIndiceCod = cod

    media += numV
    if numA < 2000:
        mediaMq2000 += numA
        cont += 1

media = media/5
mediaMq2000 = mediaMq2000/cont

print("Maior índice de acidentes: ", maiorIndice, ", código da cidade: ", maiorIndiceCod)
print("Menor índice de acidentes: ", menorIndice, ", código da cidade: ", menorIndiceCod)
print("Média de veículos nas 5 cidades: ", media)
print("Média de acidentes nas cidades com menos de 2000 veículos", mediaMq2000)
