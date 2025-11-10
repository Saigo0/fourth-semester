a1 = int(input("Insira o valor do primeiro ângulo: "))
a2 = int(input("Insira o valor do segundo ângulo: "))
a3 = int(input("Insira o valor do terceiro ângulo: "))

if a1 + a2 + a3 == 180:
    if a1 == a2 and a3 == a1:
        print("Equilátero")
    elif a1 == a2 or a3 == a1 or a3 == a2:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é possível formar um triângulo com esses ângulos! ")
