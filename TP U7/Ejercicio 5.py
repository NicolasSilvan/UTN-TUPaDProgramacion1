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