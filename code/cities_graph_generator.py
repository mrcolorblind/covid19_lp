import pandas as pd
import seaborn as sns
import math
sns.set()
# plt.set()
import matplotlib.pyplot as plt

cities      = pd.read_csv("../data/cities.csv")
arcos       = cities['arcos']
bh          = cities['bh']
contagem    = cities['contagem']
divinopolis = cities['divinopolis']
lagoa       = cities['lagoa']
lavras      = cities['lavras']
samonte     = cities['samonte']
index       = range(len(cities))
year        = cities['year']
month       = cities['month']
day         = cities['day']
date        = [(str(day[i]) + "/" + str(month[i]) + "/" + str(year[i])) for i in range(len(day))]
actual      = len(day) - 1

plt.plot(index, arcos, 'red', index, contagem, 'navy', index, divinopolis, 'black', index, lagoa, 'magenta', index, lavras, 'seagreen', index, samonte, 'darkgoldenrod')
plt.title("Casos de COVID-19 em diferentes cidades por tempo (" + date[actual] + ")")
plt.xlabel("Dias desde 01/04/2020")
plt.xlim(0, len(index))
plt.ylabel("Número de casos")
plt.xticks(range(0, len(cities), math.floor(len(cities) / 10)))
plt.legend(["Arcos", "Contagem", "Divinopolis", "Lagoa da Prata", "Lavras", "Santo Antônio do Monte"])
plt.savefig("../data/graph_cities.png", dpi=300)
saveName = "/home/jonas/Imagens/covid/grafico_cidades_"+ str(day[actual]) + "_" + str(month[actual]) + "_" + str(year[actual]) + ".png"
plt.savefig(saveName, dpi=300)