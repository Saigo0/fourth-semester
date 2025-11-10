lista = [0] * 5

for i in range(5):
    lista[i] = int(input('Digite um valor: '))

valor = int(input('Digite o valor a ser procurado na lista: '))
posicao = -1
for i in range(5):
    if lista[i] == valor:
        posicao = i
        print("O valor que você digitou foi encontrado na posição", i)
        break

if posicao == -1:
    print("Valor não encontrado")