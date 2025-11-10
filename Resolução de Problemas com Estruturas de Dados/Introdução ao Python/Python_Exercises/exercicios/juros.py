import math

montante = float(input('Digite o valor do capital inicial: '))
taxa = float(input('Digite o valor da taxa: '))


for i in range (1, 25):
    montante = montante * (1+taxa)
    print(montante)