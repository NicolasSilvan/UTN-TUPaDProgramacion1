#Ejercicio 1
lista=[ 6, 8, 4, 2, 7, 9, 8, 10, 5, 6]
suma=0
for i in range(len(lista)):
    suma=suma+lista[i]
    print(f"Estudiante N°{i+1}: Nota {lista[i]}")
notaa=max(lista)
notab=min(lista)
promedio=suma/len(lista)
print(f"La nota mas alta es: {notaa}, la mas baja es: {notab} y el promedio de todas las notas es: {promedio}")
#-------------------------------------------------------
#Ejercicio 2
productos=[]
for i in range(1, 6):
    producto=input("Escriba el producto: ")
    productos.append(producto)
    
lista_ordenada=sorted(productos)
print(lista_ordenada)

while True:
    decision=input("Desea eliminar algun producto del carrito? S/N ").lower()
    if decision == "si" or decision == "s":
        otro=int(input("Escriba un numero del 1 al 5 dependiendo que producto desee eliminar "))
        otro-=1
        print(f"Ha eliminado {lista_ordenada[otro]} de la lista")
        del lista_ordenada[otro]
        print(lista_ordenada)
    elif decision == "no" or decision == "n":
        break
#-------------------------------------------------------
#Ejercicio 3
import random
lista=[]
pares=[]
impares=[]
for i in range(1, 16):
    numero_aleatorio=random.randint(1, 100)
    lista.append(numero_aleatorio)

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(f"Hay {len(pares)} numeros pares y {len(impares)} numeros impares.")
#-------------------------------------------------------
#Ejercicio 4
datos=[1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos=[]
for i in datos:
    if i not in sin_repetidos:
        sin_repetidos.append(i)

print(sin_repetidos)
#-------------------------------------------------------
#Ejercicio 5
estudiantes=["Emiliano", "Enzo", "Gabriel", "Luciano", "Abigail", "Adrian", "Agustin", "Alejo"]

while True:
    pregunta=input("Quiere agregar un nuevo estudiante o eliminar uno existente? S/N ").lower()
    if pregunta == "si" or pregunta == "s":
        preguntab=int(input("Si desea agregar uno nuevo escriba 1, si desea eliminar uno existente escriba 2 "))
        if preguntab == 1:
            estudiante=input("Ingrese el nombre del estudiante que quiere añadir a la lista ").title()
            estudiantes.append(estudiante)
            print(estudiantes)
        elif preguntab == 2:
            print(estudiantes)
            estudianteb=int(input("Ingrese con numeros que estudiante de la lista quiere eliminar "))
            del estudiantes[estudianteb-1]
            print(estudiantes)
    elif pregunta == "no" or pregunta == "n":
        print(f"Esta es la lista despues de los cambios, {estudiantes}")
        break
#-------------------------------------------------------
#Ejercicio 6
numeros=[5, 32, 68, 12, 75, 40, 56]
ultimo=numeros.pop()
numeros.insert(0, ultimo)
print(numeros)
#-------------------------------------------------------
#Ejercicio 7
minimas=0
maximas=0
mayor_amplitud=0
dia_amplitud=0
i=0
temperaturas= [
    [10, 19],
    [12, 23],
    [4, 14],
    [16, 27],
    [9, 20],
    [14, 26],
    [8, 15],
]
for dia in temperaturas:
    minimas+=dia[0]

for dia in temperaturas:
    maximas+=dia[1]

promedio_max=maximas/7
promedio_min=minimas/7

for dia in temperaturas:
    i=i+1
    resta=dia[1]-dia[0]
    if mayor_amplitud<resta:
        mayor_amplitud=resta
        dia_amplitud=i

print(f"El promedio de las minimas es {promedio_min} y el de las maximas es {promedio_max}")
print(f"Hubo una amplitud de {mayor_amplitud}°, el dia {dia_amplitud}")
#-------------------------------------------------------
#Ejercicio 8
promedio=[]
materia=[]
notas=[
    [9, 7, 5],
    [2, 6, 10],
    [5, 7, 8],
    [9, 10, 8],
    [4, 6, 8]
]
for i in range(len(notas)):
    materias=(len(notas[i]))
    suma=sum(notas[i])
    promediob=suma/materias
    promedio.append(round(promediob, 1))

for j in range(len(notas[0])):
    suma=0
    for i in range(len(notas)):
        suma += notas[i][j]
    promedioc=suma/len(notas)
    materia.append(round(promedioc, 1))
    
print(f"El promedio de los estudiantes es: {promedio}")
print(f"El promedio de las materias es: {materia}")
#-------------------------------------------------------
#Ejercicio 9
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
#-------------------------------------------------------
#Ejercicio 10
productos=[]
produ=0
sumac=0
mas_vendido=0
ventas=[
    [12, 5, 7, 9, 3, 14, 6],
    [8, 10, 4, 11, 6, 2, 13],
    [3, 16, 1, 8, 12, 8, 5],
    [15, 6, 10, 4, 7, 11, 2]
]
for fila in range(len(ventas)):
    suma=sum(ventas[fila])
    productos.append(suma)
    print(f"Producto {fila+1} vendio un total de {suma} unidades.")

for columna in range(len(ventas[0])):
    sumab=0
    for fila in range(len(ventas)):
       sumab+=ventas[fila][columna]
    print(f"El dia {columna+1} tuvo un total de {sumab} ventas.")

for i in range(len(productos)):
    if productos[i]>produ:
        produ=productos[i]
        mas_vendido=i
        
print(f"El producto mas vendido de la semana fue el {mas_vendido+1}")