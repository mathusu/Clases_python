def ordenarsas():
    cartas.append(carta_nueva)
    for position in range(len(cartas) - 1):
        minimum = position
        for i in range(position+1, len(cartas)):
            if cartas[i] < cartas[minimum]:
                minimum = i
        cartas[position], cartas[minimum] = cartas[minimum], cartas[position]
cartas = [1,4,6,8]
carta_nueva = 7
ordenarsas()
print(cartas)
