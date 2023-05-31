import pandas as pd
#usando el read csv para leer el archivo csd con pandas
#df hace referencia al "data frame"
df  = pd.read_csv("archivosTXT.py\\datos.csv")
df2  = pd.read_csv("archivosTXT.py\\datos.csv")
#obteniendo los datos de la columna
nombres = df["nombre"] 
#ordenando el data frame por la edad
df_ordenado = df.sort_values("edad")
#ordenando de forma ascendente (de mayor a menor)
df_ordenado = df.sort_values("edad",ascending=False)
#print(df_ordenado)


# concatenando los dos data frame
df_concatenado = pd.concat([df,df2])
print(df_concatenado)

#accediendo a la primera fila con head
df_pimera_fila = df.head(0)
df_ultima_fila = df.tail(3)
print(df_ultima_fila)