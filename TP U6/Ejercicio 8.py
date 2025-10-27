def es_divisible(num, div):
    return num%div==0
def es_primo(num):
    if num<2:
        return False
    for i in range(2, num):
        if es_divisible(num, i):
            return False
    return True

num=int(input("Ingrese un numero: "))
resultado=es_primo(num)
if resultado == True:
    print(f"{num} es un numero primo.")
else:
    print(f"{num} no es un numero primo.")