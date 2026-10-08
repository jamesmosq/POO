"""
Solución - Ejercicio propuesto 02 - Interfaz de almacenamiento
"""

import json
import os
from abc import ABC, abstractmethod


class Almacenamiento(ABC):
    @abstractmethod
    def guardar(self, clave, valor):
        pass

    @abstractmethod
    def obtener(self, clave):
        pass

    @abstractmethod
    def eliminar(self, clave):
        pass


class AlmacenamientoMemoria(Almacenamiento):
    def __init__(self):
        self._datos = {}

    def guardar(self, clave, valor):
        self._datos[clave] = valor

    def obtener(self, clave):
        return self._datos.get(clave)

    def eliminar(self, clave):
        return self._datos.pop(clave, None) is not None


class AlmacenamientoJSON(Almacenamiento):
    def __init__(self, ruta):
        self.ruta = ruta

    def _leer(self):
        if not os.path.exists(self.ruta):
            return {}
        with open(self.ruta, encoding="utf-8") as archivo:
            return json.load(archivo)

    def _escribir(self, datos):
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)

    def guardar(self, clave, valor):
        datos = self._leer()
        datos[clave] = valor
        self._escribir(datos)

    def obtener(self, clave):
        return self._leer().get(clave)

    def eliminar(self, clave):
        datos = self._leer()
        if clave not in datos:
            return False
        del datos[clave]
        self._escribir(datos)
        return True


def registrar_visita(almacen, usuario):
    # Esta función solo conoce la interfaz Almacenamiento, no cómo se guarda.
    total = (almacen.obtener(usuario) or 0) + 1
    almacen.guardar(usuario, total)
    return total


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os
    import tempfile

    try:
        Almacenamiento()
        raise AssertionError("Almacenamiento debe ser abstracta")
    except TypeError:
        pass

    ruta = os.path.join(tempfile.mkdtemp(), "datos.json")
    for almacen in (AlmacenamientoMemoria(), AlmacenamientoJSON(ruta)):
        assert almacen.obtener("x") is None
        almacen.guardar("x", 10)
        assert almacen.obtener("x") == 10
        assert almacen.eliminar("x") is True
        assert almacen.eliminar("x") is False

        assert registrar_visita(almacen, "ana") == 1
        assert registrar_visita(almacen, "ana") == 2
        assert registrar_visita(almacen, "luis") == 1

    assert AlmacenamientoJSON(ruta).obtener("ana") == 2, "Los datos deben quedar en el archivo"

    print("Todas las pruebas pasaron")
