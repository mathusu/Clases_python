def imprimir_matriz(mensaje1,matriz):
    mensaje=mensaje1 + "\n"+"\t"
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            mensaje+=str(matriz[i][j])+ "\t"
        mensaje+="\n"+"\t"
    print(mensaje)
numero1= float(input("Primer numero de la matriz"))
numero2= int(input("Segundo numero de la matriz"))
numero3= int(input("Tercer numero de la matriz"))
numero4= int(input("Cuarto numero de la matriz"))
numero12= int(input("Primer numero de la segunda matriz"))
numero22= int(input("Segundo numero de la segunda matriz"))
numero32= int(input("Tercer numero de la segunda matriz"))
numero42= int(input("Cuarto numero de la segunda matriz"))

matriz1=[[numero1,numero2],[numero3,numero4]]
matriz2=[[numero12,numero22], [numero32,numero42]]

filas=len(matriz1)
columnas=len(matriz1[1])

suma=[]
for i in range(filas):
    suma.append([0]*columnas)
    for j in range(columnas):
        suma[i][j]=matriz1[i][j]+matriz2[i][j]

print("Resultados")
imprimir_matriz("Matriz 1:",matriz1)
imprimir_matriz("Matriz 2:",matriz2)
imprimir_matriz("Suma:",suma)  