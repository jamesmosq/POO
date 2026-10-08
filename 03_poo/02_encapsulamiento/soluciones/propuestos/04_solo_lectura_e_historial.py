"""
Solución - Ejercicio propuesto 04 - Atributos de solo lectura e historial
"""

class Producto:
    def __init__(self, codigo, precio):
        self._codigo = codigo
        self._historial = []
        self._precio = None
        self.precio = precio

    @property
    def codigo(self):
        # Sin setter: asignar p.codigo lanza AttributeError.
        return self._codigo

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        if self._precio is not None:
            self._historial.append(self._precio)
        self._precio = valor

    @property
    def historial_de_precios(self):
        # Una tupla no se puede modificar: la lista interna queda protegida.
        return tuple(self._historial)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    p = Producto("CAF-01", 10000)
    assert p.codigo == "CAF-01"

    try:
        p.codigo = "OTRO"
        raise AssertionError("codigo debe ser de solo lectura")
    except AttributeError:
        pass

    p.precio = 12000
    p.precio = 11500
    assert p.precio == 11500
    assert p.historial_de_precios == (10000, 12000)

    historial = p.historial_de_precios
    try:
        historial.append(1)
        raise AssertionError("El historial no debe poder modificarse desde afuera")
    except AttributeError:
        pass

    try:
        p.precio = 0
        raise AssertionError("Debe lanzar ValueError")
    except ValueError:
        pass
    assert p.historial_de_precios == (10000, 12000), "Un precio inválido no entra al historial"

    print("Todas las pruebas pasaron")
