numero=(int)(input("Introduzca un numero y cuando desee acabar introduzca el 0 "))
suma=0
contador=0
while numero!=0:
    suma=suma+numero
    contador=contador+1
    numero=(int)(input("Introduzca un numero y cuando desee acabar introduzca el 0 "))

print("La media es",suma/contador)
print("La suma es ", suma)