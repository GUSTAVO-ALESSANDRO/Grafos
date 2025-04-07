# Função para ler o cabeçalho do arquivo fornecido e retornar os dados como um dicionário
def lerCabecalho(nomeArquivo):
    # Dicionário para armazenar os dados extraídos do arquivo
    cabecalho = {}

    try:
        # Abre o arquivo no modo de leitura (apenas leitura)
        with open(nomeArquivo, "r") as file:
            # Extrai o nome
            cabecalho["Nome"] = file.readline().strip().split("\t\t")[1]
            # Extrai o valor ótimo
            cabecalho["ValorOtimo"] = int(file.readline().strip().split("\t")[1])
            # Extrai a quantidade de veículos disponíveis
            cabecalho["QtdVeiculos"] = int(file.readline().strip().split("\t")[1])
            # Extrai a capacidade máxima dos veículos
            cabecalho["Capacidade"] = int(file.readline().strip().split("\t")[1])
            # Extrai o nó do depósito (ponto de partida e retorno)
            cabecalho["NoDeposito"] = int(file.readline().strip().split("\t")[1])
            # Extrai o número total de nós (vértices)
            cabecalho["Nos"] = int(file.readline().strip().split("\t\t")[1])
            # Extrai o número total de arestas
            cabecalho["Arestas"] = int(file.readline().strip().split("\t\t")[1])
            # Extrai o número total de arcos
            cabecalho["Arcos"] = int(file.readline().strip().split("\t\t")[1])
            # Extrai o número de nós obrigatórios
            cabecalho["NosObrig"] = int(file.readline().strip().split("\t")[1])
            # Extrai o número de arestas obrigatórias
            cabecalho["ArestasObrig"] = int(file.readline().strip().split("\t")[1])
            # Extrai o número de arcos obrigatórios
            cabecalho["ArcosObrig"] = int(file.readline().strip().split("\t")[1])
            #le linha vazia
            file.readline()
    except Exception as e:
        # Exibe uma mensagem genérica de erro
        print(f"Ocorreu um erro inesperado: {e}")

    # Retorna o dicionário com os dados extraídos
    return cabecalho

