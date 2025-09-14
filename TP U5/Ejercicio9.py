contador=0
x="X"
o="O"
jugadas_ganadoras = [
    # Filas
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # Columnas
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Diagonales
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]
tateti=[
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
while True:
    contador=contador+1
    if contador == 9:
        print("Fin del juego! Empate")
        break
    elif contador % 2 == 0:
        simbolo=o
    elif contador % 2 != 0:
        simbolo=x
    while True:
        num=int(input("Ingrese la fila del 1 al 3 "))
        numb=int(input("y tambien ingrese la columna "))
        columna=numb-1
        fila=num-1
        if tateti[fila][columna] == "-":
            tateti[fila][columna] = simbolo
            for fila in tateti:
                print(" | ".join(fila))
            
            for combinacion in jugadas_ganadoras:
                a, b, c = combinacion
                if tateti[a[0]][a[1]] == tateti[b[0]][b[1]] == tateti[c[0]][c[1]] != "-":
                    print("¡Gano", tateti[a[0]][a[1]], "!")
                    exit()
            break
        else:
            print("Elija otra casila")