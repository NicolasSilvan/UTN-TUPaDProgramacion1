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