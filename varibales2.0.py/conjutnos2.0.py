#Creando un conjunto con set
conjunto = set(["Lucas","Fel"])

conjunto1 = frozenset(["Lucas","Fel"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,2,3,4}
conjunto2 = {2,3,4}
#cerificando el subconjunto
resultado = conjunto2.issubset(conjunto1)
print(resultado)
#Verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay un numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)
