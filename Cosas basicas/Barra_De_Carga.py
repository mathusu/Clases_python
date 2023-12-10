porcentaje = "---------------------------------------------------------------------------------------------------."
x = 0 
y = 0
for i in porcentaje:
    x = x + 1
    y = y + 1
    print(porcentaje[0:x],"%", y)

for i in porcentaje:
    x = x - 1
    y = y - 1
    print(porcentaje[0:x],"%", y)

x = 5

porcentaje = porcentaje[0:x]
print(porcentaje)