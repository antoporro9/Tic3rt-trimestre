cadena=input("Introduzca una cadena de caracteres ")
contador=0

for i in cadena:
    if(i==" "):
        contador=contador+1

print("La cadena tiene ", contador+1,"palabras")