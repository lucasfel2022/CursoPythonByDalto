import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#importando el archivo y leyendolo con pandas
df = pd.read_csv("archivosGraficos.py\\pedos.csv")
#asignamos los valores en el grafico con lineaas, de tipo lineal y le damos cordenadas
sns.lineplot(x="fecha",y="pedos",data=df)
#usamos el plt con plot para hacer un punto en el grafco
plt.plot("7-5",9,"o")
plt.plot("13-5",1,"o")
#lo mostramos al grafico con show
plt.show()