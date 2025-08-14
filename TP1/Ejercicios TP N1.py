# Trabajo Practico N°1

#Nicolas Silvan

#Ejercicio 1
print("Hola Mundo!");

#Ejercicio 2
nombre = input("Ingrese su nombre: ");
print(f"Hola {nombre}!");

#Ejercicio 3
nombre = input("Ingrese su nombre: ");
apellido = input("Ingrese su apellido: ");
edad = input("Ingrese su edad: ");
residencia = input("Ingrese su lugar de residencia: ");
nombre_completo = nombre + " " + apellido;
print(f"Soy {nombre_completo}, tengo {edad} años y vivo en {residencia}");

#Ejercicio 4
radio = int(input("Ingrese el radio del circulo: "));
pi = 3.14159;
area = pi * (radio**2);
perimetro = 2*pi*radio;
print(f"El area del circulo es {area} y el perimetro es {perimetro}");

#Ejercicio 5
segundos = int(input("Escriba una cantidad de segundos: "));
horas = segundos / 60;
print(f"Esos segundos equivalen a {horas} horas");

#Ejercicio 6
numero = int(input("Escriba un numero: "));
contador = 1;
while contador <= 10:
    resultado = numero * contador;
    print(f"{numero}*{contador}={resultado}");
    contador = contador+1;

#Ejercicio 7
while True:
    num = int(input("Seleccione su primer numero: "));
    nums = int(input("Seleccione su segundo numero: "));
    if num == 0 or nums == 0 :
        print("Ingrese denuevo:");
    else:
        break;
resultadoS=num+nums;
resultadoR=num-nums;
resultadoD=num/nums;
resultadoM=num*nums;
print(f"Los resultados son, Suma: {resultadoS}, Resta: {resultadoR}, Division: {resultadoD} y Multiplicación: {resultadoM}");

#Ejercicio 8
altura = float(input("Ingrese su altura: "));
peso = int(input("Ingrese su peso: "));
imc = peso/(altura**2);
print(f"Su IMC es de: {imc}");

#Ejercicio 9
celcius = int(input("Ingrese su temperatura en grados Celcius: "));
fahrenheit = celcius*9/5+32;
print (f"Su temperatura en Fahrenheit seria de: {fahrenheit} °F");

#Ejercicio 10
numa = int(input("Escriba su primer numero: "));
numb = int(input("Escriba su segundo numero: "));
numc = int(input("Escriba su tercer numero: "));
promedio = numa+numb+numc;
promedio = promedio/3;
print(f"Su promedio seria de: {promedio}");