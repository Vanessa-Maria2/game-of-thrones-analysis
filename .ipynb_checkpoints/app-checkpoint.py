import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
import got 

data = got.got_data('https://raw.githubusercontent.com/pupimvictor/NetworkOfThrones/master/stormofswords.csv')
HtmlFile = open("gameofthrones.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 1200,width=1000)