n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
n3 = int(input("Insira o terceiro valor: "))
n4 = int(input("Insira o quarto valor: "))

if n4 > n1 and n4 < n2:
    print(n1, n4, n2, n3)
elif n4 > n2 and n4 < n3:
    print(n1, n2, n4, n3)
elif n4 < n1:
    print(n4, n1, n2, n3)
else:
    print(n1, n2, n3, n4)