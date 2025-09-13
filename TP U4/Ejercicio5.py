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