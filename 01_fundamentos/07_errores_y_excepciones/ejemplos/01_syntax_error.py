#1.SyntaxError: Calculadora simple con error de sintaxis

# Versión con error de sintaxis.
# El error clásico es usar '=' (asignación) en lugar de '==' (comparación):
#
#     if operacion = "+":
#                  ^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
#
# La función de abajo ya tiene la comparación escrita correctamente para que el
# archivo pueda ejecutarse. Cambia '==' por '=' en la primera condición y ejecuta
# para ver el error.
def calculadora_con_error():
    operacion = input("Ingrese la operación (+, -, *, /): ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == "+":  # Aquí se comete el error si se escribe '='
        print(f"Resultado: {num1 + num2}")
    elif operacion == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacion == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacion == "/":
        print(f"Resultado: {num1 / num2}")
    else:
        print("Operación no válida")


# Versión corregida y mejorada con manejo de excepciones
def calculadora_corregida():
    try:
        operacion = input("Ingrese la operación (+, -, *, /): ")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            resultado = num1 / num2
        else:
            raise ValueError("Operación no válida")

        print(f"Resultado: {resultado}")

    except ValueError as e:
        if str(e) == "Operación no válida":
            print(e)
        else:
            print("Error: Por favor, ingrese números válidos.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# Ejecutar la calculadora
if __name__ == "__main__":
    print("Calculadora con error de sintaxis (comentada para evitar la interrupción del programa)")
    # calculadora_con_error()  # Esto causaría un SyntaxError

    print("\nCalculadora corregida y mejorada:")
    calculadora_corregida()