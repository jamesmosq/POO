"""
Ejercicio propuesto 03 - Propiedades abstractas
Nivel: intermedio

Una propiedad también puede ser abstracta. El orden de los decoradores
importa: @property va arriba y @abstractmethod abajo.

    @property
    @abstractmethod
    def nombre(self):
        pass

Requisitos:
1. Clase abstracta Figura con:
   - propiedad abstracta nombre.
   - método abstracto area().
   - método abstracto perimetro().
   - método concreto resumen(): "Cuadrado: área 4.00, perímetro 8.00".
2. Clases concretas Cuadrado(lado) y Circulo(radio). En cada una, nombre
   es una propiedad que retorna el texto "Cuadrado" o "Círculo".
3. Una clase que no implemente todo lo abstracto no se debe poder
   instanciar (eso ya lo hace ABC: compruébalo con las pruebas).

Conceptos: propiedades abstractas, orden de decoradores, contratos.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Cuadrado(2).resumen() == "Cuadrado: área 4.00, perímetro 8.00"
    assert Circulo(1).resumen() == "Círculo: área 3.14, perímetro 6.28"
    assert isinstance(Cuadrado.nombre, property), "nombre debe ser una propiedad"

    class Incompleta(Figura):
        @property
        def nombre(self):
            return "Incompleta"

        def area(self):
            return 0

    try:
        Incompleta()
        raise AssertionError("Una figura sin perimetro() no se debe poder crear")
    except TypeError:
        pass

    print("Todas las pruebas pasaron")
