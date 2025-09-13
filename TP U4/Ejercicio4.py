print("Ingrese numeros enteros de uno en uno. Para obtener el resultado de la suma, ingrese 0.")
suma=0

while True:
    num=int(input("Ingrese un numero:"))
    suma=num+suma
    if num == 0:
        break

print(f"El total de su suma es: {suma}")