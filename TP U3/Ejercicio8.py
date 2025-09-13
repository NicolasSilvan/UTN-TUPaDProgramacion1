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