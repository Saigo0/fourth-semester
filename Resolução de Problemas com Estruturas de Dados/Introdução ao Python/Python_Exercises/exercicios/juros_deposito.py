import math

montante = float(input('Digite o valor do capital inicial: '))
taxa = float(input('Digite o valor da taxa: '))


for i in range(1, 13):
    montante = montante * (1 + taxa)
    capital = float(input('Digite o valor do capital deste mês: '))
    montante += capital
    print("Montante deste mês : ", montante)

print(montante)
