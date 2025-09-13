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