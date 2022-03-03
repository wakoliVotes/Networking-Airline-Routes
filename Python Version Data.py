#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
mydata = pd.read_csv(r"D:\Network Science\Airlines.csv")


# In[4]:


# Overview of the Data Frame
mydata.head(n=20)


# ### Example 1: In this Section we Focus on Airline's "Flight" and "Destination"

# In[8]:


# Creating the World into which the graph will exist
import networkx as nx
GG = nx.Graph()


# In[9]:


GG.nodes()       # Empty since we have not added any Nodes yet


# In[11]:


GG.edges()      # Empty since we have not added any Edges yet


# In[12]:


# Trimming dataframe into only needed columns, i.e., 'flight', 'dest'
mydata1 = mydata[['flight', 'dest']]


# In[14]:


# Getting an overview of the New Dataframe
mydata1.head(n=10)


# In[15]:


# Adding the edges using pandas to created Graph 'GG'
GG = nx.from_pandas_edgelist(mydata1, 'flight', 'dest')


# In[16]:


# Checking the NEW outlook of the Graph based on Nodes
GG.nodes()


# In[17]:


# Checking the outlook of the Graph based on Edges
GG.edges()


# In[20]:


# Now, we need to visualize the Graph 'GG'
# Here, matplotlib.pyplot becomes useful

from matplotlib.pyplot import figure
figure(figsize=(20, 20))                                    # Specifying the figure size
nx.draw_shell(GG,  with_labels=True, node_color='red')


# ### Example 2: In this section, we focus on 'Carrier' and 'Destination'

# In[21]:


# Creating the world for new Graph 'GW'
GW = nx.Graph()


# In[22]:


# Picking needed columns from original data
mydata2 = mydata[['carrier', 'dest']]


# In[23]:


# Dataframe overview
mydata2.head(10)


# In[24]:


# Adding data frame to Graph 'GW'

GW = nx.from_pandas_edgelist(mydata2, 'carrier', 'dest')


# In[25]:


GW.nodes()


# In[26]:


GW.edges()


# In[27]:


# Visualizing the Graph GW now

figure(figsize=(15, 15))
nx.draw_shell(GW, with_labels=True, node_color='green')


# ### Example 3: In this last example, the focus is on 'Origin', and 'Destination'

# In[29]:


# Picking only the needed columns from original data [mydata]
mydata3 = mydata[['origin', 'dest']]


# In[30]:


# Creating Graph 'GS' that will hold the nodes and edges
GS = nx.Graph()


# In[31]:


# Getting an overview of the data
mydata3.head(10)


# In[32]:


# Now, adding the dataframe to the Graph 'GS' containing 'origin' and 'dest'
GS = nx.from_pandas_edgelist(mydata3, 'origin', 'dest')


# In[33]:


# Outlook of the Graph based on Nodes
GS.nodes()


# In[34]:


# Outlook of Graph based on Edges
GS.edges()


# In[35]:


# Finally, visualizing the Graph

figure(figsize=(15, 15))
nx.draw_shell(GS, with_labels=True, node_color='green')

