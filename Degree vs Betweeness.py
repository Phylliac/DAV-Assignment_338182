#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# In[11]:


# Australia
Australia_nodes = pd.read_csv('/Users/lip/Desktop/DAV/Australia_nodes.csv')
Australia_edges = pd.read_csv('/Users/lip/Desktop/DAV/Australia_links.csv')
G = nx.from_pandas_edgelist(Australia_edges, 'Source', 'Target', 'Weight')
deg_centrality = nx.degree_centrality(G)
bet_centrality = nx.betweenness_centrality(G, normalized = True, endpoints = False)
plt.scatter(bet_centrality.values(), deg_centrality.values())
plt.title("Australia Degree centrality vs. betweenness centrality distribution")
plt.ylabel("Degree centrality")
plt.xlabel("Betweenness centrality")
# assortativity
r = nx.degree_assortativity_coefficient(G)
print(f"{r:3.1f}")


# In[12]:


# China
china_nodes = pd.read_csv('/Users/lip/Desktop/DAV/China_nodes.csv')
china_edges = pd.read_csv('/Users/lip/Desktop/DAV/China_links.csv')
G = nx.from_pandas_edgelist(china_edges, 'Source', 'Target', 'Weight')
deg_centrality = nx.degree_centrality(G)
bet_centrality = nx.betweenness_centrality(G, normalized = True, endpoints = False)
plt.scatter(bet_centrality.values(), deg_centrality.values())
plt.title("China Degree centrality vs. betweenness centrality distribution")
plt.ylabel("Degree centrality")
plt.xlabel("Betweenness centrality")
# assortativity
r = nx.degree_assortativity_coefficient(G)
print(f"{r:3.1f}")


# In[13]:


# UK
UK_nodes = pd.read_csv('/Users/lip/Desktop/DAV/UK_nodes.csv')
UK_edges = pd.read_csv('/Users/lip/Desktop/DAV/UK_links.csv')
G = nx.from_pandas_edgelist(UK_edges, 'Source', 'Target', 'Weight')
deg_centrality = nx.degree_centrality(G)
bet_centrality = nx.betweenness_centrality(G, normalized = True, endpoints = False)
plt.scatter(bet_centrality.values(), deg_centrality.values())
plt.title("UK Degree centrality vs. betweenness centrality distribution")
plt.ylabel("Degree centrality")
plt.xlabel("Betweenness centrality")
# assortativity
r = nx.degree_assortativity_coefficient(G)
print(f"{r:3.1f}")


# In[14]:


# USA
USA_nodes = pd.read_csv('/Users/lip/Desktop/DAV/USA_nodes.csv')
USA_edges = pd.read_csv('/Users/lip/Desktop/DAV/USA_links.csv')
G = nx.from_pandas_edgelist(USA_edges, 'Source', 'Target', 'Weight')
deg_centrality = nx.degree_centrality(G)
bet_centrality = nx.betweenness_centrality(G, normalized = True, endpoints = False)
plt.scatter(bet_centrality.values(), deg_centrality.values())
plt.title("UK Degree centrality vs. betweenness centrality distribution")
plt.ylabel("Degree centrality")
plt.xlabel("Betweenness centrality")
# assortativity
r = nx.degree_assortativity_coefficient(G)
print(f"{r:3.1f}")


# In[ ]:




