#creando una funcion simple
#def saludar():
    #print("Hola lucas mi maestro , como estas??")
    

#Ejecutando la funcion simple
#saludar()

#creando una funcion con parametros
def saludar(nombre,sexo):
     sexo = sexo.lower()
     if (sexo == "mujer"):
          adjetivo = "reina"
    
     elif(sexo == "hombre"):
          adjetivo = "maestro"
          
     print(f'Hola {nombre} como estas {adjetivo} ??')
    

saludar("Lucas","mujer")

#creando una funcion que retorna algo (vamos a crear una contraseña random xd)
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
 #desempaquetando la funcion mostrando los resultados obtenidos y los datos utilizados para obtenerlos   
password,primer_numero = crear_contraseña_random(768)
print(f"La contraseña es: {password}")
print(f"Y el nnumero utilizado fue: {primer_numero}")
