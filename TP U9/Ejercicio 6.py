def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10)+ suma_digitos(n // 10)

n=int(input("Ingrese un numero positivo: "))
print(suma_digitos(n))