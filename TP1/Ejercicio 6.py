numero = int(input("Escriba un numero: "));
contador = 1;
while contador <= 10:
    resultado = numero * contador;
    print(f"{numero}*{contador}={resultado}");
    contador = contador+1;