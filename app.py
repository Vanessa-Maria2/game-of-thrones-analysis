import streamlit as st
import streamlit.components.v1 as components
import got 

st.title('Game of Thrones')

data = got.graph_full('https://raw.githubusercontent.com/pupimvictor/NetworkOfThrones/master/stormofswords.csv')
option = st.selectbox("Escolha um subconjunto do grafo:", ["Grafo", "Maior componente conectada", "Nó com alto grau"])

if option == "Grafo":
    selected_graph = data
elif option == "Maior componente conectada":
    selected_graph = got.get_largest_connected_component(data)
else:  
    selected_graph = got.get_high_degree_subgraph(data)

html_content = got.visualize_graph(selected_graph)

components.html(html_content, height = 1200,width=1000)
got.node_centrality(data)
