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