archivo = open("archivosTXT.py\\textodeDalto.txt")# aca estamos abriendo el archivo para despues guardarlo y poder leerlo
#print(archivo.read())# aca estamos leyendo el archivo completo

lineas = archivo.readlines()
print(lineas)
archivo.close()