n1 = int(input("Insira o dividendo: "))
n2 = int(input("Insira o divisor: "))
cont = 0
resto = 0

while n1 > 0:
    n1 = n1 - n2
    cont += 1

if n1 < 0:
    resto = n1 + n2
    cont = cont - 1
print("Resultado: ",cont)
print("Resto: ",resto)