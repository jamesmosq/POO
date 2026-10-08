"""
Solución - Ejercicio para corregir 02 - División con mensajes

CORRECCIÓN 1 (UnboundLocalError: cannot access local variable 'resultado'):
la línea del mensaje de éxito se ejecutaba siempre, incluso cuando la
división había fallado y resultado no existía. Esa línea va en el bloque
else, que solo corre si no hubo error.

CORRECCIÓN 2 (mensaje incorrecto con divisor cero): los except se revisan
en orden. Exception atrapa casi todo, incluido ZeroDivisionError, así que
el segundo except nunca se alcanzaba. Los errores específicos van primero.
Además, es mejor atrapar el error exacto (ValueError) que Exception.
"""

def dividir(a, b):
    try:
        resultado = float(a) / float(b)
    except ZeroDivisionError:  # CORRECCIÓN 2
        mensaje = "No se puede dividir entre cero"
    except ValueError:  # CORRECCIÓN 2
        mensaje = "Los datos deben ser números"
    else:
        mensaje = f"Resultado: {resultado}"  # CORRECCIÓN 1
    return mensaje


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert dividir("10", "4") == "Resultado: 2.5"
    assert dividir("10", "0") == "No se puede dividir entre cero", dividir("10", "0")
    assert dividir("10", "x") == "Los datos deben ser números"

    print("Todas las pruebas pasaron")
