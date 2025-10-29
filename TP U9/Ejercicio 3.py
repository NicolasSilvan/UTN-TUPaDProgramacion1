def potencia(num,pot):
    if pot == 0:
        return 1
    else:
        return num*potencia(num, pot-1)

num=int(input("Ingrese un numero: "))
pot=int(input("Ingrese otro numero: "))
print(potencia(num,pot))