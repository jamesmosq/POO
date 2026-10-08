"""
Ejercicio propuesto 05 - Productos con mixins (herencia múltiple)
Nivel: avanzado

Un mixin es una clase pequeña que aporta UNA capacidad y está pensada para
combinarse con otras mediante herencia múltiple. No se usa sola.

Requisitos:
1. Clase Producto(nombre, precio).
2. ExportableMixin con el método a_diccionario(), que retorne un diccionario
   con la clave "tipo" (el nombre de la clase del objeto) más todos los
   atributos del objeto. Pista: type(self).__name__ y vars(self).
3. ComparablePorPrecioMixin con el método especial __lt__(self, otro), que
   compare por el atributo precio. Con esto sorted() funciona sobre una lista
   de productos.
4. ProductoDigital(nombre, precio, tamano_mb), que herede en este orden de
   ExportableMixin, ComparablePorPrecioMixin y Producto. Su __init__ debe
   usar super().__init__(nombre, precio).

Pregunta para pensar (respóndela en un comentario): ¿por qué los mixins se
escriben antes que la clase base en la lista de herencia? Revisa el MRO.

Conceptos: herencia múltiple, mixins, MRO, métodos especiales.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
