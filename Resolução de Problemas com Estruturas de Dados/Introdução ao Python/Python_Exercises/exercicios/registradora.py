cod = -1
tot = 0
while cod != 0:
    cod = int(input("Digite o código do produto: "))
    if cod == 0:
        break
    if cod == 4 or (5 < cod < 9) or cod > 9 :
        print("Erro, nenhum produto com este código foi encontrado")
        break
    qtd = int(input("Digite a quantidade do produto: "))
    if cod == 1:
        tot += qtd * 0.5

    if cod == 2:
        tot += qtd * 1

    if cod == 3:
        tot += qtd * 4

    if cod == 5:
        tot += qtd * 7

    if cod == 9:
        tot += qtd * 8

    print("Total até o momento : ", tot)



print("Total: ", tot)
