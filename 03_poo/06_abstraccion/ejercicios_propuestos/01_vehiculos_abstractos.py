"""
Ejercicio propuesto 01 - Vehículos abstractos
Nivel: básico

Una clase abstracta define QUÉ deben hacer sus hijas, pero no CÓMO. No se
pueden crear objetos de ella directamente. Se construye con el módulo abc:

    from abc import ABC, abstractmethod

    class Base(ABC):
        @abstractmethod
        def metodo(self):
            pass

Requisitos:
1. Clase abstracta Vehiculo(ABC) con:
   - __init__(self, marca)
   - método abstracto mover(), que retorna un texto.
   - método concreto (normal) describir(): "Toyota: avanza por la
     carretera", usando mover().
2. Clases concretas:
       Carro(marca)      mover() -> "avanza por la carretera"
       Bicicleta(marca)  mover() -> "avanza pedaleando"
       Lancha(marca)     mover() -> "navega por el agua"

Conceptos: ABC, @abstractmethod, métodos concretos en la clase abstracta.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from abc import ABC

    try:
        Vehiculo("X")
        raise AssertionError("No se debe poder crear un Vehiculo directamente")
    except TypeError:
        pass

    assert issubclass(Vehiculo, ABC)
    assert Carro("Toyota").describir() == "Toyota: avanza por la carretera"
    assert Bicicleta("GW").describir() == "GW: avanza pedaleando"
    assert Lancha("Yamaha").describir() == "Yamaha: navega por el agua"

    print("Todas las pruebas pasaron")
