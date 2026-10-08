"""
Ejercicio propuesto 02 - Propiedades de temperatura
Nivel: básico

@property permite que un método se use como si fuera un atributo, y
@nombre.setter permite validar cuando se le asigna un valor:

    t.celsius = 25     # en realidad llama al setter, que valida
    print(t.celsius)   # en realidad llama al getter

Requisitos. Crea la clase Temperatura(celsius=0):
1. Guarda el valor en self._celsius.
2. Propiedad celsius con getter y setter. El setter lanza ValueError si el
   valor es menor que -273.15 (el cero absoluto).
3. En __init__ asigna con self.celsius = celsius, para que también se
   valide al crear el objeto.
4. Propiedad fahrenheit calculada a partir de celsius (F = C * 9 / 5 + 32),
   con un setter que convierte y guarda en celsius.

Conceptos: @property, setter, propiedades calculadas.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    t = Temperatura(25)
    assert t.celsius == 25
    assert t.fahrenheit == 77

    t.fahrenheit = 212
    assert t.celsius == 100

    t.celsius = -273.15
    try:
        t.celsius = -300
        raise AssertionError("Debe lanzar ValueError")
    except ValueError:
        pass
    assert t.celsius == -273.15

    try:
        Temperatura(-500)
        raise AssertionError("El constructor también debe validar")
    except ValueError:
        pass

    assert isinstance(Temperatura.celsius, property), "celsius debe ser una propiedad"

    print("Todas las pruebas pasaron")
