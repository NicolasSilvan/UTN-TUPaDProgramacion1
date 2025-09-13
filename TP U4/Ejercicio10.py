num=int(input("Ingrese un numero: "))
digito=0
numb=0
while num != 0:
    digito=num%10
    num=num//10
    numb=numb*10+digito

print(f"Tu numero invertido es: {numb}")