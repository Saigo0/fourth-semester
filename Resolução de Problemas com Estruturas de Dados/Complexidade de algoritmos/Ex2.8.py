def alg4(arr):
    n = len(arr)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += arr[j]
        total += prefix
    return total

#A complexidade assintótica nesse caso é O(n), visto que a única coisa que poderia causar a variação é a leitura do vetor, a qual é feita somente uma vez
