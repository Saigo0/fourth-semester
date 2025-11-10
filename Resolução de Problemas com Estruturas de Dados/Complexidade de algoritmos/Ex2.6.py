def alg2(arr):
    n = len(arr)
    total = 0
    for j in range(0, n, 2):
        total += arr[j]
    return total

#A complexidade assintótica é O(n), pois a única variação que pode ocorrer é em relação ao tamanho do array que entra na função, visto que só há um for na função