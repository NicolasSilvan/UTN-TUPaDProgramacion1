edad=int(input("Ingrese su edad: "))

if edad<12:
    print("Es un niño/a")
elif edad>=12 and edad<18:
    print("Es un adolescente")
elif edad>=18 and edad<30:
    print("Es un adulto/a joven")
elif edad>=30:
    print("Es un adulto/a")