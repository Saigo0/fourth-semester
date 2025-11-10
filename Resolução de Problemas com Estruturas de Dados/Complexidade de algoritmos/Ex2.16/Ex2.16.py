# Experimento: encontrar o maior n tal que unique1 e unique2 rodem em <= 60 segundos.
# unique1: verificar unicidade por comparação de todos pares -> O(n^2)
# unique2: ordenar e checar vizinhos -> O(n log n) (usa sorted())
# Estratégia: para cada algoritmo, achar limite por crescimento exponencial + busca binária.
# Regras: usamos listas de inteiros distintos (pior caso para unique1) e medições de tempo com time.perf_counter.
# Resultado: tabela com o maior n encontrado e tempos medidos.

import time, random, math, statistics
import pandas as pd
from caas_jupyter_tools import display_dataframe_to_user

# Definição dos algoritmos
def unique1(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] == lst[j]:
                return False
    return True

def unique2(lst):
    # cria cópia (ou sorted retorna nova) e verifica adjacentes
    a = sorted(lst)
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            return False
    return True

# Função para medir tempo com limite (timeout seconds)
def time_run(func, lst, timeout=60.0):
    start = time.perf_counter()
    try:
        res = func(lst)
        dur = time.perf_counter() - start
        # If ran longer than timeout, consider timeout (but we check externally too)
        return dur, res, False
    except Exception as e:
        return None, None, True

# Função para find max n by exponential + binary search
def find_max_n(func, prepare_list_fn, timeout=60.0, n_start=100, n_max_cap=2_000_000_000):
    # exponential phase
    n = n_start
    last_ok = 0
    last_ok_time = None
    last_fail = None
    while True:
        if n > n_max_cap:
            break
        lst = prepare_list_fn(n)
        # run and measure, but ensure we abort if time > timeout by checking after run
        t, res, failed = time_run(func, lst, timeout)
        if failed or t is None:
            last_fail = n
            break
        if t <= timeout:
            last_ok = n
            last_ok_time = t
            # grow
            # choose growth factor smaller for algorithms expected to be O(n^2)
            if func is unique1:
                n = int(n * 2)  # double
            else:
                n = int(n * 4)  # faster growth for unique2
            if n == last_ok:
                n += 1
            continue
        else:
            last_fail = n
            break
    # If never failed (reached cap) return last_ok
    if last_fail is None:
        return last_ok, last_ok_time, None
    
    # binary search between last_ok+1 and last_fail-1 to find max n s.t. time<=timeout
    low = last_ok
    high = last_fail
    while low + 1 < high:
        mid = (low + high) // 2
        lst = prepare_list_fn(mid)
        t, res, failed = time_run(func, lst, timeout)
        if failed or t is None:
            # treat as fail
            high = mid
        elif t <= timeout:
            low = mid
            last_ok_time = t
        else:
            high = mid
    return low, last_ok_time, high

# prepare function: produce worst-case distinct integers (no duplicates)
def prepare_distinct(n):
    # use random.sample but for large n it's expensive; use range shuffled for moderate n
    # For performance, when n is huge, create list(range(n)) and shuffle partially or not shuffle.
    lst = list(range(n))
    # shuffle to avoid best-case ordering for sort; but cost of shuffle is small relative to sort for big n
    random.shuffle(lst)
    return lst

random.seed(1234)

results = []

# Find for unique1 (O(n^2)). Start small.
print("Iniciando busca para unique1 (pode demorar alguns minutos dependendo do ambiente)...")
max_n_u1, time_u1, fail_bound_u1 = find_max_n(unique1, prepare_distinct, timeout=60.0, n_start=128, n_max_cap=200_000)
print(f"unique1: maior n testado que passou em <=60s = {max_n_u1}, tempo ~ {time_u1:.4f}s, fail_bound={fail_bound_u1}")

results.append({"algoritmo":"unique1", "max_n": max_n_u1, "time_s": time_u1, "fail_bound": fail_bound_u1})

# Find for unique2 (O(n log n)). Use larger caps.
print("Iniciando busca para unique2 (pode demorar alguns minutos dependendo do ambiente)...")
max_n_u2, time_u2, fail_bound_u2 = find_max_n(unique2, prepare_distinct, timeout=60.0, n_start=1024, n_max_cap=10_000_000)
print(f"unique2: maior n testado que passou em <=60s = {max_n_u2}, time ~ {time_u2:.4f}s, fail_bound={fail_bound_u2}")

results.append({"algoritmo":"unique2", "max_n": max_n_u2, "time_s": time_u2, "fail_bound": fail_bound_u2})

df = pd.DataFrame(results)
display_dataframe_to_user("Limites n para execução <= 60s (unique1 vs unique2)", df)

# Also provide a bit more detail by attempting one run at max_n and at fail_bound (if exists)
details = []
for r in results:
    algo = unique1 if r["algoritmo"]=="unique1" else unique2
    n_ok = r["max_n"]
    lst_ok = prepare_distinct(n_ok)
    t_ok, _, _ = time_run(algo, lst_ok, timeout=60.0)
    t_fail = None
    if r["fail_bound"] is not None:
        lst_fail = prepare_distinct(r["fail_bound"])
        t_fail, _, _ = time_run(algo, lst_fail, timeout=60.0)
    details.append({"algoritmo": r["algoritmo"], "n_ok": n_ok, "time_ok_s": t_ok, "n_fail_bound": r["fail_bound"], "time_fail_bound_s": t_fail})

details_df = pd.DataFrame(details)
display_dataframe_to_user("Detalhes de verificação", details_df)

df, details_df



