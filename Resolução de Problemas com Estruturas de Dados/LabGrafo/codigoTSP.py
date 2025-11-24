import sys
import numpy as np

def vizinho_mais_proximo(matriz_distancias):
    """
    Resolve o Problema do Caixeiro Viajante (TSP) usando a heurística do Vizinho Mais Próximo.
    
    Args:
        matriz_distancias (numpy.ndarray): Matriz de distâncias onde matriz[i, j] é a distância entre o nó i e o nó j.

    Returns:
        tuple: (custo_total, caminho_percorrido)
    """
    
    # Número total de cidades (vértices)
    num_cidades = matriz_distancias.shape[0]
    
    # 1. Escolha um ponto de partida inicial (Geralmente o nó 0 ou 1, ou um escolhido aleatoriamente)
    # Vamos começar sempre do nó 0 (assumindo que os índices são de 0 a N-1)
    cidade_atual = 0  
    
    # Inicializa a lista de nós visitados com o nó inicial
    caminho = [cidade_atual]
    custo_total = 0
    
    # Conjunto para rastrear quais cidades já foram visitadas (para consultas rápidas)
    visitadas = {cidade_atual}
    
    # O loop continua até que N-1 arestas tenham sido adicionadas (Nós visitados = N)
    while len(caminho) < num_cidades:
        
        # O vizinho mais próximo é inicialmente indefinido
        proximo_vizinho = -1
        distancia_minima = np.inf  # Usamos infinito como distância inicial
        
        # Obtemos a linha da matriz que corresponde à cidade atual
        distancias_da_cidade_atual = matriz_distancias[cidade_atual, :]
        
        # 2. Busca pelo Vizinho Mais Próximo
        # Iteramos por todas as cidades (índices 0 a N-1)
        for proxima_cidade in range(num_cidades):
            
            # Condição de busca:
            # 1. A cidade não pode ser a cidade atual (distância 0)
            # 2. A cidade ainda não pode ter sido visitada
            if proxima_cidade != cidade_atual and proxima_cidade not in visitadas:
                
                distancia = distancias_da_cidade_atual[proxima_cidade]
                
                # 3. Estratégia Gulosa: Encontrar a menor distância
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    proximo_vizinho = proxima_cidade
                    
        # 4. Adicionar o vizinho encontrado ao caminho
        if proximo_vizinho != -1:
            caminho.append(proximo_vizinho)
            visitadas.add(proximo_vizinho)
            custo_total += distancia_minima
            cidade_atual = proximo_vizinho
        else:
            # Não deve ocorrer se o grafo for completo e bem formado
            break
            
    # 5. Fechar o Ciclo (Voltar ao ponto inicial)
    # O ciclo deve retornar do último nó visitado para o nó inicial (0)
    ultima_cidade = caminho[-1]
    distancia_volta = matriz_distancias[ultima_cidade, caminho[0]]
    custo_total += distancia_volta
    caminho.append(caminho[0])
    
    return custo_total, caminho


# --- Lógica de Execução e I/O (Entrada/Saída) ---

if __name__ == "__main__":
    
    # O script espera o caminho do arquivo como o primeiro argumento
    if len(sys.argv) < 2:
        print("Uso: python nome_do_script.py <caminho_para_instancia>")
        sys.exit(1)

    caminho_instancia = sys.argv[1]
    
    try:
        # Assumindo que o arquivo é uma matriz de distâncias legível pelo numpy (ex: formato CSV/TXT com números separados por espaço)
        # Se for um formato TSP mais complexo (ex: .tsp), a leitura deve ser adaptada.
        matriz_distancias = np.loadtxt(caminho_instancia)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_instancia}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler a matriz de distâncias: {e}")
        sys.exit(1)

    # Executa a heurística
    custo, rota = vizinho_mais_proximo(matriz_distancias)
    
    # Formatação da Saída (TSP é geralmente 1-indexado, mas a matriz é 0-indexada. Adicione +1 aos nós para a saída)
    rota_saida = [n + 1 for n in rota]
    
    # Saída no formato: Custo: X, Rota: (A B C D A)
    rota_str = " ".join(map(str, rota_saida))
    print(f"Custo: {int(custo)}, Rota: ({rota_str})")