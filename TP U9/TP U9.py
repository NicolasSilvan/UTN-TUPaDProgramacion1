#Ejercicio 1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
numeros=[]
num=int(input("Ingrese un numero: "))
for i in range(1, num+1):
    numeros.append(i)
for j in numeros:
    print(f"{j}!= {factorial(j)}")
#-------------------------------------------------------
#Ejercicio 2
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

num=int(input("Ingrese un numero: "))
for i in range (0, num+1):
    print(fibonacci(i))
#-------------------------------------------------------
#Ejercicio 3
def potencia(num,pot):
    if pot == 0:
        return 1
    else:
        return num*potencia(num, pot-1)

num=int(input("Ingrese un numero: "))
pot=int(input("Ingrese otro numero: "))
print(potencia(num,pot))
#-------------------------------------------------------
#Ejercicio 4
def binario(num):
    if num < 2:
        return str(num)
    else:
        return binario(num // 2)+str(num%2)

num=int(input("Ingrese un numero: "))
print(binario(num))
#-------------------------------------------------------
#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra=input("Ingrese una palabra: ")
print(es_palindromo(palabra))
#-------------------------------------------------------
#Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10)+ suma_digitos(n // 10)

n=int(input("Ingrese un numero positivo: "))
print(suma_digitos(n))
#-------------------------------------------------------
#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

n=int(input("Ingrese un numero: "))
print(f"Necesita {contar_bloques(n)} bloques para construir la piramide.")
#-------------------------------------------------------
#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            coincidencia = 1
        else:
            coincidencia = 0
        return coincidencia + contar_digito(numero // 10, digito)
    
numero=int(input("Ingresa un numero: "))
digito=int(input("Ingrese un numero entre 0 y 9: "))
if 0 <= digito <= 9:
    print(contar_digito(numero, digito))
else:
    print("Digito invalido.")