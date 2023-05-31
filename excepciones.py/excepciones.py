def sumar():
    while True:
     a = input("Ingrese numero 1: ")
     b = input("Ingrese numero 2: ")
     try:
      resultado = int(a) + int(b)
      print("Bien capo..")

     except:
         print("Te pedi un numero salaame, sos boludo?..dale..de nuevo")
     else:
         break
     finally:
        print("ESSSSOOO")
    return resultado
print(sumar())