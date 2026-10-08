"""
Ejercicio propuesto 01 - Vehículo anfibio
Nivel: básico

Requisitos:
1. Clase Terrestre con:
       andar()       -> "Avanzando por tierra"
       velocidad()   -> 80
2. Clase Acuatico con:
       navegar()     -> "Navegando en el agua"
       velocidad()   -> 30
3. Clase Anfibio, que herede de Terrestre y de Acuatico (en ese orden):
       - tiene los métodos de los dos padres;
       - su velocidad() es la de Terrestre (la hereda por el orden, no la
         escribas de nuevo);
       - velocidad_en_agua(): retorna la velocidad de Acuatico llamando
         explícitamente al método de ese padre: Acuatico.velocidad(self)
       - describir(): "Anfibio: 80 km/h en tierra, 30 km/h en agua"

Conceptos: sintaxis de herencia múltiple, MRO, llamar al método de un padre
específico.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    a = Anfibio()
    assert a.andar() == "Avanzando por tierra"
    assert a.navegar() == "Navegando en el agua"
    assert a.velocidad() == 80, "Por el MRO se usa la velocidad de Terrestre"
    assert a.velocidad_en_agua() == 30
    assert a.describir() == "Anfibio: 80 km/h en tierra, 30 km/h en agua"

    assert Anfibio.__bases__ == (Terrestre, Acuatico), "Hereda de Terrestre y de Acuatico, en ese orden"
    assert "velocidad" not in Anfibio.__dict__, "No redefinas velocidad() en Anfibio"
    assert isinstance(a, Terrestre) and isinstance(a, Acuatico)

    print("Todas las pruebas pasaron")
