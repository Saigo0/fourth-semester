
m =0
n =1

while m < n:
    m = int(input("Digite o primeiro valor do par:"))
    n = int(input("Digite o segundo valor do par:"))
    soma = 0
    for i in range(m, n+1):
        soma += i

    if m < n:
        print("Soma do par: ", soma)
    else:
        print("Programa finalizado")