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