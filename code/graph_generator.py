import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cases      = pd.read_csv('../data/cases.csv')
year       = cases['year']
month      = cases['month']
day        = cases['day']
suspicious = cases['suspicious']
positive   = cases['positive']
negative   = cases['negative']
date       = [(str(day[i]) + "/" + str(month[i]) + "/" + str(year[i])) for i in range(len(day))]
index      = range(len(cases))

plt.plot(index, suspicious, '--y', index, negative, '--g', index, positive, '--r')
plt.title("Casos de COVID-19 em Lagoa da Prata por tempo (" + date[len(date)-1] + ")")
plt.xlabel("Dias desde 22/03 (Primeiro boletim)")
plt.ylabel("Número de casos")
plt.legend(["Suspeitos", "Negativos", "Confirmados"])
plt.savefig("../data/graph.png", dpi=300)
actual = len(day) - 1
saveName = "/home/jonas/Imagens/covid/grafico_"+ str(day[actual]) + "_" + str(month[actual]) + "_" + str(year[actual]) + ".png"
plt.savefig(saveName, dpi=300)
