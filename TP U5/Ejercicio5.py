estudiantes=["Emiliano", "Enzo", "Gabriel", "Luciano", "Abigail", "Adrian", "Agustin", "Alejo"]

while True:
    pregunta=input("Quiere agregar un nuevo estudiante o eliminar uno existente? S/N ").lower()
    if pregunta == "si" or pregunta == "s":
        preguntab=int(input("Si desea agregar uno nuevo escriba 1, si desea eliminar uno existente escriba 2 "))
        if preguntab == 1:
            estudiante=input("Ingrese el nombre del estudiante que quiere añadir a la lista ").title()
            estudiantes.append(estudiante)
            print(estudiantes)
        elif preguntab == 2:
            print(estudiantes)
            estudianteb=int(input("Ingrese con numeros que estudiante de la lista quiere eliminar "))
            del estudiantes[estudianteb-1]
            print(estudiantes)
    elif pregunta == "no" or pregunta == "n":
        print(f"Esta es la lista despues de los cambios, {estudiantes}")
        break