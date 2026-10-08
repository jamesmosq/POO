def obtener_numeros_unicos():
    numeros = []
    while len(numeros) < 3:
        try:
            num = int(input(f"Ingrese el número {len(numeros) + 1}: "))
            if num in numeros:
                print("Este número ya fue ingresado. Por favor, ingrese un número diferente.")
            else:
                numeros.append(num)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    return numeros

def analizar_numeros(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    suma = sum(numeros)
    promedio = suma / len(numeros)
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    print(f"Análisis de los números {numeros}:")
    print(f"El mayor número es: {mayor}")
    print(f"El menor número es: {menor}")
    print(f"La suma de los números es: {suma}")
    print(f"El promedio de los números es: {promedio:.2f}")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")

    if len(pares) > len(impares):
        print("Hay más números pares que impares.")
    elif len(pares) < len(impares):
        print("Hay más números impares que pares.")
    else:
        print("Hay igual cantidad de números pares e impares.")

numeros = obtener_numeros_unicos()
analizar_numeros(numeros)