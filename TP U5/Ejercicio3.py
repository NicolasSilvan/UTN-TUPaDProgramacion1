import random
lista=[]
pares=[]
impares=[]
for i in range(1, 16):
    numero_aleatorio=random.randint(1, 100)
    lista.append(numero_aleatorio)

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(f"Hay {len(pares)} numeros pares y {len(impares)} numeros impares.")