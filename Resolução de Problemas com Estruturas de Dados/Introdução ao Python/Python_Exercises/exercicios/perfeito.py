def perfeito (n):
    divisores = ""
    somaDivisores = 0
    for i in range(1, n):
        if n%i == 0:
            divisores += " " + "[" + str(i) + "]"
            somaDivisores += i

    if somaDivisores == n:
        return f"{n} é um número perfeito! Seus divisores são: {divisores}"
    else:
        return f"{n} não é um número perfeito!"

num = int(input("Digite um número: "))
print(perfeito(num))


