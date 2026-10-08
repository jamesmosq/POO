"""
Ejercicio propuesto 02 - Vector con operadores
Nivel: intermedio

Con métodos mágicos, los operadores +, -, *, abs() funcionan con tus
propios objetos (sobrecarga de operadores).

Requisitos. Crea la clase Vector(x, y):
1. __add__(otro):  Vector(1, 2) + Vector(3, 4) -> Vector(4, 6)
2. __sub__(otro):  Vector(3, 4) - Vector(1, 1) -> Vector(2, 3)
3. __mul__(escalar): Vector(1, 2) * 3 -> Vector(3, 6)
4. __rmul__(escalar): 3 * Vector(1, 2) -> Vector(3, 6)
   (Python llama a __rmul__ cuando el objeto está a la DERECHA del
   operador y el de la izquierda no sabe operar con él.)
5. __abs__: magnitud del vector: raíz de x² + y².
6. __eq__ y __repr__ ("Vector(4, 6)").

Todos los operadores retornan un Vector NUEVO; no modifican los originales.

Conceptos: sobrecarga de operadores, __add__, __mul__, __rmul__, __abs__.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    a = Vector(1, 2)
    b = Vector(3, 4)

    assert a + b == Vector(4, 6)
    assert b - a == Vector(2, 2)
    assert a * 3 == Vector(3, 6)
    assert 3 * a == Vector(3, 6)
    assert abs(b) == 5
    assert repr(a + b) == "Vector(4, 6)"
    assert a == Vector(1, 2), "Los operadores no deben modificar los originales"

    print("Todas las pruebas pasaron")
