def promedio(notas):
    return sum(notas)/len(notas)
alumnos={}
for i in range(1, 4):
    lista=[]
    nombre=input("Ingrese el nombre del alumno: ")
    for j in range(1, 4):
        nota=int(input("Ingrese la nota del alumno: "))
        lista.append(nota)
    notas=tuple(lista)
    alumnos[nombre]=notas

print(alumnos)
for nombre, notas in alumnos.items():
    prom=promedio(notas)
    print(f"{nombre}: {prom:.2f}")