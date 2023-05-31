#creando una funcion que muestre la serie fibonacci entre el 0 hasta el numero dado
def fibonacci (num):
    a,b = 0,1
    lista_fibonacci = [0]
    for i in range(num):
        if b > num: return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a,b=b,a+b
            
            
resultado = fibonacci(34)
print(resultado)
            