import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

cases      = pd.read_csv('../data/cases.csv')
year       = cases['year']
month      = cases['month']
day        = cases['day']
suspicious = cases['suspicious']
positive   = cases['positive']
negative   = cases['negative']
date       = [(str(year[i]) + "-" + str(month[i]) + "-" + str(day[i])) for i in range(len(day))]
index      = range(len(cases))

plt.plot(index, suspicious, 'y', index, negative, 'g', index, positive, 'r')
plt.title("Casos de COVID-19 em Lagoa da Prata por tempo")
plt.xlabel("Dias desde 22/03 (Primeiro boletim)")
plt.ylabel("Número de casos")
plt.legend(["Suspeitos", "Negativos", "Confirmados"])
plt.savefig("../data/graph.png")