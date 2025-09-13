cantidad=100
par=0
impar=0
positivo=0
negativo=0
for i in range(1, cantidad+1):
    num=int(input("Ingrese un numero: "))
    if num % 2 == 0:
        par+=1
    elif num % 2 != 0:
        impar+=1

    if num<0:
        negativo+=1
    elif num>=0:
        positivo+=1

print(f"Hay {par} numeros pares, {impar} impares, {positivo} positivos y {negativo} negativos")