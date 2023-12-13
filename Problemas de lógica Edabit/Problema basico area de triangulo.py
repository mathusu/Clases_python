#Problemas básicos de python
#------------------------------------------------------
def tri_area(base, height):
    area = (base * height) / 2
    return area
base= 7
height=7

result_area = tri_area(base, height)

print (result_area)


#------------------------------------------------------
def Divisible(x, y): #Si da 1 no es divisible y 0 divisible
    resultado = x % y
    return resultado

x=40
y=4
resultado= Divisible(x,y)
resultado=round(resultado)
print(resultado)

def addition(a, b):
    x= a + b
    return x


#------------------------------------------------------
def string_int(txt):
    txt = int(txt)
    return txt
txt_str= "90"
txt_int = string_int(txt_str)
print(txt_int)


#------------------------------------------------------
def multiplicación(multiplicando, multiplicador):
    producto= multiplicando*multiplicador
    return producto
x=4
y=5
resultado=multiplicación(x,y)
print(resultado)


#------------------------------------------------------
def dis(descuento,precio):
    nuevo= descuento * precio / 100
    precio_final = precio - nuevo
    return precio_final

descuento = 61
precio = 593
precio_final = dis(descuento, precio)
precio_final = round(precio_final)
print(precio_final)


#------------------------------------------------------
def circuit_power(voltage, current):
	power= current * voltage
	return power
voltage = 40
current = 10
power = circuit_power(voltage, current)
print(power)


#------------------------------------------------------
def calculator(num1, operator, num2):
    if operator == "+":
        owo = num1+num2
    elif operator == "-":
        owo = num1-num2
    elif num2 == 0:
        print("Can't divide by 0!")
    elif operator == "/":
        owo = num1/num2
    elif operator == "*":
        owo = num1*num2
    return owo
num1=1
num2=2
operator=input(str("ingresa lal"))
owo= calculator(num1, operator, num2)
print(owo)


#------------------------------------------------------
from math import pi
import math

def radians_to_degrees(rad):
    result= rad * (180/pi)
    result = round(result,1)
    return result
radial = 60

resultado= radians_to_degrees(radial)
print(resultado)


#------------------------------------------------------
