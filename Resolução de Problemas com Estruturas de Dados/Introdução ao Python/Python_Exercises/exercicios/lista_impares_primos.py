vetor_impares = [0] * 20
aux = 0
for i in range(1,40,2):
    vetor_impares[aux] = i
    aux+=1

print(vetor_impares)

n = 2
vetor_primos = [0] * 20
indice_controle = 0
while vetor_primos[-1] == 0:
    contaDivs = 0
    divMax = int(n**(1/2))
    for i in range(2, divMax + 1):
        if n%i == 0:
            contaDivs += 1
            break

    if contaDivs == 0:
        vetor_primos[indice_controle] = n
        indice_controle += 1
    n += 1

print(vetor_primos)