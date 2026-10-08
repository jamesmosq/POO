"""
Solución - Ejercicio para corregir 05 - Exportadores

CORRECCIÓN 1 (las claves del registro eran objetos property): al leer
clase.extension desde la CLASE se obtiene el objeto property, no su valor.
La propiedad solo da el texto cuando se lee desde un objeto. Además, el
enunciado pide guardar objetos: se crea una instancia de cada clase.

CORRECCIÓN 2 (TypeError: sequence item 1: expected str instance, float
found): join solo une textos; la nota es un float. Hay que convertir cada
valor con str().

CORRECCIÓN 3: con una extensión desconocida, get() retornaba None y el
error era un AttributeError poco claro. Se valida y se lanza el ValueError
que pide el enunciado.
"""

import json
from abc import ABC, abstractmethod


class Exportador(ABC):
    @property
    @abstractmethod
    def extension(self):
        pass

    @abstractmethod
    def exportar(self, datos):
        pass


class ExportadorCSV(Exportador):
    @property
    def extension(self):
        return "csv"

    def exportar(self, datos):
        encabezados = list(datos[0].keys())
        lineas = [";".join(encabezados)]
        for registro in datos:
            lineas.append(";".join(str(valor) for valor in registro.values()))  # CORRECCIÓN 2
        return "\n".join(lineas)


class ExportadorJSON(Exportador):
    @property
    def extension(self):
        return "json"

    def exportar(self, datos):
        return json.dumps(datos, ensure_ascii=False)


REGISTRO = {objeto.extension: objeto for objeto in (ExportadorCSV(), ExportadorJSON())}  # CORRECCIÓN 1


def exportar(datos, extension):
    if extension not in REGISTRO:  # CORRECCIÓN 3
        raise ValueError(f"Formato no soportado: {extension}")
    return REGISTRO[extension].exportar(datos)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [{"nombre": "Ana", "nota": 4.5}]
    assert set(REGISTRO) == {"csv", "json"}, f"Claves del registro: {list(REGISTRO)}"
    assert exportar(datos, "json") == '[{"nombre": "Ana", "nota": 4.5}]'
    assert exportar(datos, "csv") == "nombre;nota\nAna;4.5"

    try:
        exportar(datos, "pdf")
        raise AssertionError("Una extensión desconocida debe lanzar ValueError")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
