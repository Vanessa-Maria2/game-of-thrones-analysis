import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
import got 

st.title('Game of Thrones')

data = got.got_data('https://raw.githubusercontent.com/pupimvictor/NetworkOfThrones/master/stormofswords.csv')
components.html(data, height = 1200,width=1000)