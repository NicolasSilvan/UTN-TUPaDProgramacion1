productos=[]
for i in range(1, 6):
    producto=input("Escriba el producto: ")
    productos.append(producto)
    
lista_ordenada=sorted(productos)
print(lista_ordenada)

while True:
    decision=input("Desea eliminar algun producto del carrito? S/N ").lower()
    if decision == "si" or decision == "s":
        otro=int(input("Escriba un numero del 1 al 5 dependiendo que producto desee eliminar "))
        otro-=1
        print(f"Ha eliminado {lista_ordenada[otro]} de la lista")
        del lista_ordenada[otro]
        print(lista_ordenada)
    elif decision == "no" or decision == "n":
        break