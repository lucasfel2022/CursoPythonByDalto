animales = ["gato","perro","loro","cocodrilo"]
numeros = [1,2,3,4]
#recorriendo la lista animales
for animal in animales:
     print(animal)





#recorriendo la lista numeros y multiplicandola por dos
for numero in numeros:
        resultado = numero * 2
        print(f'La multiplicacion da: {resultado}')
    
  
  
  
    
    
for animal,numero in zip(animales,numeros):
     print(f'elemento de la lista 1 : {animal}')
     print(f'elemento de la lista 2 : {numero}')
    



#forma optima y eficaz de recorrer una lista con su indice
for num in enumerate(numeros):
     indice = num [0]
     valor = num[1]
     print(f'El indice es : {indice} y el valor es de: {valor}')
