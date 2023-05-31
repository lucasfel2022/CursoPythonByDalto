# 2 listas, una con nombre otra con apellido
nombre = ["Lucas","Milagros","Natalia","Agustin"]
apellido = ["Fel","Bogliano","Martinez","Cea"]
#registrar esta informacion en un TXT  de la forma mas optima

with open("nombre_y_apellidos.txt","w") as archivo:
     archivo.writelines("Los datos son: \n")
     [archivo.writelines(f"Nombre: {n} \n Apellido: {i} \n------------------\n") for n,i in zip(nombre,apellido)]  