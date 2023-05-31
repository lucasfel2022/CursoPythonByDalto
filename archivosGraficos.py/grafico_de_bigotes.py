import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivosGraficos.py\\bigotes.csv")
#mostrando el grafico en metodo de box
sns.boxplot(x="categoria",y="valor",data=df)
plt.show()
