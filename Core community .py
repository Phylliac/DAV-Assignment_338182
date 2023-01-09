#!/usr/bin/env python
# coding: utf-8

# In[27]:


import networkx as nx
import matplotlib.pyplot as plt

# Load the network
Australia_edges = pd.read_csv('/Users/lip/Desktop/DAV/Australia_links.csv')
G = nx.from_pandas_edgelist(Australia_edges, 'Source', 'Target', 'Weight')

# Calculate the k-core of the network
k_core = nx.k_core(G)

print(k_core)

# Draw the k-core
nx.draw(k_core, with_labels=True)

# Show the plot
plt.show()


# In[18]:


import networkx as nx
import matplotlib.pyplot as plt

# Load the network
Australia_edges = pd.read_csv('/Users/lip/Desktop/DAV/Australia_links.csv')
G = nx.from_pandas_edgelist(Australia_edges, 'Source', 'Target', 'Weight')

# Calculate the degree of each node
degrees = dict(nx.degree(G))  # Convert the DegreeView object to a dictionary

# Sort the nodes by degree
sorted_degrees = sorted(degrees, key=degrees.get, reverse=True)

# Calculate the rank of each node
ranks = {node: rank for rank, node in enumerate(sorted_degrees)}

# Calculate the number of connections to higher degree nodes for each node
num_connections = {}
for node in G.nodes():
    num_connections[node] = sum(1 for neighbor in G[node] if ranks[neighbor] > ranks[node])

# Plot the number of connections to higher degree nodes against rank
plt.plot(ranks.values(), num_connections.values())
plt.xlabel('Rank')
plt.ylabel('Number of connections to higher degree nodes')
plt.show()


# In[26]:


import networkx as nx
import matplotlib.pyplot as plt

china_edges = pd.read_csv('/Users/lip/Desktop/DAV/China_links.csv')
G = nx.from_pandas_edgelist(china_edges, 'Source', 'Target', 'Weight')

# Calculate the k-core of the network
k_core = nx.k_core(G)

print(k_core)

# Draw the k-core
nx.draw(k_core, with_labels=True)

# Show the plot
plt.show()


# In[17]:


# Load the network
china_edges = pd.read_csv('/Users/lip/Desktop/DAV/China_links.csv')
G = nx.from_pandas_edgelist(china_edges, 'Source', 'Target', 'Weight')

# Calculate the degree of each node
degrees = dict(nx.degree(G))  # Convert the DegreeView object to a dictionary

# Sort the nodes by degree
sorted_degrees = sorted(degrees, key=degrees.get, reverse=True)

# Calculate the rank of each node
ranks = {node: rank for rank, node in enumerate(sorted_degrees)}

# Calculate the number of connections to higher degree nodes for each node
num_connections = {}
for node in G.nodes():
    num_connections[node] = sum(1 for neighbor in G[node] if ranks[neighbor] > ranks[node])

# Plot the number of connections to higher degree nodes against rank
plt.plot(ranks.values(), num_connections.values())
plt.xlabel('Rank')
plt.ylabel('Number of connections to higher degree nodes')
plt.show()


# In[25]:


import networkx as nx
import matplotlib.pyplot as plt

china_edges = pd.read_csv('/Users/lip/Desktop/DAV/UK_links.csv')
G = nx.from_pandas_edgelist(china_edges, 'Source', 'Target', 'Weight')

# Calculate the k-core of the network
k_core = nx.k_core(G)

print(k_core)

# Draw the k-core
nx.draw(k_core, with_labels=True)

# Show the plot
plt.show()


# In[16]:


# Load the network
UK_edges = pd.read_csv('/Users/lip/Desktop/DAV/UK_links.csv')
G = nx.from_pandas_edgelist(UK_edges, 'Source', 'Target', 'Weight')
# Calculate the degree of each node
degrees = dict(nx.degree(G))  # Convert the DegreeView object to a dictionary

# Sort the nodes by degree
sorted_degrees = sorted(degrees, key=degrees.get, reverse=True)

# Calculate the rank of each node
ranks = {node: rank for rank, node in enumerate(sorted_degrees)}

# Calculate the number of connections to higher degree nodes for each node
num_connections = {}
for node in G.nodes():
    num_connections[node] = sum(1 for neighbor in G[node] if ranks[neighbor] > ranks[node])

# Plot the number of connections to higher degree nodes against rank
plt.plot(ranks.values(), num_connections.values())
plt.xlabel('Rank')
plt.ylabel('Number of connections to higher degree nodes')
plt.show()


# In[24]:


import networkx as nx
import matplotlib.pyplot as plt

china_edges = pd.read_csv('/Users/lip/Desktop/DAV/USA_links.csv')
G = nx.from_pandas_edgelist(china_edges, 'Source', 'Target', 'Weight')

# Calculate the k-core of the network
k_core = nx.k_core(G)

print(k_core)

# Draw the k-core
nx.draw(k_core, with_labels=True)

# Show the plot
plt.show()


# In[15]:


# Load the network
USA_edges = pd.read_csv('/Users/lip/Desktop/DAV/USA_links.csv')
G = nx.from_pandas_edgelist(USA_edges, 'Source', 'Target', 'Weight')

# Calculate the degree of each node
degrees = dict(nx.degree(G))  # Convert the DegreeView object to a dictionary

# Sort the nodes by degree
sorted_degrees = sorted(degrees, key=degrees.get, reverse=True)

# Calculate the rank of each node
ranks = {node: rank for rank, node in enumerate(sorted_degrees)}

# Calculate the number of connections to higher degree nodes for each node
num_connections = {}
for node in G.nodes():
    num_connections[node] = sum(1 for neighbor in G[node] if ranks[neighbor] > ranks[node])

# Plot the number of connections to higher degree nodes against rank
plt.plot(ranks.values(), num_connections.values())
plt.xlabel('Rank')
plt.ylabel('Number of connections to higher degree nodes')
plt.show()


# In[ ]:




