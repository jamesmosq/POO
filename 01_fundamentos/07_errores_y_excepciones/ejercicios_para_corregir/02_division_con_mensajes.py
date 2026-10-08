"""
Ejercicio para corregir 02 - División con mensajes
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    dividir(a, b) recibe dos textos, los convierte a número y retorna un
    mensaje:
        dividir("10", "4")  -> "Resultado: 2.5"
        dividir("10", "0")  -> "No se puede dividir entre cero"
        dividir("10", "x")  -> "Los datos deben ser números"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def dividir(a, b):
    try:
        resultado = float(a) / float(b)
    except Exception:
        mensaje = "Los datos deben ser números"
    except ZeroDivisionError:
        mensaje = "No se puede dividir entre cero"
    mensaje = f"Resultado: {resultado}"
    return mensaje


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert dividir("10", "4") == "Resultado: 2.5"
    assert dividir("10", "0") == "No se puede dividir entre cero", dividir("10", "0")
    assert dividir("10", "x") == "Los datos deben ser números"

    print("Todas las pruebas pasaron")
