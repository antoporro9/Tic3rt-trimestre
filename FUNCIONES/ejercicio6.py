import math

def areaPerimetro(radio):
    numeroPi = math.pi
    
    area = numeroPi * (radio**2)
    perimetro = 2 * numeroPi * radio
    
    print("El área de la circunferencia es: ", area)
    print("El perímetro de la circunferencia es: ", perimetro)
    

radio = int(input("Indica el radio de la circunferencia: "))

areaPerimetro(radio)