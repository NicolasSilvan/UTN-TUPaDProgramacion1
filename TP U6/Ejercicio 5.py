def es_primo(num):
    for divisor in range(2, int(num**0.5)+1):
        if num%divisor==0:
            return False
    return True

num=int(input("Ingrese un numero: "))
resultado=es_primo(num)
if resultado == True:
    print(f"{num} es un numero primo.")
else:
    print(f"{num} no es un numero primo.")