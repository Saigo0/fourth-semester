classe = "A"
hrsAula = 0
salBruto = 0
salLiquido = 0
while classe == "A" or classe == "B":

    if classe == "A" or classe == "B":
        classe = input("Digite a classe (A ou B): ")
        hrsAula = float(input("Digite o número de horas/aula dadas mensalmente: "))
        if classe == "A":
            salBruto = hrsAula * 146
            salLiquido = salBruto * 0.9
            print("Salário bruto classe A: ", salBruto)
            print("Salário liquido classe A: ", salLiquido)
        else:
            salBruto = hrsAula * 146
            salLiquido = salBruto * 0.95
            print("Salário bruto classe B: ", salBruto)
            print("Salário liquido classe B: ", salLiquido)
    else:
        print("Programa finalizado!")
