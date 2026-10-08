"""
Solución - Ejercicio propuesto 05 - Exportadores
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
        encabezados = list(datos[0])
        lineas = [",".join(encabezados)]
        for registro in datos:
            lineas.append(",".join(str(registro[campo]) for campo in encabezados))
        return "\n".join(lineas)


class ExportadorJSON(Exportador):
    @property
    def extension(self):
        return "json"

    def exportar(self, datos):
        return json.dumps(datos, ensure_ascii=False)


class ExportadorMarkdown(Exportador):
    @property
    def extension(self):
        return "md"

    def exportar(self, datos):
        encabezados = list(datos[0])
        lineas = [
            "| " + " | ".join(encabezados) + " |",
            "| " + " | ".join("---" for _ in encabezados) + " |",
        ]
        for registro in datos:
            lineas.append("| " + " | ".join(str(registro[c]) for c in encabezados) + " |")
        return "\n".join(lineas)


def exportar(datos, extension):
    # Se buscan las clases hijas en el momento de exportar: una clase nueva
    # queda disponible sin modificar esta función.
    for clase in Exportador.__subclasses__():
        exportador = clase()
        if exportador.extension == extension:
            return exportador.exportar(datos)
    raise ValueError(f"Formato no soportado: {extension}")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import json

    datos = [{"nombre": "Ana", "nota": 4.5}, {"nombre": "Íñigo", "nota": 3.0}]

    assert exportar(datos, "csv") == "nombre,nota\nAna,4.5\nÍñigo,3.0"
    assert json.loads(exportar(datos, "json")) == datos
    assert "Íñigo" in exportar(datos, "json")
    assert exportar(datos, "md") == (
        "| nombre | nota |\n| --- | --- |\n| Ana | 4.5 |\n| Íñigo | 3.0 |"
    )

    try:
        exportar(datos, "pdf")
        raise AssertionError("Debe lanzar ValueError")
    except ValueError as error:
        assert str(error) == "Formato no soportado: pdf"

    class ExportadorTexto(Exportador):
        @property
        def extension(self):
            return "txt"

        def exportar(self, datos):
            return f"{len(datos)} registros"

    assert exportar(datos, "txt") == "2 registros", "Una clase nueva debe funcionar sin cambiar exportar()"

    print("Todas las pruebas pasaron")
