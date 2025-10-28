def crear_archivo():
    productos=[
        "Lapicera,120.5,30",
        "Cuaderno,250.0,15",
        "Goma,50.0,40"
    ]
    with open("productos.txt", "w") as archivo:
        for linea in productos:
            archivo.write(linea +"\n")
def leer_y_mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 3:
                nombre, precio, cantidad = partes
                print(f"Producto: {nombre}, Precio: ${precio}, Cantidad: {cantidad}")
def agregar_producto():
    entrada=input("Ingrese nuevo producto (nombre, precio, cantidad): ").strip()
    partes=entrada.split(",")
    if len(partes) == 3:
        with open("productos.txt", "a") as archivo:
            archivo.write(entrada + "\n")
    else:
        print("Formato incorrecto.")
def cargar_productos():
    productos=[]
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            partes=linea.strip().split(",")
            if len(partes) == 3:
                nombre, precio, cantidad = partes
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    return productos
def buscar_producto(productos):
    busqueda = input("Ingrese el producto: ").strip()
    for producto in productos:
        if producto["nombre"].lower() == busqueda.lower():
            print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
            return
    print("Producto no encontrado.")
def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}"
            archivo.write(linea + "\n")

crear_archivo()
leer_y_mostrar_productos()

while True:
    print("1) Mostrar productos")
    print("2) Agregar productos")
    print("3) Buscar productos")
    print("4) Guardar productos")
    print("5) Salir")
    opcion=int(input("Seleccione una opcion: "))
    match opcion:
        case 1:
            leer_y_mostrar_productos()
        case 2:
            agregar_producto()
        case 3:
            productos = cargar_productos()
            buscar_producto(productos)
        case 4:
            productos = cargar_productos()
            guardar_productos(productos)
        case 5:
            break
        case _:
            print("Opcion incorrecta. Intente nuevamente.")