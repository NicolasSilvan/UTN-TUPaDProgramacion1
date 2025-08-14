while True:
    num = int(input("Seleccione su primer numero: "));
    nums = int(input("Seleccione su segundo numero: "));
    if num == 0 or nums == 0 :
        print("Ingrese denuevo:");
    else:
        break;
resultadoS=num+nums;
resultadoR=num-nums;
resultadoD=num/nums;
resultadoM=num*nums;
print(f"Los resultados son, Suma: {resultadoS}, Resta: {resultadoR}, Division: {resultadoD} y Multiplicación: {resultadoM}");