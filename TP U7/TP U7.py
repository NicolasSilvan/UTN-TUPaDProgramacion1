#Ejercicio 1
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300
print(precios_frutas)
#-------------------------------------------------------
#Ejercicio 2
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450,"Naranja": 1200,"Manzana": 1500,"Pera": 2300}
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
print(precios_frutas)
#-------------------------------------------------------
#Ejercicio 3
precios_frutas = {"Banana": 1330, "Ananá": 2500, "Melón": 2800, "Uva": 1450,"Naranja": 1200,"Manzana": 1700,"Pera": 2300}
frutas=[]
frutas.append(precios_frutas.keys())
print(frutas)
#-------------------------------------------------------
#Ejercicio 4
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
#-------------------------------------------------------
#Ejercicio 5
def palabras_unicas(frase):
    palabras_unicas=set()
    palabras=frase.split()
    for palabra in palabras:
        palabras_unicas.add(palabra)
    print(palabras_unicas)
def recuento(frase):
    recuento={}
    palabras=frase.split()
    for palabra in palabras:
        if palabra in recuento:
            recuento[palabra]+=1
        else:
            recuento[palabra]=1
    print(recuento)

frase=input("Ingrese una frase: ")
palabras_unicas(frase)
recuento(frase)
#-------------------------------------------------------
#Ejercicio 6
def promedio(notas):
    return sum(notas)/len(notas)
alumnos={}
for i in range(1, 4):
    lista=[]
    nombre=input("Ingrese el nombre del alumno: ")
    for j in range(1, 4):
        nota=int(input("Ingrese la nota del alumno: "))
        lista.append(nota)
    notas=tuple(lista)
    alumnos[nombre]=notas

print(alumnos)
for nombre, notas in alumnos.items():
    prom=promedio(notas)
    print(f"{nombre}: {prom:.2f}")
#-------------------------------------------------------
#Ejercicio 7
parcial1={1,2,3,4}
parcial2={3,4,5,6}

ambos=parcial1 & parcial2
uno=parcial1 ^ parcial2
almenosuno= parcial1 | parcial2
print("Aprobaron ambos:", ambos)
print("Aprobo almenos uno:", almenosuno)
print("Aprobo solo uno:", uno)
#-------------------------------------------------------
#Ejercicio 8
def consultar_stock():
    producto=input("Que producto quiere consultar? ").title()
    if producto in productos:
        print(f"El producto {producto} tiene {productos[producto]} unidades.")
    else:
        print("El producto no existe.")
def agregar_unidad():
    producto=input("Que producto quiere actualizar? ").title()
    if producto in productos:
        unidad=int(input("Cuantas unidades quiere agregar? "))
        productos[producto] += unidad
        print(f"El stock del producto {producto} se actualizo a {productos[producto]} unidades.")
    else:
        print("El producto no existe.")
def nuevo_producto():
    producto=input("Indique el nombre del nuevo producto: ").title()
    if producto not in productos:
        productos[producto]=0
        print(f"Se ha añadido {producto} a la lista de productos.")
    else:
        print("El producto ya existe.")
productos={}

print("Presiona 1, para consultar el stock.")
print("Presiona 2, para agregar unidades al stock.")
print("Presiona 3, para añadir un nuevo producto.")
print("Presione 4, para salir.")

while True:
    sel=(int(input("Seleccione una opcion: ")))
    match sel:
        case 1:
            consultar_stock()
        case 2:
            agregar_unidad()
        case 3:
            nuevo_producto()
        case 4:
            break
        case _:
            print("Opcion no valida. Intente de nuevo")
#-------------------------------------------------------
#Ejercicio 9
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
#-------------------------------------------------------
#Ejercicio 10
paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio",
    "Brasil": "Brasilia"
}
invertido={}
def invertir():
    for pais, capital in paises.items():
        invertido[capital]=pais
invertir()
for capital, pais in invertido.items():
    print(f"{capital}: {pais}")