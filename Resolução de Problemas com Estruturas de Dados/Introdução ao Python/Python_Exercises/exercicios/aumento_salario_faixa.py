salario = float(input("Insira o valor do salário: "))
if salario > 1250:
    novoSalario = salario * 1.1
    print(novoSalario)
else:
    novoSalario = salario * 1.15
    print(novoSalario)