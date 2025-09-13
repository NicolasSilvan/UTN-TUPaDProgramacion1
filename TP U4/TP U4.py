#Ejercicio 1
for i in range(0, 101):
    print(i)
#-------------------------------------------------------
#Ejercicio 2
import math

num=int(input("Ingrese un numero: "))
if num == 0:
    longitud = 1
elif num<0:
    positivo=abs(num)
    longitud=int(math.log10(positivo))+1
else:
    longitud=int(math.log10(num))+1
    
print(f"La cantidad de digitos es {longitud}")
#-------------------------------------------------------
#Ejercicio 3
numa=int(input("Ingrese un numero: "))
numb=int(input("Ingrese otro numero: "))
inicio=min(numa, numb)+1
fin=max(numa, numb)

suma=0
for i in range(inicio, fin):
    suma=suma+i
print(f"El resultado de su suma es: {suma}")
#-------------------------------------------------------
#Ejercicio 4
print("Ingrese numeros enteros de uno en uno. Para obtener el resultado de la suma, ingrese 0.")
suma=0

while True:
    num=int(input("Ingrese un numero:"))
    suma=num+suma
    if num == 0:
        break

print(f"El total de su suma es: {suma}")
#-------------------------------------------------------
#Ejercicio 5
import random
print("Adivina el numero entre 0 y 9")
intento=0
numero_aleatorio=random.randint(0, 9)

while True:
    intento+=1
    num=int(input("Ingrese un numero: "))
    if num == numero_aleatorio:
        break
    else:
        print("Buen intento, intente nuevamente")

print(f"Fueron {intento} intentos para adivinar {numero_aleatorio}")
#-------------------------------------------------------
#Ejercicio 6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)
#-------------------------------------------------------
#Ejercicio 7
num=int(input("Ingrese un numero: "))
suma=0
for i in range(0, num):
    suma+=i
    
print(suma)
#-------------------------------------------------------
#Ejercicio 8
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
#-------------------------------------------------------
#Ejercicio 9
cantidad=100
suma=0
for i in range(1, cantidad+1):
    num=int(input("Ingrese un numero: "))
    suma+=num

resultado=suma/cantidad
print(f"El promedio es {resultado}")
#-------------------------------------------------------
#Ejercicio 10
num=int(input("Ingrese un numero: "))
digito=0
numb=0
while num != 0:
    digito=num%10
    num=num//10
    numb=numb*10+digito

print(f"Tu numero invertido es: {numb}")