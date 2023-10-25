import math
try:
    datos = input().split()

    if math.pi * (float(datos[0])/2) ** 2 > float(datos[1]) * float(datos[2]): print("Compra la rodona")
    else:
        print("Compra la rectangular")
except ValueError: print("Fica valors númerics")