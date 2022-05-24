
factorial = 1
numero = int(input("Introduce el número para calcular su factorial: "))

if (numero<0):
    print("No existe el factorial de un número negativo")
else:
    for i in range(2,(numero+1)):
        factorial = factorial*i

print("El factorial de ", numero, " es ", factorial)