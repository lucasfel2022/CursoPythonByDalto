import re

texto = '''Hola como estas capoeira? todo viento
esta es la linea 2...segui baajanndo...
 y finalmente terminamos aac mi reyyyy de reyessss'''
 
 #haciendo un busqueda simple
#resultado = re.search("segui",texto)

#d, buscando datos numericos del 0_9
#resultado = re.findall(r"\d",texto)

#D, devuelve todos los datos menos los numericos
#resultado = re.findall(r"\D",texto)

#s, busca espacios en linea,tabs,espacios,etc...
#resultado = re.findall(r"\s",texto)

#s, busca TODO MENOS espacios en linea,tabs,espacios,etc...
#resultado = re.findall(r"\S",texto)

#\n, busca  saltos en linea
#resultado = re.findall(r"\n",texto)

#\, cancela alos caracteres especales
resultado = re.findall(r"\.",texto)


print(resultado)