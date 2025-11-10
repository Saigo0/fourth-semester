l1 = float(input("Digite o valor do lado 1: "))
l2 = float(input("Digite o valor do lado 2: "))
l3 = float(input("Digite o valor do lado 3: "))

if l1 >= l2 + l3:
    print("Não é possível formar um triângulo!")
elif l2 >= l1 + l3:
    print("Não é possível formar um triângulo!")
elif l3 >= l1 + l2:
    print("Não é possível formar um triângulo!")
else:
    print("Este é um possível triângulo!")



