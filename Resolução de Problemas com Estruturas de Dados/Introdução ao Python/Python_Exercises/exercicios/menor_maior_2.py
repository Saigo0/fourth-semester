mat = [[i+j for j in range(5)] for i in range(1, 25, 5)]

maior = -1
menor = 999

for i in range(5):
    for j in range(5):
        if mat[i][j] > maior:
            maior = mat[i][j]
        if mat[i][j] < menor:
            menor = mat[i][j]
            

print(mat)
print(menor)
print(maior)