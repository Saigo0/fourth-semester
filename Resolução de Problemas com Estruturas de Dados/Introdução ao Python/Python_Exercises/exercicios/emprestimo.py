valor = float(input("Qual o valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = float(input("Quantos anos de financiamento: "))
prestacao = valor / (anos * 12)

if(prestacao > salario * 0.3):
    print("Emprestimo não pode ser concedido!")
else:
    print("Emprestimo pode ser concedido!")
    print("Valor da prestação: ", prestacao)
