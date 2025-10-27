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