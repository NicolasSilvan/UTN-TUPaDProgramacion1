numa=int(input("Ingrese un numero: "))
numb=int(input("Ingrese otro numero: "))
inicio=min(numa, numb)+1
fin=max(numa, numb)

suma=0
for i in range(inicio, fin):
    suma=suma+i
print(f"El resultado de su suma es: {suma}")