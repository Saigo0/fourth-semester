menorQ18 = 0
mediaAltura = 0
percentPeso = 0
for i in range(1,6):
    mediaIdade = 0

    for j in range(1,12):
        idade = int(input(f"Digite a idade do jogador {j} do time {i}"))
        mediaIdade += idade
        if idade < 18:
            menorQ18 += 1
        peso = float(input(f"Digite o peso do jogador {j} do time {i}"))
        if peso > 80:
            percentPeso += 1
        altura = float(input(f"Digite a altura do jogador {j} do time {i}"))
        mediaAltura += altura

    print(f"Média de idade do time {i}: ", mediaIdade)

percentPeso = (percentPeso/55) * 100
print("Média de altura de todos os jogadores: ", mediaAltura)
print("Percentual de jogadores com mais de 80 kg: ", percentPeso)