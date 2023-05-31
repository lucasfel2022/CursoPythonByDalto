diciconario = {
    "nombre":"Lucas",
    "apellido": "Fel",
    "edad" : 22
}
frutas  = ("banana","pera","manzana","naranja")
#recorriendo el dicc solamentes para obtener la claves
for datos in diciconario:
     print(datos)
     

#recorriendo el dicc para obtener las claves y sus valores con items()
for datos in diciconario.items():
     indice = datos[0]
     valor = datos[1]
     print(f'el indice es: {indice} y el valor es de : {valor}')
    
    
#saltear una vuelta con continue..
for fruta in frutas:
    if fruta == "manzana":
        continue
     
    print(f'Que rica que estaba la: {fruta}')
    
    
#cortar el bucle con la sentencia break
for fruta in frutas:
    if fruta == "pera":
        break
    print(f'Me comi una : {fruta}')