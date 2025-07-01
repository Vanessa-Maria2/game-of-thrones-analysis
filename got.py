import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st
from IPython.display import display, HTML

def graph_full(url):
  G = nx.Graph()
  
  data = pd.read_csv(url)

  for _, row in data.iterrows():
        G.add_edge(row['Source'], row['Target'], weight=row['Weight'])
  return G

def get_largest_connected_component(G):
    components = list(nx.connected_components(G))
    largest = max(components, key=len)
    return G.subgraph(largest).copy()

def get_high_degree_subgraph(G, min_degree=5):
    high_degree_nodes = [n for n, d in G.degree() if d >= min_degree]
    return G.subgraph(high_degree_nodes).copy()

def node_centrality(G):
  eigen_centrality = nx.eigenvector_centrality(G)
  degree_centrality = nx.degree_centrality(G)
  closeness_centrality = nx.closeness_centrality(G)
  betweenness_centrality = nx.betweenness_centrality(G)

  df = pd.DataFrame({
        'Eigenvector': eigen_centrality,
        'Degree': degree_centrality,
        'Closeness': closeness_centrality,
        'Betweenness': betweenness_centrality
    })
  
  top_nodes = set()
  for col in df.columns:
    top_nodes.update(df[col].sort_values(ascending=False).head(20).index)

  df_top = df.loc[list(top_nodes)].fillna(0)

  fig, axs = plt.subplots(2, 2, figsize=(15, 10))
  df_top['Eigenvector'].sort_values(ascending=False).plot(kind='bar', ax=axs[0, 0], title='Eigenvector Centrality')
  df_top['Degree'].sort_values(ascending=False).plot(kind='bar', ax=axs[0, 1], title='Degree Centrality')
  df_top['Closeness'].sort_values(ascending=False).plot(kind='bar', ax=axs[1, 0], title='Closeness Centrality')
  df_top['Betweenness'].sort_values(ascending=False).plot(kind='bar', ax=axs[1, 1], title='Betweenness Centrality')

  for ax in axs.flatten():
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        ax.set_ylabel("Centrality")

  plt.tight_layout()
  st.pyplot(fig)

def visualize_graph(G):
  net = Network(height="600px", width="100%", font_color="black", notebook=True)
  net.barnes_hut()
  net.from_nx(G)

  neighbor_map = net.get_adj_list()

  for node in net.nodes:
    if "title" not in node:
        node["title"] = str(node["id"])
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

  net.show_buttons(filter_=['physics'])
  net.show("gameofthrones.html")
  display(HTML('gameofthrones.html'))
  with open("gameofthrones.html", "r", encoding="utf-8") as f:
        html_content = f.read()

  metrics(G)
  return html_content

def metrics(G):
  density = nx.density(G)
  assortativity = nx.degree_assortativity_coefficient(G) 
  clustering = nx.average_clustering(G.to_undirected()) 
  wcc = len(list(nx.connected_components(G)))
  is_directed = G.is_directed()

  st.write(f"**Densidade da rede:** {density:.4f}")
  st.write(f"**Assortatividade:** {assortativity:.4f}")
  st.write(f"**Coeficiente de clustering global:** {clustering:.4f}")
  st.write(f"**Componentes fracamente conectados:** {wcc}")
  st.write(f"**Grafo dirigido:** {is_directed}")