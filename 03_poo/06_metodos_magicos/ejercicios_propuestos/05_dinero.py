"""
Ejercicio propuesto 05 - Dinero
Nivel: avanzado

El dinero NO se debe manejar con float: 0.1 + 0.2 da 0.30000000000000004.
Se usa decimal.Decimal, que hace aritmética decimal exacta.

Requisitos. Crea la clase Dinero(cantidad, moneda="COP"):
1. Guarda la cantidad como Decimal(str(cantidad)), para que Dinero(0.1)
   sea exactamente 0.1.
2. __add__ y __sub__: solo entre la misma moneda; si son distintas, lanza
   ValueError. Retornan un Dinero nuevo.
3. __radd__: permite usar sum() con una lista de Dinero. sum() empieza
   sumando 0 + primer_elemento, así que __radd__ debe aceptar el 0.
4. __mul__ por un número (int, float o Decimal).
5. __eq__, __lt__ (misma moneda) y __hash__.
6. __str__: "$1,500.50 COP" (dos decimales, separador de miles).
7. __bool__: False si la cantidad es 0.

Conceptos: Decimal, operadores aritméticos, __radd__, inmutabilidad.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from decimal import Decimal

    assert Dinero(0.1) + Dinero(0.2) == Dinero(0.3), "Con Decimal la suma debe ser exacta"
    assert str(Dinero(1500.5)) == "$1,500.50 COP"
    assert str(Dinero(10, "USD") * 3) == "$30.00 USD"
    assert Dinero(100) - Dinero(30) == Dinero(70)

    precios = [Dinero(1000), Dinero(2500), Dinero(500)]
    assert sum(precios) == Dinero(4000)
    assert max(precios) == Dinero(2500)

    assert not Dinero(0)
    assert Dinero(1)
    assert len({Dinero(5), Dinero(5.0), Dinero(6)}) == 2
    assert Dinero(5).cantidad == Decimal("5")

    try:
        Dinero(1, "COP") + Dinero(1, "USD")
        raise AssertionError("No se pueden sumar monedas distintas")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
