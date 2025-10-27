def validar_dimensiones(longitud, anchura):
    return longitud >=0 and anchura>=0
def calcular_area(longitud, anchura):
    return longitud*anchura
def calcular_perimetro(longitud, anchura):
    return 2*(longitud+anchura)

long=int(input("Ingrese la longitud: "))
ancho=int(input("Ingrese la anchura: "))

validar=validar_dimensiones(long, ancho)
area=calcular_area(long, ancho)
perimetro=calcular_perimetro(long, ancho)
if validar == True:
    print(f"El area del rectangulo es {area} y el perimetro es {perimetro}")
else:
    print("No son dimensiones validas.")