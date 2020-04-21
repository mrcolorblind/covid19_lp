#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import math
sns.set()
# plt.set()
import matplotlib.pyplot as plt


# In[4]:


parcos       = 40092 / 10000
pbh          = 2512070 / 10000
pcontagem    = 663855 / 10000
pdivinopolis = 238230 / 10000
plagoa       = 52165 / 10000
plavras      = 103773 / 10000
psamonte     = 28243 / 10000


# In[8]:


cities      = pd.read_csv("../data/cities.csv")
arcos       = [i/parcos for i in cities['arcos']]
bh          = [i/pbh for i in cities['bh']]
contagem    = [i/pcontagem for i in cities['contagem']]
divinopolis = [i/pdivinopolis for i in cities['divinopolis']]
lagoa       = [i/plagoa for i in cities['lagoa']]
lavras      = [i/plavras for i in cities['lavras']]
samonte     = [i/psamonte for i in cities['samonte']]
index       = range(len(cities))
year        = cities['year']
month       = cities['month']
day         = cities['day']
date       = [(str(day[i]) + "/" + str(month[i]) + "/" + str(year[i])) for i in range(len(day))]
actual      = len(day) - 1


# In[23]:


plt.plot(index, arcos, 'red', index, bh, 'navy', index, contagem, 'yellow', index, divinopolis, 'black', index, lagoa, 'magenta', index, lavras, 'seagreen', index, samonte, 'darkgoldenrod')
plt.title("Casos de COVID-19 para cada 10.000 habitantes (" + date[actual] + ")")
plt.xlabel("Dias desde 01/04/2020")
plt.xlim(0, len(index))
plt.ylabel("Número de casos")
plt.xticks(range(0, len(cities), math.floor(len(cities) / 10)))
plt.legend(["Arcos", "Belo Horizonte", "Contagem", "Divinopolis", "Lagoa da Prata", "Lavras", "Santo Antônio do Monte"])
plt.savefig("../data/population_graph_cities.png", dpi=300)
saveName = "/home/jonas/Imagens/covid/" + str(day[actual]) + "_" + str(month[actual]) + "_" + str(year[actual]) + "_grafico_cidades_populacao.png"
plt.savefig(saveName, dpi=300)

