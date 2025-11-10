def alg5(first, second):
    n = len(first)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range (j + 1):
                total += first[k]
        if second[i] == total:
            count += 1
    return count

#A complexidade assintótica dessa função é O(n^3) (cúbica ou exponencial), visto que, no pior caso, 3 for serão aninhados, gerando uma função do terceiro grau

