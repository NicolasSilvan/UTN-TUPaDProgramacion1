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