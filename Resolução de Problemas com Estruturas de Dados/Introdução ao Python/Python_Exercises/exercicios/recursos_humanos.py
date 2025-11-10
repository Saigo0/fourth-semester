salario = float(input("Digite o salario: "))
print("Menu de opções: ")
print("1: Imposto")
print("2: Novo salário")
print("3: Classificação")
operacao = input("Insira a operação: ")

if operacao == "1":
    if salario < 500:
        print("Imposto:", salario * 0.05)
    elif salario >= 500 and salario < 850:
        print("Imposto:", salario * 0.10)
    else:
        print("Imposto:", salario * 0.15)

if operacao == "2":
    if salario < 450:
        print("Aumento: R$100, novo salário: ", (salario + 100))
    elif salario >= 450 and salario < 750:
        print("Aumento: R$75, novo salário: ", (salario + 75))
    elif salario >= 750 and salario <= 1500:
        print("Aumento: R$50, novo salário: ", (salario + 50))
    else:
        print("Aumento: R$25, novo salário: ", (salario + 25))

if operacao == "3":
    if salario <= 750:
        print("Classificação: mal remunerado")
    else:
        print("CLassificação: bem remunerado")
