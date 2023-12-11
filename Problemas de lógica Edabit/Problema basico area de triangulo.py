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
