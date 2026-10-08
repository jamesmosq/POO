"""
Ejercicio propuesto 01 - Tabla de multiplicar
Nivel: básico

Requisitos:
1. Escribe la función tabla(numero, hasta=10) que retorne una LISTA de
   textos con la tabla de multiplicar:
       tabla(3, 4) -> ["3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9", "3 x 4 = 12"]
2. Usa un ciclo for con range().
3. Al final, imprime la tabla del 7 recorriendo la lista con otro for.

Pista: empieza con una lista vacía (resultado = []) y agrega cada línea con
resultado.append(...).

Conceptos: for, range(inicio, fin), listas, append.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert tabla(3, 4) == ["3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9", "3 x 4 = 12"]
    assert len(tabla(5)) == 10
    assert tabla(5)[-1] == "5 x 10 = 50"
    assert tabla(2, 0) == []

    print("Todas las pruebas pasaron")
