"""
Ejercicio para corregir 01 - Tuplas e índices
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    - mover_en_x(punto, desplazamiento): recibe un punto (x, y) como tupla y
      retorna un punto NUEVO con x desplazado.
          mover_en_x((1, 2), 5) -> (6, 2)
    - ultima_nota(notas): retorna el último elemento de la lista.
          ultima_nota([3.0, 4.5, 4.0]) -> 4.0

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def mover_en_x(punto, desplazamiento):
    punto[0] = punto[0] + desplazamiento
    return punto


def ultima_nota(notas):
    return notas[len(notas)]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    origen = (1, 2)
    assert mover_en_x(origen, 5) == (6, 2)
    assert origen == (1, 2)

    assert ultima_nota([3.0, 4.5, 4.0]) == 4.0
    assert ultima_nota([5]) == 5

    print("Todas las pruebas pasaron")
