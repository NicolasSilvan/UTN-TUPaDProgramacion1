def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra=input("Ingrese una palabra: ")
print(es_palindromo(palabra))