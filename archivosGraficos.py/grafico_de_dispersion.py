import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivosGraficos.py\\dispersion.csv")
#mostrando el grafico en metodo de dispersion
sns.scatterplot(x="tiempo",y="dinero",data=df)
plt.show()
