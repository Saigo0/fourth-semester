"""O que fiz (resumo do método)

Não tentei forçar unique1 com n muito grande (isso levaria muito tempo). Em vez disso:

medi tempos empíricos para séries de tamanhos moderados (várias repetições para reduzir ruído);

ajustei modelos simples baseados na complexidade teórica:

unique1(n) ≈ c * n²

unique2(n) ≈ c * n · log₂ n

estimei a constante c por ajuste linear (y ≈ c·x) usando os dados medidos;

resolvi numericamente c · f(n) = 60s para encontrar n máximo estimado.

Dados amostrados (mostrados como tabelas interativas)

Tamanhos testados e tempos médios usados para ajuste:

unique1 medido em n = 100, 200, 400, 800, 1600, 3200.

unique2 medido em n = 1024, 2048, 4096, 8192, 16384, 32768.

(As tabelas detalhadas foram exibidas na execução.)

Resultados (estimativas)

unique1 (algoritmo ingênuo O(n²))

Estimativa da constante:
𝑐
≈
2.230
×
10
−
8
c≈2.230×10
−8

n máximo estimado tal que o algoritmo roda em ≤ 60 s: ≈ 51 875

unique2 (ordenar + checar adjacentes, O(n log n))

Estimativa da constante:
𝑐
≈
3.162
×
10
−
8
c≈3.162×10
−8

n máximo estimado tal que o algoritmo roda em ≤ 60 s: ≈ 72 671 249

Observação: os valores acima são estimações baseadas no ambiente onde o experimento rodou (CPU, carga, Python, implementação de sorted, etc.). Em outra máquina os números podem variar bastante.

Como interpretar

unique1 escala como
𝑛
2
n
2
. Assim, aumentar n por um fator 10 aumenta o tempo por ~100× — por isso seu limite n para 60 s é relativamente pequeno (~5·10^4).

unique2 usa ordenação (Timsort em CPython) e escala ~
𝑛
log
⁡
𝑛
nlogn, permitindo atingir n muito maiores para o mesmo limite de tempo (ordens de magnitude maiores: ~7·10^7).

Se quiser avançar

Escolha uma das opções:

Verificação prática: tento executar unique1 em n = 50{,}000 e unique2 em n = 72{,}671{,}249 para confirmar — aviso: a execução de unique2 nessa magnitude pode consumir muita memória (lista de 72M inteiros) e pode falhar aqui; unique1 em ~50k também é demorado. Posso testar valores mais baixos de verificação (ex.: unique1 em 30k e unique2 em 5M).

Aumentar a precisão: medir mais pontos e mais repetições para refinar c e reduzir erro.

Gerar relatório completo (com gráficos, tabelas e explicação) em PDF ou PPTX para anexar ao trabalho.

Rodar o experimento no seu computador: eu preparo um script pronto (com instruções) para você rodar localmente — recomendado para confirmar os números no seu ambiente."""