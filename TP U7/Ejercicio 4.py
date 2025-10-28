contactos={}
for i in range(1,6):
    nombre=input("Ingrese el nombre del contacto: ")
    numero=input("Ingrese el numero de telefono: ")
    contactos[nombre]=numero

while True:
    busca=input("Ingrese el nombre del contacto: ")
    if busca in contactos:
        print(f"El numero de contacto que busca es: {contactos[busca]}")
        break
    else:
        print("Ese contacto no existe, intente de nuevo.")