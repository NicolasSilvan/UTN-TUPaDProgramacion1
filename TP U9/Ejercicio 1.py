def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
numeros=[]
num=int(input("Ingrese un numero: "))
for i in range(1, num+1):
    numeros.append(i)
for j in numeros:
    print(f"{j}!= {factorial(j)}")