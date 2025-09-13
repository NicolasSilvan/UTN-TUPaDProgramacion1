#Ejercicio 1
edad=int(input("Ingrese su edad: "))
if edad>18 :
    print("Es mayor de edad")
else:
    pass
#-------------------------------------------------------
#Ejercicio 2
nota=int(input("Ingrese su nota: "))
if nota>=6 :
    print("Aprobado")
else:
    print("Desaprobado")
#-------------------------------------------------------
#Ejercicio 3
num=int(input("Ingrese un número: "))

if num % 2 == 0 :
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
#-------------------------------------------------------
#Ejercicio 4
edad=int(input("Ingrese su edad: "))

if edad<12:
    print("Es un niño/a")
elif edad>=12 and edad<18:
    print("Es un adolescente")
elif edad>=18 and edad<30:
    print("Es un adulto/a joven")
elif edad>=30:
    print("Es un adulto/a")
#-------------------------------------------------------
#Ejercicio 5
contraseña=input("Ingrese su contraseña: ")
longitud=len(contraseña)

if longitud>=8 and longitud<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#-------------------------------------------------------
#Ejercicio 6
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media= mean(numeros_aleatorios)
mediana= median(numeros_aleatorios)
moda= mode(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Error")
#-------------------------------------------------------
#Ejercicio 7
frase=input("Ingrese una frase: ")
letra=frase[-1]
vocales=["a", "e", "i", "o","u"]

if letra in vocales:
    print(frase + "!")
else:
    print(frase)
#-------------------------------------------------------
#Ejercicio 8
nombre=input("Ingrese su nombre: ")
print("Si quiere su nombre en mayusculas, presione 1")
print("Si quiere su nombre en minusculas, presione 2")
print("Si quiere la primer letra de su nombre en mayuscula, presione 3")
while True:
    num=int(input("Elija una opcion: "))
    match num:
        case 1:
            print(nombre.upper())
            break
        case 2:
            print(nombre.lower())
            break
        case 3:
            print(nombre.title())
            break
        case _:
            print("Numero erroneo, ingrese denuevo")
# #-------------------------------------------------------
#Ejercicio 9
magnitud=int(input("Ingrese la magnitud: "))
if magnitud<3:
    print("Muy leve")
elif magnitud>=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Moderado")
elif magnitud>=5 and magnitud<6:
    print("Fuerte")
elif magnitud>=6 and magnitud<7:
    print("Muy Fuerte")
elif magnitud>=7:
    print("Extremo")
#-------------------------------------------------------
#Ejercicio 10
hemisferio= input("Indique en que hemisferio se encuentra: N/S ").lower()
mes= input("Ingrese el mes: ").lower()
dia= int(input("Ingrese que dia es: "))
while True:
    if hemisferio == "n" or hemisferio == "norte":
        if mes in ["enero", "febrero"] or (mes == "diciembre" and dia>=21) or (mes == "marzo" and dia<=20):
            print("Invierno")
        elif mes in ["abril", "mayo"] or (mes == "marzo" and dia>=21) or (mes == "junio" and dia<=20):
            print("Primavera")
        elif mes in ["julio", "agosto"] or (mes == "junio" and dia>=21) or (mes == "septiembre" and dia<=20):
            print("Verano")
        elif mes in ["octubre", "noviembre"] or (mes == "septiembre" and dia>=21) or (mes == "diciembre" and dia<=20):
            print("Otoño")
        break
    elif hemisferio == "s" or hemisferio == "sur":
        if mes in ["enero", "febrero"] or (mes == "diciembre" and dia>=21) or (mes == "marzo" and dia<=20):
            print("Verano")
        elif mes in ["abril", "mayo"] or (mes == "marzo" and dia>=21) or (mes == "junio" and dia<=20):
            print("Otoño")
        elif mes in ["julio", "agosto"] or (mes == "junio" and dia>=21) or (mes == "septiembre" and dia<=20):
            print("Invierno")
        elif mes in ["octubre", "noviembre"] or (mes == "septiembre" and dia>=21) or (mes == "diciembre" and dia<=20):
            print("Primavera")
        break
    else:
        hemisferio=input("Caracter incorrecto, ingrese denuevo").lower()