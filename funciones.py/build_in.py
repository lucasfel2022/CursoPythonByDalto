numeros = [2,4,6,8,10]

#encontrando el numero mas alto
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero mas chico
numero_mas_chico = min(numeros)
print(numero_mas_chico)

#rendondeando numeros con coma
numero = round(12345.678934242423,2)
print(numero)
#retorna false -> 0 ,vacio , false, none / true -> distinto de 0 , true, cadena , datos no vacio
resultado_bool = bool("asdasd")
print(resultado_bool)

#retorna true, si todos los valores son verdaderos
resultado_all = all([0,"true",[1,2,3]])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)