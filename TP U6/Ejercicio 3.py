def rectangulo(longitud, anchura):
    area=longitud*anchura
    perimetro=2*(longitud+anchura)
    tupla=(area, perimetro)
    return tupla

while True:
    long=(int(input("Ingrese la longitud del rectangulo: ")))
    ancho=(int(input("Ingrese el ancho del rectangulo: ")))
    if long > 0 and ancho > 0:
        area, perimetro=rectangulo(long, ancho)
        print(f"El area del rectangulo es {area} y el perimetro es {perimetro}")
        if long == ancho:
            print("Este rectangulo es un cuadrado.")
        break
    else:
        print("Las dimensiones deben ser mayores a 0.")