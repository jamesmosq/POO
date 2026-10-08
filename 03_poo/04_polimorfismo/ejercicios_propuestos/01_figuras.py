"""
Ejercicio propuesto 01 - Figuras
Nivel: básico

Polimorfismo: objetos de clases distintas responden al MISMO método, cada
uno a su manera. Quien los usa no necesita saber de qué clase son.

Requisitos:
1. Clase Figura con el método area() que lanza
   NotImplementedError("Cada figura debe implementar area()").
2. Clases Rectangulo(base, altura), Circulo(radio) y Triangulo(base,
   altura), hijas de Figura, cada una con su propio area().
3. Función area_total(figuras): suma el área de cualquier lista de figuras
   llamando a area() de cada una. No uses isinstance ni type: deja que cada
   objeto sepa calcular su área.
4. Función la_mas_grande(figuras): retorna la figura de mayor área.

Conceptos: polimorfismo, sobrescritura, NotImplementedError.
"""
import math

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    figuras = [Rectangulo(4, 5), Circulo(1), Triangulo(6, 2)]
    assert round(area_total(figuras), 2) == 29.14
    assert isinstance(la_mas_grande(figuras), Rectangulo)

    try:
        Figura().area()
        raise AssertionError("Figura.area() debe lanzar NotImplementedError")
    except NotImplementedError:
        pass

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    assert "isinstance(" not in fuente and "type(" not in fuente, "Usa polimorfismo, no isinstance ni type"

    print("Todas las pruebas pasaron")
