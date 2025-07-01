# game-of-thrones-analysis

Este projeto consiste em uma análise de dados baseada no database de Game Of Thrones. O principal intuito é explorar as relações dos grafos a partir das relações dos personagens, permitindo visualizar a rede em diferentes modos, calcular métricas a partir dos dados e visualizar as distribuições de centralidade de nós.

# Funcionalidades
- Seleção do tipo de visualização da rede:
Permite alternar entre diferentes modos de exibição:
    -  Grafo normal
    - Maior componente conectada
    - Nós com maior grau de conexão

- Cálculo de métricas da rede:
    - Densidade da rede
    - Assortatividade
    - Coeficiente de agrupamento (clustering)
    - Componentes fracamente conectados
    - Verificação se o grafo é direcionado

- Manipulação interativa da visualização (via Streamlit + Pyvis):

    Filtros e ajustes dinâmicos via controles physics do Pyvis, permitindo a personalização da estrutura visual da rede com os seguintes parâmetros:
    - gravitationalConstant
    - centralGravity
    - springLength
    - springConstant
    - damping
    - avoidOverlap
    - maxVelocity
    - minVelocity
    - timestep

- Visualização de centralidade dos nós:
    - Eigenvector centrality
    - Degree centrality
    - Closeness centrality
    - Betweenness centrality

# Estrutura projeto
```
├── analise_GameofThrones.ipynb
├── app.py
├── gameofthrones.html
├── got.py
├── README.md
└── requirements.txt
```

# Como executar o projeto

1. Clone o projeto para sua máquina local.

2. Abra o projeto em uma IDE:

3. Para instalar as dependências, execute:
    ```
    pip install -r requirements.txt
    ```
4. Para rodar a aplicação, execute:
    ```
    streamlit run app.py 
    ```

# Acesso
https://game-of-thrones-analysis-vanessa-maria.streamlit.app/ 