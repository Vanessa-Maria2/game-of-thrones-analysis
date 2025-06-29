import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st
from IPython.display import display, HTML

def got_data(url):
  data = Network(height="600px", width="100%", font_color="black", heading='Game of Thrones Graph')

  data.barnes_hut()
  got_data = pd.read_csv(url)

  sources = got_data['Source']
  targets = got_data['Target']
  weights = got_data['Weight']

  edge_data = zip(sources, targets, weights)

  for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    data.add_node(src, src, title=src)
    data.add_node(dst, dst, title=dst)
    data.add_edge(src, dst, value=w)

  neighbor_map = data.get_adj_list()

  for node in data.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

  data.show_buttons(filter_=['physics'])
  data.show("gameofthrones.html")
  display(HTML('gameofthrones.html'))
