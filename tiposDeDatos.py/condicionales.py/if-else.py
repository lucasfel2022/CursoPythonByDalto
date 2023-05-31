ingreso_mensual = 10

if ingreso_mensual >= 10000 :
    #si se cumple la condicion de arriba va a ejecutarse el codigo, sino, pasa al bloque de abajo
    print("Estas bien economicamente en cualquier parte del mundo")
    
    #funciona como else if pero en Python se escribe Elif (funcionam de la misma manera)
elif ingreso_mensual >=1000 :
    print("Estas bien en lationamerica")
#sino se cumple el primer if, y el segundo tampoco, el else funciona como cualquier else. Como sino
else : 
    print("Sos pobre weyyyy")