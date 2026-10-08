"""
Solución - Ejercicio para corregir 03 - Orden imposible

CORRECCIÓN 1 (TypeError: Cannot create a consistent method resolution
order (MRO)): la lista de padres ponía a Documento antes que Factura, pero
Factura hereda de Documento y debe ir antes. Como Factura ya incluye a
Documento, basta con (ExportableMixin, Factura).

CORRECCIÓN 2 (AttributeError: 'FacturaExportable' object has no attribute
'total'): el mixin espera un atributo llamado total, y Factura lo guardaba
como valor_total. Un mixin depende de que las clases con las que se combina
cumplan su "contrato" (los atributos que usa).
"""

class Documento:
    def __init__(self, codigo):
        self.codigo = codigo


class Factura(Documento):
    def __init__(self, codigo, total):
        super().__init__(codigo)
        self.total = total  # CORRECCIÓN 2


class ExportableMixin:
    def exportar(self):
        return f"{self.codigo};{self.total}"


class FacturaExportable(ExportableMixin, Factura):  # CORRECCIÓN 1
    pass


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    f = FacturaExportable("F-001", 150000)
    assert f.exportar() == "F-001;150000", f.exportar()
    assert isinstance(f, Factura) and isinstance(f, Documento)

    print("Todas las pruebas pasaron")
