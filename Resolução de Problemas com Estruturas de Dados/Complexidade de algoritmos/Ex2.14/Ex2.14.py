import random
import time
import matplotlib.pyplot as plt
import math

def disjoint1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b and b == c:
                    return False
    return True

def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True

def gera_listas(n):
    A = random.sample(range(n*10), n)
    B = random.sample(range(n*10), n)
    C = random.sample(range(n*10), n)
    return A, B, C


tamanhos = [10, 20, 40, 80, 160, 320]
tempos1 = []
tempos2 = []

for n in tamanhos:
    A, B, C = gera_listas(n)

    inicio = time.perf_counter()
    disjoint1(A, B, C)
    tempos1.append(time.perf_counter() - inicio)

    inicio = time.perf_counter()
    disjoint2(A, B, C)
    tempos2.append(time.perf_counter() - inicio)

plt.figure(figsize=(8,5))
plt.loglog(tamanhos, tempos1, 'o-', label="disjoint1 (O(n³))")
plt.loglog(tamanhos, tempos2, 's-', label="disjoint2 (O(n²))")
plt.xlabel("Tamanho da entrada (n) [escala log]")
plt.ylabel("Tempo de execução (s) [escala log]")
plt.title("Comparação de tempo: disjoint1 vs disjoint2")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()
