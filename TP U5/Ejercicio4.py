datos=[1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos=[]
for i in datos:
    if i not in sin_repetidos:
        sin_repetidos.append(i)

print(sin_repetidos)