def añadir_horario(tupla, evento):
    agenda[tupla]=evento
def consultar_agenda():
    dia=input("Ingrese el dia: ").title()
    hora=input("Ingrese la hora: ")
    if (dia, hora) in agenda:
        print(f"Ese dia tiene {agenda[(dia,hora)]}")
    else:
        print("No hay ningun evento en ese horario.")
agenda={}
while True:
    dia=input("Ingrese el dia: ").title()
    hora=input("Ingrese la hora(Hora:Minuto): ")
    evento=input("Que evento tiene ese dia? ").title()
    fecha=(dia, hora)
    añadir_horario(fecha, evento)
    salir=input("Quiere ingresar otro evento a la agenda? S/N ").lower()
    if salir == "n":
        break
print(agenda)
consulta=input("Quiere consultar un horario en especifico? S/N ").lower()
if consulta == "s":
    consultar_agenda()