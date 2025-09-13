frase=input("Ingrese una frase: ")
letra=frase[-1]
vocales=["a", "e", "i", "o","u"]

if letra in vocales:
    print(frase + "!")
else:
    print(frase)