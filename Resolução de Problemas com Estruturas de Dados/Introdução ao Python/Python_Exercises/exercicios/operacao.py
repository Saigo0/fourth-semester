n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))

operacao = input("Qual a operação a ser feita: ")
if operacao == "+":
    result = n1 + n2
    print(result)
elif operacao == "-":
    result = n1 - n2
    print(result)
elif operacao == "*":
    result = n1 * n2
    print(result)
elif operacao == "/":
    if n2 != 0:
        result = n1 / n2
        print(result)
    else:
        print("Valor Inválido! Não é possível realizar divisões por zero!")