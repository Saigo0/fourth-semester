import sys
import networkx as nx

def heuristica_sahni_gonzalez(G):
    """
    Implementa a heurística gulosa de Sahni-Gonzalez para o Problema do Corte Máximo.
    Atribui cada vértice sequencialmente à partição que maximiza o corte.
    """
    
    # Partições: P1 e P2 (Inicialmente vazias)
    P1 = set()
    P2 = set()
    corte_maximo = 0
    
    # 1. Processa os Vértices em Ordem Sequencial
    # Usa-se a ordem padrão dos nós do networkx
    for v in G.nodes():
        
        # 2. Calcular o Ganho (Contribuição)
        ganho_P1 = 0  # Arestas cruzando o corte se v for para P1
        ganho_P2 = 0  # Arestas cruzando o corte se v for para P2
        
        # Itera sobre os vizinhos para calcular a contribuição
        for vizinho in G.neighbors(v):
            
            # Se o vizinho já está em P1, adicionar 'v' a P2 maximiza o corte
            if vizinho in P1:
                ganho_P2 += 1
            # Se o vizinho já está em P2, adicionar 'v' a P1 maximiza o corte
            elif vizinho in P2:
                ganho_P1 += 1
                
        # 3. Decisão Gulosa: Atribuir à Partição que Oferece o Maior Ganho
        if ganho_P1 >= ganho_P2:
            # Atribui 'v' ao conjunto P1 (Critério de desempate implícito: P1)
            P1.add(v)
            corte_maximo += ganho_P1
        else:
            # Atribui 'v' ao conjunto P2
            P2.add(v)
            corte_maximo += ganho_P2

    return corte_maximo, P1, P2

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python sahni_gonzalez.py <caminho_para_instancia.txt/gml>")
        sys.exit(1)

    caminho_instancia = sys.argv[1]
    
    try:
        # Tenta carregar o grafo (o formato GML é comum para Max-Cut)
        G = nx.read_edgelist(caminho_instancia, create_using=nx.Graph, nodetype=int)
    except Exception as e:
        print(f"Erro ao ler o grafo. Certifique-se de que o formato é compatível (ex: lista de arestas): {e}")
        sys.exit(1)

    corte, particao_1, particao_2 = heuristica_sahni_gonzalez(G)
    
    print(f"Tamanho do Corte Máximo (Aproximado): {corte}")
    print(f"Partição 1 (V1): {sorted(list(particao_1))}")
    print(f"Partição 2 (V2): {sorted(list(particao_2))}")