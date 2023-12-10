while  True: 
    pos = int(input("ingrese posicion del numero de fibonacci requerido: "))
    r1 = 0
    r2 = 1

    for xd in range (pos):
        r3 = r1 + r2
        r1 = r2
        r2 = r3
        print(r1)
    if pos == 0:
        print (r1)

    lel = str(input("desea seguir operando? "))
    if lel == "no":
        break
    elif lel == "si":
        pass 
    elif lel == "sas": 
        print("sos un gracioso")
        break
    else:  
        print("NO RECONOSE PAPAPAPAU")
        break