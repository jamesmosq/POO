"""
Ejercicio para corregir 03 - Orden imposible
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    - Documento es la base; Factura es un Documento.
    - FacturaExportable combina Factura con el mixin ExportableMixin.
    - El mixin funciona con cualquier clase que tenga los atributos
      "codigo" y "total"; exportar() retorna "F-001;150000".

Pista: si Python dice que no puede crear un MRO consistente, revisa si
alguna clase aparece en la lista de padres ANTES que una de sus hijas.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Documento:
    def __init__(self, codigo):
        self.codigo = codigo


class Factura(Documento):
    def __init__(self, codigo, total):
        super().__init__(codigo)
        self.valor_total = total


class ExportableMixin:
    def exportar(self):
        return f"{self.codigo};{self.total}"


class FacturaExportable(ExportableMixin, Documento, Factura):
    pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    f = FacturaExportable("F-001", 150000)
    assert f.exportar() == "F-001;150000", f.exportar()
    assert isinstance(f, Factura) and isinstance(f, Documento)

    print("Todas las pruebas pasaron")
