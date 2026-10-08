"""
Ejercicio propuesto 05 - Exportadores
Nivel: avanzado

Una aplicación exporta datos en varios formatos. Para agregar un formato
nuevo no debería ser necesario tocar el código existente, solo crear una
clase nueva.

Los datos son una lista de diccionarios con las mismas claves:
    [{"nombre": "Ana", "nota": 4.5}, {"nombre": "Luis", "nota": 3.0}]

Requisitos:
1. Clase abstracta Exportador con:
   - propiedad abstracta extension (por ejemplo "csv").
   - método abstracto exportar(datos) -> str.
2. ExportadorCSV: primera línea con los encabezados separados por coma,
   luego una línea por registro. Las líneas se unen con "\\n".
       nombre,nota
       Ana,4.5
       Luis,3.0
3. ExportadorJSON: usa json.dumps(datos, ensure_ascii=False).
4. ExportadorMarkdown: tabla en formato Markdown:
       | nombre | nota |
       | --- | --- |
       | Ana | 4.5 |
       | Luis | 3.0 |
5. Función exportar(datos, extension): busca entre las subclases de
   Exportador (Exportador.__subclasses__()) la que tenga esa extensión,
   crea un objeto y exporta. Si no hay ninguna, lanza
   ValueError(f"Formato no soportado: {extension}").

Conceptos: abstracción, extensibilidad, __subclasses__, principio
abierto/cerrado.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
