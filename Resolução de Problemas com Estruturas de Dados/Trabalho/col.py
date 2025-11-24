import sys
import networkx as nx

nome_arquivo = sys.argv[1]

G = nx.Graph()

with open(nome_arquivo, 'r') as file:
        for line in file:
            if line.startswith('e '):
                linha = line.strip().split()
                linha.remove('e')
                G.add_node(int(linha[0]))
                G.add_node(int(linha[1]))
                G.add_edge(int(linha[0]), int(linha[1]))
    

def algoritmo_dsatur(G):
    
    graus = list(G.degree())
    vertices_ordenados = sorted(graus, key=lambda item: item[1], reverse=True)
    
    coloracao = {}
    
    cor_atual = 1
    
    nao_coloridos = set(G.nodes())
    
    while nao_coloridos:
        
        vertices_para_colorir = []

        for vertice, _ in vertices_ordenados:
            if vertice in nao_coloridos:

                pode_usar_cor = True

                for vizinho in G.neighbors(vertice):

                    if vizinho in coloracao and coloracao[vizinho] == cor_atual:
                        pode_usar_cor = False
                        break
                
                if pode_usar_cor:
                    coloracao[vertice] = cor_atual
                    vertices_para_colorir.append(vertice)

        nao_coloridos -= set(vertices_para_colorir)

        cor_atual += 1

    return cor_atual - 1


print(algoritmo_dsatur(G))