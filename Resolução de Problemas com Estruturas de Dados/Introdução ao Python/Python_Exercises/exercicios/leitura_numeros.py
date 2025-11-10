num = -1
cont = 0
soma = 0
while num != 0:
    num = int(input("Digite um valor: "))
    if num == 0:
        break
    cont += 1
    soma += num



media = soma / cont
print(cont, "números foram digitados, a soma de todos eles é: ", soma, ", e a média entre eles é de ", media)
