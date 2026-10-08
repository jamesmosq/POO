"""
Ejercicio para corregir 05 - Exportadores
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - Exportador es abstracta, con la propiedad abstracta extension y el
      método abstracto exportar(datos).
    - REGISTRO es un diccionario extension -> OBJETO exportador.
    - exportar(datos, extension) usa el objeto del registro o lanza
      ValueError si la extensión no existe.

        datos = [{"nombre": "Ana", "nota": 4.5}]
        exportar(datos, "csv")  -> "nombre;nota\\nAna;4.5"
        exportar(datos, "json") -> '[{"nombre": "Ana", "nota": 4.5}]'

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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
            lineas.append(";".join(registro.values()))
        return "\n".join(lineas)


class ExportadorJSON(Exportador):
    @property
    def extension(self):
        return "json"

    def exportar(self, datos):
        return json.dumps(datos, ensure_ascii=False)


REGISTRO = {clase.extension: clase for clase in (ExportadorCSV, ExportadorJSON)}


def exportar(datos, extension):
    exportador = REGISTRO.get(extension)
    return exportador.exportar(datos)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
