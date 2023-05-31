import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivosGraficos.py\\fuente_ingresos.csv")
#mostrando el grafico en barras
sns.barplot(x="fuente",y="ingresos",data=df)
#sumando los iinigresos totales con .sum
ingresos_totales = df['ingresos'].sum()
#mostrando el total de los ingresos obtenidos
print(f'el total de los ingresos es de: ${ingresos_totales}')
plt.show()
