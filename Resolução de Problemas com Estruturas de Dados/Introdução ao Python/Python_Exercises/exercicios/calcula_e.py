n = int(input("Digite um valor: "))
e = 1
fat = 1

for i in range(1, n+1):
    fat = i * fat

    e += 1/fat

print(e)