def binario(num):
    if num < 2:
        return str(num)
    else:
        return binario(num // 2)+str(num%2)

num=int(input("Ingrese un numero: "))
print(binario(num))