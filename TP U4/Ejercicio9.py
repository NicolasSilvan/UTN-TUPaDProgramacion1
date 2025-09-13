cantidad=100
suma=0
for i in range(1, cantidad+1):
    num=int(input("Ingrese un numero: "))
    suma+=num

resultado=suma/cantidad
print(f"El promedio es {resultado}")