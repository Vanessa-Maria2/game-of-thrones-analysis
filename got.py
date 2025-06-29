import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st
from IPython.display import display, HTML

def got_data(url):
  G = nx.Graph()
  data = pd.read_csv(url)

  for _, row in data.iterrows():
        G.add_edge(row['Source'], row['Target'], weight=row['Weight'])

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
  scc = len(list(nx.strongly_connected_components(G))) if nx.is_directed(G) else 'N/A'
  wcc = len(list(nx.connected_components(G)))

  st.write(f"**Densidade da rede:** {density:.4f}")
  st.write(f"**Assortatividade:** {assortativity:.4f}")
  st.write(f"**Coeficiente de clustering global:** {clustering:.4f}")
  st.write(f"**Componentes fortemente conectados:** {scc}")
  st.write(f"**Componentes fracamente conectados:** {wcc}")