"""Resultados principais (do experimento)

Inclinação (regressão log-log) estimada:

list.sort: slope ≈ 1.162, R² ≈ 0.9986

sorted(): slope ≈ 1.203, R² ≈ 0.9984

A razão tempo / (n * log2 n) foi plotada: varia pouco para a parte intermediária dos tamanhos, o que é consistente com comportamento
Θ
(
𝑛
log
⁡
𝑛
)
Θ(nlogn).

Interpretação

Se o tempo médio realmente cresce como
𝑐
⋅
𝑛
log
⁡
𝑛
c⋅nlogn, no gráfico log-log esperamos aproximadamente uma reta com inclinação próxima de 1 (pois
log
⁡
(
𝑛
log
⁡
𝑛
)
=
log
⁡
𝑛
+
log
⁡
log
⁡
𝑛
log(nlogn)=logn+loglogn e
log
⁡
log
⁡
𝑛
loglogn varia lentamente).

As inclinações obtidas (~1.16 e ~1.20) são razoavelmente próximas de 1 — isso, junto ao alto R² e à razão tempo/(n log n) relativamente estável, dá evidência empírica de que o custo médio do algoritmo de ordenação do Python é
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).

Pequena diferença entre list.sort e sorted() é esperada (implementacional / overhead da cópia), mas ambos seguem o mesmo comportamento assintótico.

O que eu rodei (detalhes do experimento)

Tamanhos testados:
𝑛
=
2
8
,
2
9
,
…
,
2
16
n=2
8
,2
9
,…,2
16
 (256 a 65 536).

Repetições: 6 medições por tamanho (média usada).

Medidas: list.sort() (in-place, em cópia) e sorted().

Ajuste: regressão linear em escala log-log para estimar a inclinação (slope).

Plots gerados:

Gráfico log-log de tempo médio vs n (ambos algoritmos).

Gráfico log-log de
tempo
/
(
𝑛
log
⁡
2
𝑛
)
tempo/(nlog
2
	​

n) vs n (para checar se fica aproximadamente constante).

Arquivos / saídas

Mostrei uma tabela interativa com os tempos médios e um resumo da regressão.

Também mostrei os 2 gráficos (log-log e razão)."""