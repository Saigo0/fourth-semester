mat = [[i+j for j in range(5)] for i in range(1, 25, 5)]
mat2 = [[i+j for j in range(5)] for i in range(1, 25, 5)]


somatorio = 0
for i in range(5):
    for j in range(5):
        somatorio += mat[i][j] + mat2[i][j]

print(somatorio)

soma2 = 0
for i in range(1, 26):
    print(i)
    soma2 += i*2
    print(soma2)

print(soma2)