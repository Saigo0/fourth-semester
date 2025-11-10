vetor = [0] * 10

for i in range(10):
    vetor[i] = int(input('Digite um valor: '))

x = int(input('Digite o primeiro índice a ser somado: '))
y = int(input("Digite o segundo índice a ser somado: "))

print("Resultado da soma: ",vetor[x] + vetor[y])