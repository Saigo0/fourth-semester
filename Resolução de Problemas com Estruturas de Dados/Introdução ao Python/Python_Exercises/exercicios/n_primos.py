n = int(input("Digite um valor: "))
nLoop = 0
cont = 2
primo = False

while nLoop < n:
    primo = True

    for i in range(2, cont):
        if cont % i == 0:
            primo = False
            break

    if primo:
        print(cont)
        nLoop += 1

    cont += 1