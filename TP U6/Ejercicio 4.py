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