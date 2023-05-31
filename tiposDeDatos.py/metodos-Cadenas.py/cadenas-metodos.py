cadena1 = "Hola me llamo Lucas"
cadena2 = "Y tengo 22 años"

resultado = cadena1.upper() #convierte a mayuscula

print(resultado)

resultado = cadena1.lower() #convierte a minuscula
print(resultado)

primera_letra_mayuscula = cadena1.capitalize() #convierte la primera letra en mayuscula
print(primera_letra_mayuscula)

busqueda_find = cadena1.find("a") #buscamos una cadena en otra cadena, sino hay coincidencias el valor sera de -1
print(busqueda_find)


es_alphanumerico = cadena1.isalpha() #es alphanumerico contando de la "a/A" a la "z/Z"
print(es_alphanumerico)

contar_coicidencias = cadena1.count("a") # cuenta la cantidad de veces que esta el caracter en el parentesis
print(contar_coicidencias)

contar_caracteres = len(cadena1) #nos cuenta la cantidad de caracteres que tiene la cadena
print(contar_caracteres)