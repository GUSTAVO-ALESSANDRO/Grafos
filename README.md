# TrabalhoGrafosPt1
Este projeto implementa diversas funções para ler dados de instâncias de grafos (em arquivos no formato .dat) e gerar matrizes de pesos para transporte, serviço, demanda e um peso total, considerando arestas e arcos obrigatórios e não obrigatórios.

# Visão Geral
O objetivo principal deste projeto é processar instâncias de grafos provenientes de arquivos formatados com informações como:

- Cabeçalho: Informações gerais do problema (nome, valor ótimo, capacidade, número de veículos, número de nós, etc.).

- Nós obrigatórios: Lista de nós com demanda e custo de serviço.

- Arestas obrigatórias e não obrigatórias: Cada uma com custo de transporte, e para as obrigatórias, também demanda e custo de serviço.

- Arcos obrigatórios e não obrigatórios: Semelhantes às arestas, porém direcionais.

Com base nesses dados, o projeto cria:

- Matriz de transporte (custo de transporte entre os nós);

- Matriz de serviço (custo de serviço, onde aplicável);

- Matriz de demanda (demanda associada à conexão, onde aplicável);

- Matriz de peso total, onde cada entrada é calculada, por padrão, como a soma dos três custos (transporte + serviço + demanda).

Para conexões inexistentes, as matrizes de transporte, serviço e peso total são inicializadas com infinito (float('inf')), mantendo a diagonal com valor zero.

# Estrutura do Projeto
A estrutura principal do projeto é dividida nos seguintes módulos/funções:

- Leitura do Cabeçalho e Dados:
Funções para ler os dados do arquivo .dat e extrair as informações do cabeçalho, nós obrigatórios, arestas (obrigatórias e não obrigatórias) e arcos (obrigatórios e não obrigatórios).

- Criação da Matriz de Adjacência:
Função que gera uma matriz de adjacência (e o respectivo mapeamento dos nós) para representar as conexões entre os vértices.

- Criação das Matrizes de Pesos:
Função que constrói as matrizes de transporte, serviço, demanda e peso total com base nas conexões presentes no grafo, tratando de forma diferenciada as ligações obrigatórias (bidirecionais) e os arcos (unidirecionais).

Exemplo de Execução:
O notebook TrabalhoGrafosPt1.ipynb contém exemplos de como ler o arquivo de instância, processar os dados e gerar as matrizes para posterior análise e aplicação de algoritmos em grafos.

# Instalação
Clone o repositório:
```
git clone https://github.com/GUSTAVO-ALESSANDRO/Grafos.git
cd Grafos
```
