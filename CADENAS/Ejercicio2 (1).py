
cadena=input("Dime una cadena de caracteres. ")
subcadena=input("Dime una subcadena de caracteres. ")

if (subcadena == cadena[0:len(subcadena)]):
    print("La cadena leída por teclado comienza por una subcadena introducida por teclado")
else: print("La cadena leída por teclado no comienza por una subcadena introducida por teclado")
