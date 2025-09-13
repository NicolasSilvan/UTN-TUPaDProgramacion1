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