import networkx as nx
import sys

G = nx.Graph()

file_name = sys.argv[1]

def ler_e_atribuir_grafo(nome_arquivo):
    nome_arquivo = nome_arquivo

    with open(nome_arquivo, 'r') as file:
        for line in file:
            if line.startswith('e '):
                linha = line.strip().split()
                linha.remove('e')
                G.add_node(int(linha[0]))
                G.add_node(int(linha[1]))
                G.add_edge(int(linha[0]), int(linha[1]))
    return G


G = ler_e_atribuir_grafo(file_name)
            

"""
Métodos úteis para resolver esse problema:

networkx.read_dimacs_color(caminho_arquivo)	Lê um arquivo de grafo no formato .col (formato DIMACS para problemas de coloração) e retorna um objeto networkx.Graph (grafo não-direcionado).

networkx.Graph()	Cria um objeto de grafo não-direcionado vazio, caso você opte por construir o grafo programaticamente.

G.nodes()Retorna uma visão dos nós (vértices) do grafo G. Você pode converter isso para uma lista ou conjunto, se necessário.

G.neighbors(v)Retorna um iterador sobre os vizinhos do nó (vértice) v no grafo G.

set()Cria um objeto de conjunto (set) vazio. Conjuntos são ideais para armazenar elementos únicos e para operações de pertinência rápida.

C.add(elemento)Adiciona um único elemento ao conjunto C.

C.update(colecao)Adiciona todos os elementos de uma colecao (como uma lista ou outro conjunto) ao conjunto C. Equivalente a uma união (∪).

C.remove(elemento)Remove um elemento do conjunto C. Lança um erro se o elemento não estiver presente.

elemento in C: Operador de pertinência. Retorna True se o elemento estiver no conjunto C, e False caso contrário.

if not C: Avaliação booleana. A forma Pythonica de verificar se um conjunto (C) está vazio. Retorna True se o conjunto for vazio.

"""

def conjunto_dominante_guloso(G):

# 1. C ← V: Inicializa o conjunto de candidatos (vértices que ainda precisam ser dominados)
    # Convertemos os nós para inteiros para garantir que a ordenação funcione corretamente.
    C = set(map(int, G.nodes())) 
    
    # 2. S ← {}: Inicializa o Conjunto Dominante
    S = set()
    
    # O loop continua ENQUANTO C != ∅
    while C:
        
        melhor_vertice = None
        max_ganho = -1
        
        # 3. Estratégia de Seleção (Linhas 4 e Desempate)
        
        # A. Cria uma lista de candidatos ordenados para desempate
        # A regra é: escolher o vértice de menor índice em caso de empate.
        # Ordenamos C numericamente para garantir que o primeiro vértice com o ganho máximo seja o de menor índice.
        candidatos_ordenados = sorted(list(C)) 

        for v in candidatos_ordenados:
            
            # 1. Obtém os vizinhos de v que AINDA NÃO estão dominados (Vizinhos Não-Dominados)
            # set(G.neighbors(v)) retorna os vizinhos. A interseção (&) com C 
            # encontra os vizinhos de v que ainda são 'candidatos' (não dominados).
            vizinhos_nao_dominados = set(map(int, G.neighbors(v))) & C
            
            # 2. Calcula o ganho (número de novos vértices dominados)
            ganho_v = len(vizinhos_nao_dominados)
            
            # 3. Atualiza o melhor_vertice.
            # Se o ganho for estritamente maior (max_ganho < ganho_v), ele é o novo melhor.
            # Se o ganho for igual, a regra de desempate é satisfeita pela iteração sobre 'candidatos_ordenados',
            # garantindo que o vértice de menor índice seja escolhido primeiro.
            if ganho_v > max_ganho:
                max_ganho = ganho_v
                melhor_vertice = v

        # Se nenhum vértice em C contribuir com novos vizinhos (max_ganho == 0), 
        # o melhor_vertice será um nó isolado ou dominado apenas por si mesmo.
        if melhor_vertice is None:
            # Devemos pegar o primeiro (menor índice) de C e parar, pois não haverá mais ganho.
            # Isso é uma situação de tratamento de exceção ou finalização.
            # No algoritmo guloso, se max_ganho for 0, o loop pode estar terminando.
            # Porém, se o algoritmo prosseguir (como na Linha 5), pegamos o menor índice:
            melhor_vertice = candidatos_ordenados[0]
        
        v = melhor_vertice
        
        # 4. S ← S ∪ {v}
        S.add(v)
        
        # 5. Seta v e seus vizinhos como dominados (Removendo-os de C)
        
        # Cria um conjunto dos vértices a serem removidos de C (o próprio v e seus vizinhos)
        cobertos_por_v = set(map(int, G.neighbors(v)))
        cobertos_por_v.add(v)
        
        # C ← C \ Cobertos: Remove todos os vértices dominados do conjunto de candidatos
        C -= cobertos_por_v
        
    # RETORNA S
    return S

# --- EXECUÇÃO E SAÍDA ---
conjunto_final = conjunto_dominante_guloso(G)

# Formatação da saída
tamanho = len(conjunto_final)
# Os elementos devem ser ordenados para corresponder ao formato de saída.
elementos_ordenados = sorted(list(conjunto_final)) 

elementos_str = " ".join(map(str, elementos_ordenados))

print(f"{tamanho} ({elementos_str})")



"""

"""

        
    

