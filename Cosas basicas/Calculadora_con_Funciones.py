def sas(num1, num2, op): #la funcion, esto se utiliza para tenerlo ya escrito y no  tener que volver a copiarlo
    if op == "+":
        owo = num1+num2
    elif op == "-":
        owo = num1-num2
    elif op == "/":
        owo = num1/num2
    elif op == "*":
        owo = num1*num2
    else:
        print("Hubo un error al ejecutar la calculadora")
    return(owo)
imput1 = float(input("Ingrese un numero: ")) #input numero 1
imput2 = float(input("Ingrese un numero: ")) #input numero 2
operacion = input("Ingresa la operacion: ") #tipo de operacion

xd = sas(imput1, imput2, operacion) #para printear el resultado se puede usar esto 
print(xd)

print(sas(imput1, imput2, operacion))# o para acortarlo se puede usar solo esto

def suma(a,b):
    c = a + b
    return(c)
print(suma(imput1, imput2))# esto llama a que se imprima el imput 1 y 2 pero usando la fomra del def suma