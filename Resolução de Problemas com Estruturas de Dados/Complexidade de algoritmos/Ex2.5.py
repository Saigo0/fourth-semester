def alg1(arr):
    n = len(arr)
    total = 0
    for j in range(n):
        total += arr [j]
    return total

#O(n), pois a única variação que pode ocorrer é por conta do tamanho do array que entra na função (possui apenas um for.)
