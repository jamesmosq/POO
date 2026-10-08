"""
Ejercicio propuesto 01 - Clase Persona
Nivel: básico

Una clase es un molde; cada objeto creado con ella tiene sus propios datos
(atributos) y comportamientos (métodos).

Requisitos. Crea la clase Persona:
1. __init__(self, nombre, edad): guarda los dos atributos.
2. presentarse(): retorna "Hola, soy Ana y tengo 20 años".
3. cumplir_anios(): suma 1 a la edad y retorna la edad nueva.
4. es_mayor_de_edad(): True si la edad es 18 o más.

Recuerda que todos los métodos reciben self como primer parámetro: self es
el objeto sobre el que se llama el método.

Conceptos: class, __init__, self, atributos de instancia, métodos.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Persona("Ana", 17)
    luis = Persona("Luis", 30)

    assert ana.nombre == "Ana" and ana.edad == 17
    assert ana.presentarse() == "Hola, soy Ana y tengo 17 años"
    assert ana.es_mayor_de_edad() is False

    assert ana.cumplir_anios() == 18
    assert ana.es_mayor_de_edad() is True
    assert ana.presentarse() == "Hola, soy Ana y tengo 18 años"

    assert luis.edad == 30, "Cada objeto tiene sus propios atributos"

    print("Todas las pruebas pasaron")
