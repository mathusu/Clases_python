#Es una calculadora solo que el resultado es la cantidad de palabras que aparece
num1 = float(input("Ingrese un numero: ")) #input numero 1
num2 = float(input("Ingrese un numero: ")) #input numero 2
op = input("Ingresa la operacion: ") #tipo de operacion
if op == "+":
    num3 = num1 + num2
elif op == "-":
    num3 = num1 - num2
elif op == "/":
    num3 = num1 / num2
elif op == "*":
    num3 = num1 * num2
else:
    print("Hubo un error al ejecutar la calculadora")
lista = [] 

num3redondo = round(num3) # otra forma de quitarle la coma al numero no hace falta usar las dos
Decimassas = num3 - num3redondo
if num3 < 0:
    num3 = num3 * -1
    for i in range(int(num3)): #el int es para redondear el numero y quitarle una coma porque sino da error
        lista.append("Sas")
    print(lista)
    print("con {:.1f} decimas sas".format(Decimassas))
else:
    for i in range(int(num3redondo)): #el int es para redondear el numero y quitarle una coma porque sino da error
            lista.append("✌️") # el .append es para agregar a la lista
    
    print(lista)
    
    print("con {:.1f} decimas ses".format(Decimassas)) #El .1f es para poner decimas queres en este caso una
# y el .format es lo que edita