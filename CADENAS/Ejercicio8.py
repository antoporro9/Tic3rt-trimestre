cadena=input("Introduzca una cadena:  ")
tam=len(cadena)-1
i=0
while i<=tam:
    if cadena[i]==cadena[i].upper():
        print(cadena[i].lower(), end="")
    else:
     print(cadena[i].upper(),end="")
    
    i=i+1