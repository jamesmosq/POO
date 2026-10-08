"""
Ejemplo 05 - Mixins

Un mixin es una clase pequeña que aporta UNA capacidad concreta y está
pensada para combinarse con otras. No se usa sola y no tiene sentido como
"tipo de cosa" (un producto no "es un" Exportable; "puede" exportarse).

Convenciones:
    - El nombre termina en Mixin.
    - No tiene __init__ propio (o, si lo tiene, es cooperativo).
    - Se escribe ANTES de la clase base en la lista de herencia, para que
      sus métodos tengan prioridad en el MRO.
"""
import json


class ExportableJSONMixin:
    def a_json(self):
        return json.dumps(vars(self), ensure_ascii=False)


class ComparablePorPrecioMixin:
    def __lt__(self, otro):
        return self.precio < otro.precio


class RepresentableMixin:
    def __repr__(self):
        atributos = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{type(self).__name__}({atributos})"


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class ProductoTienda(ExportableJSONMixin, ComparablePorPrecioMixin, RepresentableMixin, Producto):
    pass


class Servicio(ExportableJSONMixin, RepresentableMixin):
    """Los mismos mixins sirven para clases que no tienen nada que ver."""

    def __init__(self, descripcion, horas):
        self.descripcion = descripcion
        self.horas = horas


cafe = ProductoTienda("Café", 12000)
pan = ProductoTienda("Pan", 500)
print(cafe.a_json())
print(sorted([cafe, pan]))           # usa __lt__ del mixin y __repr__ del otro mixin
print(Servicio("Soporte", 3).a_json())
print([c.__name__ for c in ProductoTienda.mro()])
