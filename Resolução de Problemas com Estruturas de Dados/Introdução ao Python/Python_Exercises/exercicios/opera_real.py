n = float(input("Digite um número: "))

print("Parte inteira: ", int(n))
print("Parte fracionária: ", n - int(n))
print("Arredondamento para uma casa decimal: ", round(n, 1))
print("Arredondamento para um número inteiro: ", round(n))