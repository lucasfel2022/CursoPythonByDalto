frase = input("Hola, por favor, ingrese una frase para contar la cantidad de palabras ingresada: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(cantidad_de_palabras)
if cantidad_de_palabras > 120 : print("Flaco, te pregunte como estabas nada mas...")