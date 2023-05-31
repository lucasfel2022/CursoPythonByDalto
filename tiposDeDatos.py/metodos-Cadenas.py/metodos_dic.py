diccionario  = {
    "nombre" : "Lucas",
    "edad" : 22,
    "Nacionalidad" : "Argentino",
    "Hicha" : "Boca juniors"
}

claves = diccionario.keys() #Nos devuelve un objeto

valor_De_elemento = diccionario.get("nombre") #Nos da el valor del elemento

#Eliminando todos los elementos del diccionario
#diccionario.clear()

elemento_a_eliminar = diccionario.pop("Hincha")#Eliminando un elemento del diccionario

print(valor_De_elemento)