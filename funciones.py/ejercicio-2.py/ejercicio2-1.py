#falto el profesor y los chicos organizan la clase

#creamos una funcion para obtener a los compañeros y retornar el asistente y al profesor
def obtener_compañeros(cantidad_de_compañeros):
    #creamos una lista vacia para poder agregar a los alumnos una vez cargado los datos
    compañeros = []
    #usamos un for para poder recorrer el tamaño del parametro pasado(en este ejemplo es un 5)
    for i in range(cantidad_de_compañeros):
        #ingresamos el nombre
        nombre = input("Ingrese el nombre del alumno: ")
        #ingresamos la edad del alumno
        edad = int(input("Ingrese la edad del alumno: "))
        #Creamos una tupla con esos datos obtenidos
        compañero = (nombre,edad)
        #usamos la funcion append para agregarlos a la lista vacia "compañeros" que creamos anteriormente
        compañeros.append(compañero)
        #utiliamos la funcion sort para ordenarlos con lambda y poder asi saber cual es el menor y el mayor de todos   
    compañeros.sort(key=lambda x:x[1])
    #asignamos el menor al asistente
    asistente = compañeros[0][0]
    #asignamos el mayor al profesor
    profesor = compañeros[-1][0]
    #retornamos esos dos valores obtenidos
    return asistente,profesor
#desempaquetamos...
asistente,profesor = obtener_compañeros(5)
#y finalmente mostramos quien es el asistente y quien es el madafucking profesor xddd
print(f"El profesor es: {profesor}")
print(f"El asistente es: {asistente}")