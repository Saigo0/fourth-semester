n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

if n3 > n2 and n2 > n1 and n3 > n1:
    print(n1, n2, n3)
elif n2 > n1 and n1 > n3 and n2 > n3:
    print(n3, n1, n2)
elif n1 > n2 and n2 > n3 and n1 > n3:
    print(n3, n2, n1)
elif n3 > n1 and n2 > n3 and n2 > n1:
    print(n1, n3, n2)
elif n3 > n2 and n1 > n3 and n1 > n2:
    print(n2, n3, n1)
else:
    print(n2, n1, n3)