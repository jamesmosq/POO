#Llenar una lista con números pares hasta un límite:

pares = []
numero = 1
limite = 10

while numero <= limite:
    if numero % 2 == 0:
        pares.append(numero)
    numero += 1

print("Números pares hasta", limite, ":", pares)
