def promedio_calificaciones(lista):
    if not lista:
        return 0
    suma=0
    for i in lista:
        suma+=i
    resultado=suma/len(lista)
    return resultado
        
notas=[]
while True:
    nota=float(input("Ingrese una nota: "))
    if 0<= nota <=10:
        notas.append(nota)
    else:
        print("Numero fuera de rango. Elija otro numero entre 0 y 10")
    otro=input("Desea ingresar otra nota? s/n ").lower()
    if otro == "n":
        break
respuesta=promedio_calificaciones(notas)
print(f"El promedio es {respuesta}")