#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# In[47]:


# Australia
aus_nodes = pd.read_csv('/Users/lip/Desktop/DAV/Australia_nodes.csv')
aus_edges = pd.read_csv('/Users/lip/Desktop/DAV/Australia_links.csv')
G = nx.from_pandas_edgelist(aus_edges, 'Source', 'Target', 'Weight')
degrees = dict(nx.degree(G))  # Convert the DegreeView object to a dictionary
# Sort the nodes by degree
sorted_degrees = sorted(degrees, key=degrees.get, reverse=True)

# Calculate the rank of each node
ranks = {node: rank for rank, node in enumerate(sorted_degrees)}

# Plot the degree distribution
plt.plot(ranks.values(), [degrees[node] for node in sorted_degrees], 'bo')
plt.title("Australia Degree Distribution (Degree-Rank plot)")
plt.xlabel('Rank')
plt.ylabel('Weighted degree')
plt.yscale('log')
plt.show()


# In[46]:


# China
china_nodes = pd.read_csv('/Users/lip/Desktop/DAV/China_nodes.csv')
china_edges = pd.read_csv('/Users/lip/Desktop/DAV/China_links.csv')
G = nx.from_pandas_edgelist(china_edges, 'Source', 'Target', 'Weight')
degrees = dict(nx.degree(G))  # Convert the DegreeView object to a dictionary
# Sort the nodes by degree
sorted_degrees = sorted(degrees, key=degrees.get, reverse=True)

# Calculate the rank of each node
ranks = {node: rank for rank, node in enumerate(sorted_degrees)}

# Plot the degree distribution
plt.plot(ranks.values(), [degrees[node] for node in sorted_degrees], 'bo')
plt.title("China Degree Distribution (Degree-Rank plot)")
plt.xlabel('Rank')
plt.ylabel('Weighted degree')
plt.yscale('log')
plt.show()

plt.show()


# In[44]:


UK_nodes = pd.read_csv('/Users/lip/Desktop/DAV/UK_nodes.csv')
UK_edges = pd.read_csv('/Users/lip/Desktop/DAV/UK_links.csv')
G = nx.from_pandas_edgelist(UK_edges, 'Source', 'Target', 'Weight')
degrees = dict(nx.degree(G))  # Convert the DegreeView object to a dictionary
# Sort the nodes by degree
sorted_degrees = sorted(degrees, key=degrees.get, reverse=True)

# Calculate the rank of each node
ranks = {node: rank for rank, node in enumerate(sorted_degrees)}

# Plot the degree distribution
plt.plot(ranks.values(), [degrees[node] for node in sorted_degrees], 'bo')
plt.title("UK Degree Distribution (Degree-Rank plot)")
plt.xlabel('Rank')
plt.ylabel('Weighted degree')
plt.yscale('log')
plt.show()


# In[42]:


USA_edges = pd.read_csv('/Users/lip/Desktop/DAV/USA_links.csv')
G = nx.from_pandas_edgelist(USA_edges, 'Source', 'Target', 'Weight')
# Calculate the degree of each node
degrees = dict(nx.degree(G))  # Convert the DegreeView object to a dictionary

# Sort the nodes by degree
sorted_degrees = sorted(degrees, key=degrees.get, reverse=True)

# Calculate the rank of each node
ranks = {node: rank for rank, node in enumerate(sorted_degrees)}

# Plot the degree distribution
plt.plot(ranks.values(), [degrees[node] for node in sorted_degrees], 'bo')
plt.title("USA Degree Distribution (Degree-Rank plot)")
plt.xlabel('Rank')
plt.ylabel('Weighted degree')
plt.yscale('log')
plt.show()


# In[ ]:




