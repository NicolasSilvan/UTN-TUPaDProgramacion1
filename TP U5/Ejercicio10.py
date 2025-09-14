productos=[]
produ=0
sumac=0
mas_vendido=0
ventas=[
    [12, 5, 7, 9, 3, 14, 6],
    [8, 10, 4, 11, 6, 2, 13],
    [3, 16, 1, 8, 12, 8, 5],
    [15, 6, 10, 4, 7, 11, 2]
]
for fila in range(len(ventas)):
    suma=sum(ventas[fila])
    productos.append(suma)
    print(f"Producto {fila+1} vendio un total de {suma} unidades.")

for columna in range(len(ventas[0])):
    sumab=0
    for fila in range(len(ventas)):
       sumab+=ventas[fila][columna]
    print(f"El dia {columna+1} tuvo un total de {sumab} ventas.")

for i in range(len(productos)):
    if productos[i]>produ:
        produ=productos[i]
        mas_vendido=i
        
print(f"El producto mas vendido de la semana fue el {mas_vendido+1}")