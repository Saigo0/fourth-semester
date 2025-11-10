vel = int(input("Insira o velocidade em km/h: "))

if vel > 80:
    print("Você foi multado em R$",float((vel - 80) * 30), "!")