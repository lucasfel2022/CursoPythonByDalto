import csv

with open("archivosTXT.py\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
    