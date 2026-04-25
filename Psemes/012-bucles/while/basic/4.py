#Ejercicio 4: Sumar hasta un límite con break
suma = 0

while True:
    numero = int(input("Introduce un número: "))
    suma += numero
    if suma >= 10:
        print(f"La suma ha alcanzado o superado {suma}.")
        break  # Rompemos el ciclo
    print("Suma actual:", suma)
