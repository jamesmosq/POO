"""
Ejercicio propuesto 02 - Figuras geométricas
Nivel: básico

Vas a modelar figuras que comparten comportamiento: todas tienen un nombre,
calculan su área y se describen de la misma forma.

Requisitos:
1. Crea la clase Figura que reciba un nombre. Debe tener:
   - area(): retorna 0 (cada figura concreta lo sobrescribe).
   - describir(): retorna el nombre y el área con dos decimales, por ejemplo:
         "Rectángulo con área 20.00"
2. Crea Rectangulo(base, altura), que herede de Figura con el nombre
   "Rectángulo" y sobrescriba area().
3. Crea Circulo(radio), que herede de Figura con el nombre "Círculo".
   Usa math.pi para el área.
4. Crea Cuadrado(lado), que herede de Rectangulo. No vuelvas a escribir
   area(): llama a super().__init__(lado, lado) y cambia el nombre a
   "Cuadrado".

Observa que describir() se escribe una sola vez y funciona para todas.

Conceptos: herencia simple, herencia multinivel, sobrescritura, reutilización.
"""
import math

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Figura("Genérica").area() == 0

    r = Rectangulo(4, 5)
    assert r.area() == 20
    assert r.describir() == "Rectángulo con área 20.00"

    c = Circulo(1)
    assert c.describir() == "Círculo con área 3.14"

    q = Cuadrado(3)
    assert q.area() == 9
    assert q.describir() == "Cuadrado con área 9.00"
    assert isinstance(q, Rectangulo), "Cuadrado debe heredar de Rectangulo"
    assert "area" not in Cuadrado.__dict__, "Cuadrado no debe redefinir area()"

    print("Todas las pruebas pasaron")
