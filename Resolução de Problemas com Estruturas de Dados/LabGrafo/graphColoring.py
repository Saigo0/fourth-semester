import sys
import networkx as nx

def algoritmo_welsh_powell(G):
    """
    Implementa o algoritmo de Welsh e Powell para a coloração de grafos.
    A prioridade de coloração é dada aos vértices com maior grau.
    """
    
    # 1. Ordenação dos Vértices (Critério Principal do Welsh-Powell)
    # Lista de tuplas (nó, grau). Ordena por grau decrescente.
    graus = list(G.degree())
    vertices_ordenados = sorted(graus, key=lambda item: item[1], reverse=True)
    
    # Dicionário para armazenar o resultado da coloração: {vertice: cor_id}
    coloracao = {}
    
    # Inicializa a primeira cor (cor ID 1)
    cor_atual = 1
    
    # Conjunto para rastrear os vértices que ainda não foram coloridos
    nao_coloridos = set(G.nodes())
    
    # 2. Loop Principal (Enquanto houver vértices não coloridos)
    while nao_coloridos:
        
        # 3. Encontra o próximo vértice de maior grau ainda não colorido
        # Como iteramos sobre a lista já ordenada 'vertices_ordenados', 
        # o primeiro nó na lista que ainda não foi colorido é o de maior grau.
        
        # Lista temporária para armazenar os vértices que receberão a 'cor_atual'
        vertices_para_colorir = []
        
        for vertice, _ in vertices_ordenados:
            if vertice in nao_coloridos:
                
                # 4. Verifica a Disponibilidade da Cor
                pode_usar_cor = True
                
                # Verifica os vizinhos
                for vizinho in G.neighbors(vertice):
                    # Se o vizinho já foi colorido E tem a mesma cor atual
                    if vizinho in coloracao and coloracao[vizinho] == cor_atual:
                        pode_usar_cor = False
                        break
                
                # 5. Atribui a Cor e Remove dos Não-Coloridos
                if pode_usar_cor:
                    coloracao[vertice] = cor_atual
                    vertices_para_colorir.append(vertice)
        
        # Remove os vértices que acabaram de ser coloridos do conjunto de não-coloridos
        nao_coloridos -= set(vertices_para_colorir)
        
        # Incrementa a cor para a próxima iteração
        cor_atual += 1
        
    # O número de cores usadas é (cor_atual - 1)
    return len(set(coloracao.values())), coloracao

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python welsh_powell.py <caminho_para_instancia.col>")
        sys.exit(1)

    caminho_instancia = sys.argv[1]
    
    try:
        # Lê a instância DIMACS no formato .col
        G = nx.read_dimacs_color(caminho_instancia)
    except Exception as e:
        print(f"Erro ao ler o grafo: {e}")
        sys.exit(1)

    num_cores, coloracao_final = algoritmo_welsh_powell(G)
    
    print(f"Número de Cores Usadas: {num_cores}")
    
    # Formato de saída: Vertice: Cor
    print("Coloração dos Vértices:")
    for vertice, cor in sorted(coloracao_final.items()):
        print(f"  {vertice}: {cor}")