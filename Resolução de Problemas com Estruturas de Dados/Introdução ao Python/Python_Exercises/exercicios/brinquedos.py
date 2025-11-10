import math

a = 0
b = 0
c = 0
esf10 = 0
esf15 = 0
esf20 =0
esf25 =0
maiorQ25 = 0

def calc_diag(a,b,c):
    return math.sqrt(a**2 + b**2+c**2)

while True:
    a = float(input("Digite o valor do comprimento da caixa: "))
    b = float(input("Digite o valor da largura da caixa: "))
    c = float(input("Digite o valor da altura da altura: "))
    if a > 0 and b > 0 and c > 0:
        diag = calc_diag(a,b,c)
        if diag <= 10:
            esf10 += 1
            print("Esfera de 10 centímetros adicionada")

        if 10 < diag <= 15:
            esf15 += 1
            print("Esfera de 15 centímetros adicionada")

        if 15 < diag <= 20:
            esf20 += 1
            print("Esfera de 20 centímetros adicionada")

        if 20 < diag <= 25:
            esf25 += 1

        if diag > 25:
            maiorQ25 += 1
    else:
        break

print(f"Esferas de 10 centímetros: {esf10}\nEsferas de 15 centímetros de diâmetro: {esf15}"
      f"\nEsferas de 20 centímetros de diâmetro: {esf20}"
      f"\nEsferas de 25 centímetros de diâmetro: {esf25}"
      f"\nNúmero de caixas com diagonal maior do que a esfera de 25 centímetros de diâmetro: {maiorQ25}")

