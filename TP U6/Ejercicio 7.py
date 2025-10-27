def validar_entrada(num):
    if num >= 0:
        return True
    else:
        return False
def factorial(num):
    multi=1
    for i in range(1, num+1):
        multi*=i
    return multi

num=int(input("Ingrese un numero: "))
val=validar_entrada(num)
if val == True:
    resultado=factorial(num)
    print(f"El factorial de {num} es {resultado}")
else:
    print("Numero erroneo, no es un numero entero positivo.")