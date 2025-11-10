def alg3(arr):
    n = len(arr)
    total = 0
    for j in range(n):
        for k in range(j+1):
            total += arr[k]
    return total

#a complexidade assintótica nessa função é O(n^2), visto que há 2 for, um aninhado no outro, o que gera a leitura do vetor uma segunda vez, gerando um função quadrática.

