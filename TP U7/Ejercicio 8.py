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