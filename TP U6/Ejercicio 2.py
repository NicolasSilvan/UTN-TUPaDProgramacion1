def suma_pares(lista):
    suma=0
    for i in lista:
        if i % 2 == 0:
            suma+=i
    print(f"{lista} = {suma}")

lista=[]
while True:
    numlista=int(input("Ingresa los numeros para la lista (0 para salir) "))
    if numlista == 0:
        break
    lista.append(numlista)

if not lista:
    print("No hay numeros para sumar en la lista")
else:
    suma_pares(lista)