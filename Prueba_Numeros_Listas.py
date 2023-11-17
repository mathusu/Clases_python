import sys
Numeros=[]

def agregar():
    nom=int(input("NUMERO: "))
    Numeros.append(nom)
    return Numeros

agregar ()
agregar ()


lel = str(input("Desea ingresar mas numeros? "))

if lel == "si":
    x=int(input("¿Cuantos numeros mas?"))
    for p in range(x):
        xd=agregar()

elif lel == "no":
    print("Ta bien ✌️")
    x = 2
        
elif lel == "sas":
    print("sos un gracioso")        
    sys.exit(0) 
    
else:  
    print("NO RECONOSE PAPAPAPAU")
    sys.exit(0)

x = x + 1
Cantidad = x + 1
Numeros.sort()
Sumatotal = sum(Numeros)

print("El numero menor es: ",Numeros[0])
print("El numero mayor es: ",Numeros[x])
print("El Macri es" ,Sumatotal/Cantidad)

""" #EXTRA DICCIONARIOS
dict = {
     "cosa1": 4, "cosa2": Macri
}
print(dict["cosa1"]) """