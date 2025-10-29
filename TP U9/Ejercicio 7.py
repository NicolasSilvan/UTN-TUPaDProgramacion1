def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

n=int(input("Ingrese un numero: "))
print(f"Necesita {contar_bloques(n)} bloques para construir la piramide.")