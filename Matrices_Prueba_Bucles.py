listamadre= []
fila1=[]
fila2=[]
fila3=[]
fila4=[]
fila5=[]
fila6=[]
fila7=[]
fila8=[]
fila9=[]
fila10=[]

fila1 = (input("Introducir numeros de la fila 1")).split(",")
listamadre.append(fila1)


alto = int(input("Cantidad de filas de alto "))

if alto == 2:
    fila2 = (input("Introducir numeros de la fila 2 ")).split(",")
    listamadre.append(fila2)
elif alto == 3:
    fila2 = (input("Introducir numeros de la fila 2 ")).split(",")
    fila3 = (input("Introducir numeros de la fila 3 ")).split(",")
    listamadre.append(fila2)
    listamadre.append(fila3)
elif alto == 4:
    fila2 = (input("Introducir numeros de la fila 2 ")).split(",")
    fila3 = (input("Introducir numeros de la fila 3 ")).split(",")
    fila4 = (input("Intruducir numeros de la fila 4 ")).split(",")
    listamadre.append(fila2)
    listamadre.append(fila3)
    listamadre.append(fila4)
elif alto == 5:
    fila2 = (input("Introducir numeros de la fila 2 ")).split(",")
    fila3 = (input("Introducir numeros de la fila 3 ")).split(",")
    fila4 = (input("Intruducir numeros de la fila 4 ")).split(",")
    fila5 = (input("Intruducir numeros de la fila 5 ")).split(",")
    listamadre.append(fila2)
    listamadre.append(fila3)
    listamadre.append(fila4)
    listamadre.append(fila5)
elif alto == 6:
    fila2 = (input("Introducir numeros de la fila 2 ")).split(",")
    fila3 = (input("Introducir numeros de la fila 3 ")).split(",")
    fila4 = (input("Intruducir numeros de la fila 4 ")).split(",")
    fila5 = (input("Intruducir numeros de la fila 5 ")).split(",")
    fila6 = (input("Intruducir numeros de la fila 6 ")).split(",")
    listamadre.append(fila2)
    listamadre.append(fila3)
    listamadre.append(fila4)
    listamadre.append(fila5)
    listamadre.append(fila6)
elif alto == 7:
    fila2 = (input("Introducir numeros de la fila 2 ")).split(",")
    fila3 = (input("Introducir numeros de la fila 3 ")).split(",")
    fila4 = (input("Intruducir numeros de la fila 4 ")).split(",")
    fila5 = (input("Intruducir numeros de la fila 5 ")).split(",")
    fila6 = (input("Intruducir numeros de la fila 6 ")).split(",")
    fila7 = (input("Intruducir numeros de la fila 7 ")).split(",")
    listamadre.append(fila2)
    listamadre.append(fila3)
    listamadre.append(fila4)
    listamadre.append(fila5)
    listamadre.append(fila6)
    listamadre.append(fila7)
elif alto == 8:
    fila2 = (input("Introducir numeros de la fila 2 ")).split(",")
    fila3 = (input("Introducir numeros de la fila 3 ")).split(",")
    fila4 = (input("Intruducir numeros de la fila 4 ")).split(",")
    fila5 = (input("Intruducir numeros de la fila 5 ")).split(",")
    fila6 = (input("Intruducir numeros de la fila 6 ")).split(",")
    fila7 = (input("Intruducir numeros de la fila 7 ")).split(",")
    fila8 = (input("Intruducir numeros de la fila 8 ")).split(",")
    listamadre.append(fila2)
    listamadre.append(fila3)
    listamadre.append(fila4)
    listamadre.append(fila5)
    listamadre.append(fila6)
    listamadre.append(fila7)
    listamadre.append(fila8)
elif alto == 9:
    fila2 = (input("Introducir numeros de la fila 2 ")).split(",")
    fila3 = (input("Introducir numeros de la fila 3 ")).split(",")
    fila4 = (input("Intruducir numeros de la fila 4 ")).split(",")
    fila5 = (input("Intruducir numeros de la fila 5 ")).split(",")
    fila6 = (input("Intruducir numeros de la fila 6 ")).split(",")
    fila7 = (input("Intruducir numeros de la fila 7 ")).split(",")
    fila8 = (input("Intruducir numeros de la fila 8 ")).split(",")
    fila9 = (input("Intruducir numeros de la fila 9 ")).split(",")
    listamadre.append(fila2)
    listamadre.append(fila3)
    listamadre.append(fila4)
    listamadre.append(fila5)
    listamadre.append(fila6)
    listamadre.append(fila7)
    listamadre.append(fila8)
    listamadre.append(fila9)
largo1 = len (fila1)
largo2 = len (fila2)
largo3 = len (fila3)
largo4 = len (fila4)
largo5 = len (fila5)
largo6 = len (fila6)
largo7 = len (fila7)
largo8 = len (fila8)
largo9 = len (fila9)

if largo1 == largo2 and largo1 == largo3 and largo1 == largo4 and largo1 == largo5 and largo1 == largo6 and largo1 == largo7 and largo1 == largo6 and largo1 == largo9:
    def print_matrix(matrix):
        for row in matrix:
            print(*row)
    print_matrix(listamadre)
else:
    print("no es igual de ancha en todos los lugares")