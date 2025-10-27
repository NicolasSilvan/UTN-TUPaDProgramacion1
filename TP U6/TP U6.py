#Ejercicio 1
def tabla_multiplicar(num, rango):
    tabla=[]
    if num < 0 or rango < 0:
        print("Error: Numero negativo, Intente denuevo")
        return
    for i in range(1, rango+1):
        resultado=num*i
        tabla.append(resultado)
    print(tabla)    

num=int(input("Escriba un numero: "))
rango=int(input("Ingrese el multiplicador: "))
tabla_multiplicar(num, rango)
#-------------------------------------------------------
#Ejercicio 2
def suma_pares(lista):
    suma=0
    for i in lista:
        if i % 2 == 0:
            suma+=i
    print(f"{lista} = {suma}")

lista=[]
while True:
    numlista=int(input("Ingresa los numeros para la lista (0 para salir) "))
    if numlista == 0:
        break
    lista.append(numlista)

if not lista:
    print("No hay numeros para sumar en la lista")
else:
    suma_pares(lista)
#-------------------------------------------------------
#Ejercicio 3
def rectangulo(longitud, anchura):
    area=longitud*anchura
    perimetro=2*(longitud+anchura)
    tupla=(area, perimetro)
    return tupla

while True:
    long=(int(input("Ingrese la longitud del rectangulo: ")))
    ancho=(int(input("Ingrese el ancho del rectangulo: ")))
    if long > 0 and ancho > 0:
        area, perimetro=rectangulo(long, ancho)
        print(f"El area del rectangulo es {area} y el perimetro es {perimetro}")
        if long == ancho:
            print("Este rectangulo es un cuadrado.")
        break
    else:
        print("Las dimensiones deben ser mayores a 0.")
#-------------------------------------------------------
#Ejercicio 4
def convertir_temperatura(celcius):
    fahrenheit=celcius*9/5+32
    kelvin=celcius+273.15
    #Rankine=celcius*9/5+491.67
    #Si quiero añadir otra temperatura, solo tengo que añadir una nueva variable y agrandar un poco el if afuera de la funcion.
    temperatura=(fahrenheit, kelvin)
    return(temperatura)

c=int(input("Ingrese la temperatura en celcius: "))
f, k=convertir_temperatura(c)
while True:
    accion=input("Ingrese que temperatura quiere, K para Kelvin o F para Fahrenheit. ").upper()
    if accion == "K" or accion == "F":
        if accion == "K":
            print(f"La temperatura {c}° seria {k}° en Kelvin")
            break
        elif accion == "F":
            print(f"La temperatura {c}° seria {f}° en Fahrenheit")
            break
    else:
        print("Solo se acepta K o F, Intente nuevamente")
#-------------------------------------------------------
#Ejercicio 5
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
#-------------------------------------------------------
#Ejercicio 6
def promedio_calificaciones(lista):
    if not lista:
        return 0
    suma=0
    for i in lista:
        suma+=i
    resultado=suma/len(lista)
    return resultado
        
notas=[]
while True:
    nota=float(input("Ingrese una nota: "))
    if 0<= nota <=10:
        notas.append(nota)
    else:
        print("Numero fuera de rango. Elija otro numero entre 0 y 10")
    otro=input("Desea ingresar otra nota? s/n ").lower()
    if otro == "n":
        break
respuesta=promedio_calificaciones(notas)
print(f"El promedio es {respuesta}")
#-------------------------------------------------------
#Ejercicio 7
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
#-------------------------------------------------------
#Ejercicio 8
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
#-------------------------------------------------------
#Ejercicio 9
def convertir_a_fahrenheit(num):
    return num*9/5+32
def convertir_a_kelvin(num):
    return num+273.15
def menu_conversion(eleccion, num):
    if eleccion == "f":
        return convertir_a_fahrenheit(num)
    elif eleccion == "k":
        return convertir_a_kelvin(num)
    
num=float(input("Ingrese la temperatura en celsius: "))
temp=input("A que temperatura quiere convertir? F o K ").lower()

while True:
    if temp == "f":
        respuesta=menu_conversion(temp, num)
        print(f"Convirtio {num}° Celsius a {respuesta}° Fahrenheit.")
        break
    elif temp == "k":
        respuesta=menu_conversion(temp, num)
        print(f"Convirtio {num}° Celsius a {respuesta}° Kelvin.")
        break
    else:
        print("Temperatura no valida. Intente denuevo.")
#-------------------------------------------------------
#Ejercicio 10
def validar_dimensiones(longitud, anchura):
    return longitud >=0 and anchura>=0
def calcular_area(longitud, anchura):
    return longitud*anchura
def calcular_perimetro(longitud, anchura):
    return 2*(longitud+anchura)

long=int(input("Ingrese la longitud: "))
ancho=int(input("Ingrese la anchura: "))

validar=validar_dimensiones(long, ancho)
area=calcular_area(long, ancho)
perimetro=calcular_perimetro(long, ancho)
if validar == True:
    print(f"El area del rectangulo es {area} y el perimetro es {perimetro}")
else:
    print("No son dimensiones validas.")