def lerNosObrigatorios(nomeArquivo, cabecalho):
    # Dicionário para armazenar os dados no formato desejado
    nosObrigatorios = {}

    try:
        # Abre o arquivo no modo leitura
        with open(nomeArquivo, "r") as file:
            # Pula as primeiras 13 linhas (ajuste conforme necessário)
            for i in range(13):
                file.readline()

            # Lê o número de nós obrigatórios definido no cabeçalho
            for i in range(cabecalho["NosObrig"]):
                # Lê uma linha e separa os valores por tabulação
                linha = file.readline().strip().split("\t")
                if len(linha) >= 3:  # Garante que há pelo menos 3 colunas
                    no = linha[0]  # Nome do nó (ex: "N2")
                    demanda = int(linha[1])  # Demanda (convertida para inteiro)
                    custo_servico = int(linha[2])  # Custo de serviço (convertido para inteiro)
                    # Adiciona ao dicionário no formato desejado
                    nosObrigatorios[no] = {"Demand": demanda, "Service Cost": custo_servico}
                else:
                    print(f"Erro: Linha inválida - {linha}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # Retorna o dicionário com os dados extraídos
    return nosObrigatorios

def lerArestasObrigatorias(nomeArquivo, cabecalho):
    # Lista para armazenar as arestas obrigatórias no formato desejado
    arestasObrigatorias = []

    try:
        # Abre o arquivo no modo leitura
        with open(nomeArquivo, "r") as file:
            # Pula as primeiras 13 linhas (ou ajuste conforme necessário para chegar até a seção ReE)
            for i in range(15 + cabecalho["NosObrig"]):
                file.readline()

            # Lê o número de arestas obrigatórias definido no cabeçalho
            for i in range(cabecalho["ArestasObrig"]):  # Exemplo: {"ArestasObrig": 3}
                # Lê uma linha da seção ReE e separa os valores
                linha = file.readline().strip().split("\t")
                aresta = {
                    "Name": linha[0],                 # Nome da aresta (ex: "E3")
                    "From": f"N{linha[1]}",           # Nó de origem
                    "To": f"N{linha[2]}",             # Nó de destino
                    "Transport Cost": int(linha[3]),  # Custo de transporte
                    "Demand": int(linha[4]),          # Demanda
                    "Service Cost": int(linha[5])     # Custo de serviço
                }
                arestasObrigatorias.append(aresta)  # Adiciona a aresta à lista

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # Retorna a lista com as arestas obrigatórias
    return arestasObrigatorias

def lerArestasNaoObrigatorias(nomeArquivo, cabecalho):
    # Lista para armazenar as arestas não obrigatórias no formato desejado
    arestasNaoObrigatorias = []

    try:
        # Abre o arquivo no modo leitura
        with open(nomeArquivo, "r") as file:
            # Pula as primeiras 13 linhas (ou ajuste conforme necessário para chegar à seção EDGE)
            for i in range(17 + cabecalho["NosObrig"] + cabecalho["ArestasObrig"]):
                file.readline()

            # Lê o número de arestas não obrigatórias definido no cabeçalho
            for i in range(cabecalho["Arestas"] - cabecalho["ArestasObrig"]):  # Exemplo: {"ArestasNaoObrig": 2}
                # Lê uma linha da seção EDGE e separa os valores
                linha = file.readline().strip().split("\t")
                if len(linha) >= 4:  # Garante que há pelo menos 4 colunas
                    aresta = {
                        "Name": linha[0],                 # Nome da aresta (ex: "NrE1")
                        "From": f"N{linha[1]}",           # Nó de origem
                        "To": f"N{linha[2]}",             # Nó de destino
                        "Transport Cost": int(linha[3])   # Custo de transporte
                    }
                    arestasNaoObrigatorias.append(aresta)  # Adiciona a aresta à lista
                else:
                    print(f"Erro: Linha inválida - {linha}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # Retorna a lista com as arestas não obrigatórias
    return arestasNaoObrigatorias

def lerArcosObrigatorios(nomeArquivo, cabecalho):
    # Lista para armazenar os arcos obrigatórios no formato desejado
    arcosObrigatorios = []

    try:
        # Abre o arquivo no modo leitura
        with open(nomeArquivo, "r") as file:
            # Pula as primeiras linhas até chegar à seção ReA
            for i in range(19 + cabecalho["NosObrig"] + cabecalho["ArestasObrig"] +
                           (cabecalho["Arestas"] - cabecalho["ArestasObrig"])):  # Ajuste conforme necessário
                file.readline()

            # Lê o número de arcos obrigatórios definido no cabeçalho
            for i in range(cabecalho["ArcosObrig"]):  # Exemplo: {"ArcosObrig": 12}
                # Lê uma linha da seção ReA e separa os valores
                linha = file.readline().strip().split("\t")
                arco = {
                    "Name": linha[0],                 # Nome do arco (ex: "A6")
                    "From": f"N{linha[1]}",           # Nó de origem
                    "To": f"N{linha[2]}",             # Nó de destino
                    "Transport Cost": int(linha[3]),  # Custo de transporte
                    "Demand": int(linha[4]),          # Demanda
                    "Service Cost": int(linha[5])     # Custo de serviço
                }
                arcosObrigatorios.append(arco)  # Adiciona o arco à lista
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # Retorna a lista com os arcos obrigatórios
    return arcosObrigatorios

def lerArcosNaoObrigatorios(nomeArquivo, cabecalho):
    # Lista para armazenar os arcos não obrigatórios no formato desejado
    arcosNaoObrigatorios = []

    try:
        # Abre o arquivo no modo leitura
        with open(nomeArquivo, "r") as file:
            # Pula as primeiras linhas até chegar à seção ARC
            for i in range(21 + cabecalho["NosObrig"] + cabecalho["ArestasObrig"] +
                           (cabecalho["Arestas"] - cabecalho["ArestasObrig"]) + cabecalho["ArcosObrig"]):  # Ajuste conforme necessário para chegar ao início da seção ARC
                file.readline()

            # Lê o número de arcos não obrigatórios definido no cabeçalho
            for i in range(cabecalho["Arcos"] - cabecalho["ArcosObrig"]):  # Exemplo: {"ArcosNaoObrig": 18}
                # Lê uma linha da seção ARC e separa os valores
                linha = file.readline().strip().split("\t")
                arco = {
                    "Name": linha[0],                 # Nome do arco (ex: "NrA1")
                    "From": f"N{linha[1]}",           # Nó de origem
                    "To": f"N{linha[2]}",             # Nó de destino
                    "Transport Cost": int(linha[3])   # Custo de transporte
                }
                arcosNaoObrigatorios.append(arco)  # Adiciona o arco à lista

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # Retorna a lista com os arcos não obrigatórios
    return arcosNaoObrigatorios

def criar_matriz_adjacencia(nosObrig, arestasObrig, arestasNaoObrig, arcosObrig, arcosNaoObrig):
    # Criar um conjunto para armazenar todos os números de nós encontrados
    nos = set()

    # Adicionar os números dos nós obrigatórios
    for no in nosObrig.keys():
        numero_do_no = int(no[1:])  # Remove o "N" e pega o número do nó
        nos.add(numero_do_no)

    # Função auxiliar para adicionar nós de uma ligação (aresta ou arco)
    def adicionar_nos_ligacao(ligacao):
        # Usamos as chaves "From" e "To", conforme os dados fornecidos
        nos.add(int(ligacao["From"][1:]))
        nos.add(int(ligacao["To"][1:]))

    # Adicionar nós das arestas obrigatórias e não obrigatórias
    for aresta in arestasObrig:
        adicionar_nos_ligacao(aresta)
    for aresta in arestasNaoObrig:
        adicionar_nos_ligacao(aresta)

    # Adicionar nós dos arcos obrigatórios e não obrigatórios
    for arco in arcosObrig:
        adicionar_nos_ligacao(arco)
    for arco in arcosNaoObrig:
        adicionar_nos_ligacao(arco)

    # Determinar o maior número de nó. Caso não existam nós, definir como 0
    if len(nos) > 0:
        numero_maximo_de_nos = max(nos)
    else:
        numero_maximo_de_nos = 0

    # Criar a matriz de adjacência, preenchendo com 0
    matriz = []
    for i in range(numero_maximo_de_nos):
        linha = [0] * numero_maximo_de_nos  # Cria uma linha com zeros
        matriz.append(linha)

    # Criar o mapeamento de nomes dos nós (ex.: "N1") para índices na matriz
    mapeamento = {}
    contador = 0
    for i in range(1, numero_maximo_de_nos + 1):
        mapeamento[f"N{i}"] = contador
        contador += 1

    # Função auxiliar para adicionar uma conexão na matriz
    def adicionar_conexao(origem, destino, nome, bidirecional=True):
        matriz[mapeamento[origem]][mapeamento[destino]] = nome  # Adiciona o valor à matriz
        if bidirecional:
            matriz[mapeamento[destino]][mapeamento[origem]] = nome  # Se for bidirecional, adiciona no outro sentido

    # Adicionar as arestas obrigatórias (bidirecionais)
    for aresta in arestasObrig:
        adicionar_conexao(aresta["From"], aresta["To"], aresta["Name"], bidirecional=True)

    # Adicionar as arestas não obrigatórias (bidirecionais)
    for aresta in arestasNaoObrig:
        adicionar_conexao(aresta["From"], aresta["To"], aresta["Name"], bidirecional=True)

    # Adicionar os arcos obrigatórios (direcionados)
    for arco in arcosObrig:
        adicionar_conexao(arco["From"], arco["To"], arco["Name"], bidirecional=False)

    # Adicionar os arcos não obrigatórios (direcionados)
    for arco in arcosNaoObrig:
        adicionar_conexao(arco["From"], arco["To"], arco["Name"], bidirecional=False)

    # Retorna a matriz de adjacência e o mapeamento de nós
    return matriz, mapeamento

def qtdVertices(cabecalho):
    return cabecalho["Nos"]

def qtdArestas(cabecalho):
    return cabecalho["Arestas"]

def qtdArcos(cabecalho):
    return cabecalho["Arcos"]

def qtdVerticesObrig(cabecalho):
    return cabecalho["NosObrig"]

def qtdArestasObrig(cabecalho):
    return cabecalho["ArestasObrig"]

def qtdArcosObrig(cabecalho):
    return cabecalho["ArcosObrig"]

def calcular_densidade(qtd_vertices, qtd_arestas, qtd_arcos):
    # Caso especial: se não houver vértices ou apenas 1 vértice, densidade é 0
    if qtd_vertices <= 1:
        return 0

    # Fórmula para grafos mistos
    max_conexoes = qtd_vertices * (qtd_vertices - 1)  # Conexões possíveis
    conexoes_totais = (qtd_arestas * 2) + qtd_arcos  # Conexões no grafo
    densidade = conexoes_totais / max_conexoes
    return densidade


def componentes_conectados(matriz, mapeamento):
    # Número de nós no grafo
    n = len(matriz)

    # Lista para saber quais nós já foram visitados
    visitado = [False] * n

    # Lista para armazenar os componentes
    componentes = []

    # Cria um mapeamento inverso para converter índice em nome do nó
    indices_para_nomes = {}
    for k, v in mapeamento.items():
        indices_para_nomes[v] = k

    # Função auxiliar para a DFS
    def dfs(no_atual, componente):
        visitado[no_atual] = True
        componente.append(indices_para_nomes[no_atual])  # Adiciona o nó ao componente

        # Percorre todos os vizinhos
        for vizinho in range(n):
            # Considera ligação apenas na direção especificada (arcos são direcionados)
            if matriz[no_atual][vizinho] != 0 and not visitado[vizinho]:
                dfs(vizinho, componente)

    # Percorre todos os nós
    for no in range(n):
        if not visitado[no]:
            # Novo componente conectado
            componente = []
            dfs(no, componente)
            componentes.append(componente)

    return componentes


def calcular_graus(matriz, mapeamento):
    """
    Calcula o grau total (considerando entrada e saída) de cada nó.
    Para cada linha, processa as conexões que saem, e para cada coluna, processa as conexões que chegam.
    Usa um conjunto (set) para evitar contagens duplicadas, armazenando os nomes das conexões.
    """
    n = len(matriz)
    graus_totais = {}  # Dicionário para armazenar o grau total de cada nó

    # Inverte o mapeamento para obter o nome do nó a partir do índice
    indices_para_nomes = {}
    for nome, indice in mapeamento.items():
        indices_para_nomes[indice] = nome

    # Para cada nó, calcula o grau total
    for i in range(n):
        conexoes_unicas = set()  # Estrutura que armazena nomes únicos das conexões

        # Percorre a linha (ligações que saem do nó i)
        for j in range(n):
            if matriz[i][j] != 0:  # Existe uma conexão de i para j
                conexoes_unicas.add(matriz[i][j])  # Armazena o valor da conexão (ex.: "NrA2")

        # Percorre a coluna (ligações que chegam ao nó i)
        for j in range(n):
            if matriz[j][i] != 0:  # Existe uma conexão de j para i
                conexoes_unicas.add(matriz[j][i])  # Armazena o valor da conexão (ex.: "NrA1")

        # O grau total é o tamanho do conjunto de conexões únicas
        graus_totais[indices_para_nomes[i]] = len(conexoes_unicas)

    return graus_totais


def calcular_grau_minimo(graus):
    """
    Retorna o menor grau entre os vértices.
    """
    if not graus:  # Se não houver vértices
        return 0
    return min(graus.values())


def calcular_grau_maximo(graus):
    """
    Retorna o maior grau entre os vértices.
    """
    if not graus:  # Se não houver vértices
        return 0
    return max(graus.values())

def matriz_pesos(cabecalho, arestasObrig, arestasNaoObrig, arcosObrig, arcosNaoObrig):
    """
    Cria a matriz de pesos para o grafo com base nos dados fornecidos.
    A matriz representa o custo de transporte entre os nós, usando infinito para ausência de conexão.
    """
    # Número de nós no grafo
    n = cabecalho["Nos"]

    # Inicializa a matriz com infinito em todas as posições
    matriz_pesos = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:  # Custo da diagonal é 0 (do nó para si mesmo)
                linha.append(0)
            else:
                linha.append(float('inf'))  # Ausência de conexão
        matriz_pesos.append(linha)

    # Função auxiliar para inserir pesos na matriz
    def inserir_peso(from_node, to_node, custo, bidirecional=True):
        i = int(from_node[1:]) - 1  # Converte "N1" para índice 0
        j = int(to_node[1:]) - 1  # Converte "N2" para índice 1
        matriz_pesos[i][j] = custo
        if bidirecional:
            matriz_pesos[j][i] = custo  # Insere peso na direção oposta

    # Insere pesos de arestas obrigatórias (bidirecionais)
    for aresta in arestasObrig:
        inserir_peso(aresta["From"], aresta["To"], aresta["Transport Cost"], bidirecional=True)

    # Insere pesos de arestas não obrigatórias (bidirecionais)
    for aresta in arestasNaoObrig:
        inserir_peso(aresta["From"], aresta["To"], aresta["Transport Cost"], bidirecional=True)

    # Insere pesos de arcos obrigatórios (direcionais)
    for arco in arcosObrig:
        inserir_peso(arco["From"], arco["To"], arco["Transport Cost"], bidirecional=False)

    # Insere pesos de arcos não obrigatórios (direcionais)
    for arco in arcosNaoObrig:
        inserir_peso(arco["From"], arco["To"], arco["Transport Cost"], bidirecional=False)

    return matriz_pesos

def floyd_warshall(matriz_pesos):
    """
    Calcula os caminhos mínimos entre todos os pares de vértices usando o algoritmo de Floyd-Warshall.
    Versão simples e amadora.
    """
    # Número de nós no grafo
    n = len(matriz_pesos)

    # Inicializa a matriz de distâncias copiando a matriz de pesos
    dist = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(matriz_pesos[i][j])  # Copia os valores da matriz de pesos
        dist.append(linha)

    # Inicializa a matriz de predecessores com None
    pred = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i != j and matriz_pesos[i][j] != float('inf'):  # Conexão direta existe
                linha.append(i)  # Predecessor inicial é o nó de origem
            else:
                linha.append(None)  # Sem predecessor
        pred.append(linha)

    # Aplica o algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Se passar por k melhora o caminho, atualiza a distância e o predecessor
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred

def calcular_caminho_medio(dist):
    """
    Calcula o comprimento médio dos caminhos mínimos entre todos os pares de vértices.
    """
    n = len(dist)
    soma = 0
    cont = 0

    # Percorre cada par de nós i, j
    for i in range(n):
        for j in range(n):
            # Ignora caminhos inválidos (diagonal ou infinitos)
            if i != j and dist[i][j] != float('inf'):
                soma += dist[i][j]
                cont += 1

    # Calcula a média apenas se cont > 0
    if cont > 0:
        return soma / cont
    else:
        return 0

def calcular_diametro(dist):
    """
    Calcula o diâmetro do grafo, ou seja, o maior caminho mínimo entre dois nós conectados.
    """
    n = len(dist)
    diametro = 0  # Começa assumindo que o diâmetro é zero

    # Percorre todos os pares de nós (i, j)
    for i in range(n):
        for j in range(n):
            # Ignora caminhos inválidos (distância infinita)
            if dist[i][j] != float('inf') and dist[i][j] > diametro:
                diametro = dist[i][j]  # Atualiza o diâmetro com o maior valor encontrado

    return diametro


def reconstruir_caminho(i, j, pred):
    """
    Reconstrói o caminho mínimo de i a j usando a matriz de predecessores.
    Retorna uma lista com os índices do caminho, ou lista vazia se não houver caminho.
    """
    caminho = []  # Lista para armazenar o caminho

    if pred[i][j] is None:  # Se não há caminho entre i e j
        return caminho

    atual = j  # Começa pelo nó de destino
    while atual != i:  # Continua até chegar ao nó de origem
        caminho.append(atual)  # Adiciona o nó atual ao caminho
        atual = pred[i][atual]  # Move para o predecessor
        if atual is None:  # Se não houver predecessor válido
            return []  # Caminho não é válido

    caminho.append(i)  # Adiciona o nó de origem ao final
    caminho.reverse()  # Inverte para que o caminho fique da origem ao destino
    return caminho

def calcular_betweenness(pred):
    """
    Calcula a centralidade de intermediação (betweenness) para cada vértice.
    """
    n = len(pred)  # Número de nós no grafo
    betweenness = [0] * n  # Inicializa intermediação como 0 para todos os nós

    # Para cada par de nós (i, j)
    for i in range(n):
        for j in range(n):
            if i != j:  # Evita calcular caminhos de um nó para ele mesmo
                caminho = reconstruir_caminho(i, j, pred)  # Reconstrói o caminho mínimo
                if len(caminho) > 2:  # Só conta se houver nós intermediários
                    for v in caminho[1:-1]:  # Considera apenas os nós intermediários
                        betweenness[v] += 1  # Incrementa a contagem para o nó intermediário

    return betweenness


# Solicita ao usuário o nome do arquivo que deseja processar
print("Digite o nome e extensão do arquivo")
print("Ex: Arquivo_Teste.txt")

# Lê o nome do arquivo digitado pelo usuário
nomeArquivo = input("Digite: ")

# Chama a função para ler o cabeçalho do arquivo fornecido
cabecalho = lerCabecalho(nomeArquivo)
print(cabecalho)

nosObrig = lerNosObrigatorios(nomeArquivo, cabecalho)
print(nosObrig)

arestasObrig = lerArestasObrigatorias(nomeArquivo, cabecalho)
print(arestasObrig)

arestasNaoObgrig = lerArestasNaoObrigatorias(nomeArquivo, cabecalho)
print(arestasNaoObgrig)

arcosObrig = lerArcosObrigatorios(nomeArquivo, cabecalho)
print(arcosObrig)

arcosNaoObrig = lerArcosNaoObrigatorios(nomeArquivo, cabecalho)
print(arcosNaoObrig)

matriz, mapeamento = criar_matriz_adjacencia(nosObrig, arestasObrig, arestasNaoObgrig, arcosObrig, arcosNaoObrig)
for linha in matriz:
        print(linha)
print(mapeamento)

print(qtdVertices(cabecalho))

print(qtdArestas(cabecalho))

print(qtdArcos(cabecalho))

print(qtdVerticesObrig(cabecalho))

print(qtdArestasObrig(cabecalho))

print(qtdArcosObrig(cabecalho))

print(calcular_densidade(qtdVertices(cabecalho), qtdArestas(cabecalho), qtdArcos(cabecalho)))

componentes = componentes_conectados(matriz, mapeamento)
print(componentes)

graus = calcular_graus(matriz, mapeamento)
print(graus)

grauMax = calcular_grau_maximo(graus)
print(grauMax)

grauMin = calcular_grau_minimo(graus)
print(grauMin)

matrizDePesos = matriz_pesos(cabecalho, arestasObrig, arestasNaoObgrig, arcosObrig, arcosNaoObrig)
print(matrizDePesos)

dist, pred = floyd_warshall(matrizDePesos)
print(dist)
print(pred)

caminhoMedio = calcular_caminho_medio(dist)
print(caminhoMedio)

diametro = calcular_diametro(dist)
print(diametro)

betweenness = calcular_betweenness(pred)
print(betweenness)