"""
Ejercicio propuesto 01 - __str__, __repr__ y __eq__
Nivel: básico

Los métodos mágicos (o especiales) tienen doble guion bajo al inicio y al
final. Python los llama solo en ciertas situaciones:
    str(objeto) y print(objeto)  -> __str__   (texto para el usuario)
    repr(objeto) y la consola    -> __repr__  (texto para el programador)
    objeto1 == objeto2           -> __eq__

Requisitos. Crea la clase Punto(x, y):
1. __str__: "(3, 4)"
2. __repr__: "Punto(3, 4)"  (idealmente, el texto de repr sirve para
   volver a crear el objeto)
3. __eq__: dos puntos son iguales si tienen las mismas coordenadas. Si se
   compara con algo que no es un Punto, retorna NotImplemented.
4. distancia_al_origen(): raíz de x² + y².

Pregunta para pensar: sin __eq__, ¿qué compara Python cuando escribes
Punto(1, 2) == Punto(1, 2)?

Conceptos: representación de objetos, igualdad, NotImplemented.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    p = Punto(3, 4)
    assert str(p) == "(3, 4)"
    assert repr(p) == "Punto(3, 4)"
    assert f"{p}" == "(3, 4)"
    assert repr([Punto(1, 2)]) == "[Punto(1, 2)]", "Las listas usan repr de sus elementos"

    assert Punto(1, 2) == Punto(1, 2)
    assert Punto(1, 2) != Punto(2, 1)
    assert (Punto(1, 2) == (1, 2)) is False
    assert p.distancia_al_origen() == 5

    print("Todas las pruebas pasaron")
