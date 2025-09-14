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