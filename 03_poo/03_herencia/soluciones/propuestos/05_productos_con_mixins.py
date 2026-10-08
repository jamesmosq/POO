"""
Solución - Ejercicio propuesto 05 - Productos con mixins (herencia múltiple)
"""


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class ExportableMixin:
    def a_diccionario(self):
        return {"tipo": type(self).__name__, **vars(self)}


class ComparablePorPrecioMixin:
    def __lt__(self, otro):
        return self.precio < otro.precio


class ProductoDigital(ExportableMixin, ComparablePorPrecioMixin, Producto):
    def __init__(self, nombre, precio, tamano_mb):
        # Los mixins no tienen __init__, así que super() llega a Producto.
        super().__init__(nombre, precio)
        self.tamano_mb = tamano_mb


# Respuesta a la pregunta:
# Python busca los métodos siguiendo el MRO, de izquierda a derecha. Si los
# mixins van primero, sus métodos tienen prioridad y pueden ampliar o
# reemplazar los de la clase base. Si la clase base fuera primero y tuviera
# un método con el mismo nombre, el del mixin nunca se ejecutaría. Por
# convención la clase base "principal" va al final.


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    curso = ProductoDigital("Curso Python", 50000, 300)
    libro = ProductoDigital("Libro POO", 30000, 15)
    video = ProductoDigital("Video SQL", 40000, 900)

    assert curso.a_diccionario() == {
        "tipo": "ProductoDigital",
        "nombre": "Curso Python",
        "precio": 50000,
        "tamano_mb": 300,
    }

    ordenados = sorted([curso, libro, video])
    assert [p.nombre for p in ordenados] == ["Libro POO", "Video SQL", "Curso Python"]
    assert libro < curso

    nombres = [clase.__name__ for clase in ProductoDigital.__mro__]
    assert nombres == [
        "ProductoDigital",
        "ExportableMixin",
        "ComparablePorPrecioMixin",
        "Producto",
        "object",
    ]

    print("Todas las pruebas pasaron")
