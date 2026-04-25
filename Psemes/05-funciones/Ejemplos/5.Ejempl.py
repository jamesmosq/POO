#Función con número variable de argumentos:

def suma_varios(*numeros):
    return sum(numeros)

print(suma_varios(11, 2, 3))  # Imprime: 6
print(suma_varios(1, 2, 3, 4, 95))  # Imprime: 15