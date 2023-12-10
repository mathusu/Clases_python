presio = 345
lista = [100, 50, 20, 10, 1, 0.1]

def devolver(precio, billetes):
    for billete in range(len(billetes)):
        vuelto = precio // billetes[billete]
        precio = precio % billetes[billete]
        print(f"{vuelto} billetes de {billetes[billete]}")

devolver(presio, lista)