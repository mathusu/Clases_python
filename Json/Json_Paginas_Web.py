import requests # carpeta para sacar cosas de una pagina web

# Para fijarme bien las cosas voy a el link fijate developer tolls, network refresca la pagina y ahi sale
r = requests.get("https://randomuser.me/api?results=1") #sacar un dato de una pagina web y lo guardo en r
#Numero al final = cantidad gente

retorno = r.json() #Ese dato lo pasas de jrson a python y se lo das a retorno
print(retorno["results"][0]["name"]["first"]) #Dentro de la lista se busca en results luego en 0, name y first


# Esta de aca es la version para varias personas
r = requests.get("https://randomuser.me/api?results=7") #sacar un dato de una pagina web y lo guardo en r
#Numero al final = cantidad gente
retornomultiple = r.json()

listaxd = [] 
for x in range(7): #El bucle se repite 7 veces porque es la misma cantidad de gente
    #cada que pasa el bucle se le suma 1 a x
    listaqueseborra = [] #Esta se borra lo de adentro porque siempre se va editando cada que pasa borrandola
    listaxd.append(retornomultiple["results"][x]["name"]["first"]) 
    listaqueseborra.append(retornomultiple["results"][x]["name"]["first"]) 

listaordenada =sorted(listaxd) #Sorted es para ordenar la lista

print(listaxd) # se muestra en la lista
print(listaordenada)
print(listaqueseborra)