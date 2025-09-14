lista=[ 6, 8, 4, 2, 7, 9, 8, 10, 5, 6]
suma=0
for i in range(len(lista)):
    suma=suma+lista[i]
    print(f"Estudiante N°{i+1}: Nota {lista[i]}")
notaa=max(lista)
notab=min(lista)
promedio=suma/len(lista)
print(f"La nota mas alta es: {notaa}, la mas baja es: {notab} y el promedio de todas las notas es: {promedio}")