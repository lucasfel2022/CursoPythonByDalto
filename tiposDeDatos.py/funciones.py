#Creando una lista con list()
lista = list(["hola","Soy","Lucas",22])
#devuelve la cantidad de elementos de una lista
cantidad_elementos =  len(lista)
#agregando un elemento a la lista con append
lista.append("Soy el mejor programador de Python")
#Agregando un elemento a la lista
lista.insert(3,"hola capo")
#Agregamos una lista a otra lista
lista.extend(["anashe","nanananashe"])
#Eliminando un elemento de la list apor su indice
#para eliminar el ultimo elemento de una lista podemos usar el -1
lista.pop(5)
#Eliminando elemento por su valor
lista.remove("nanananashe")
#Elimina TODOS los elementos de la lista
#lista.clear()
#invierte los elementos de una lista
#lista.reverse()
#Elemento a buscar por indice
elemento_encontrado = lista.index(22)
print(elemento_encontrado)