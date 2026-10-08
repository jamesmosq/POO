"""
Ejercicio propuesto 02 - Duck typing
Nivel: básico

"Si camina como pato y hace cuac como pato, es un pato". En Python no hace
falta que las clases tengan un padre común para usarlas igual: basta con
que tengan el método que se necesita.

Requisitos:
1. Crea tres clases SIN relación de herencia entre ellas, cada una con el
   método hablar():
       Pato()          -> "Cuac"
       Robot(modelo)   -> "Soy el robot T-800" (con su modelo)
       Persona(nombre) -> "Hola, me llamo Ana"
2. Crea la clase Piedra, que NO tiene hablar().
3. Función coro(objetos): retorna una lista con lo que dice cada objeto que
   SÍ sabe hablar; ignora los que no. Pista: hasattr(objeto, "hablar"), o
   intentar llamar y atrapar AttributeError.

Conceptos: duck typing, hasattr, polimorfismo sin herencia.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    objetos = [Pato(), Piedra(), Robot("T-800"), Persona("Ana")]
    assert coro(objetos) == ["Cuac", "Soy el robot T-800", "Hola, me llamo Ana"]
    assert coro([]) == []

    for clase in (Pato, Robot, Persona):
        assert clase.__bases__ == (object,), f"{clase.__name__} no debe heredar de otra clase"

    print("Todas las pruebas pasaron")
