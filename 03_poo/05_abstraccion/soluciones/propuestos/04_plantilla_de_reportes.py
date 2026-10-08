"""
Solución - Ejercicio propuesto 04 - Plantilla de reportes
"""

from abc import ABC, abstractmethod


class Reporte(ABC):
    def __init__(self, titulo):
        self.titulo = titulo

    def generar(self):
        lineas = self.cuerpo()
        return [f"=== {self.titulo.upper()} ===", *lineas, f"Total de líneas: {len(lineas)}"]

    @abstractmethod
    def cuerpo(self):
        pass


class ReporteVentas(Reporte):
    def __init__(self, titulo, ventas):
        super().__init__(titulo)
        self.ventas = ventas

    def cuerpo(self):
        return [f"{producto}: ${valor:,.0f}" for producto, valor in self.ventas]


class ReporteInventario(Reporte):
    def __init__(self, titulo, inventario):
        super().__init__(titulo)
        self.inventario = inventario

    def cuerpo(self):
        lineas = []
        for producto in sorted(self.inventario):
            cantidad = self.inventario[producto]
            estado = "AGOTADO" if cantidad == 0 else f"{cantidad} unidades"
            lineas.append(f"{producto}: {estado}")
        return lineas


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ventas = ReporteVentas("Ventas del día", [("Café", 12000), ("Pan", 3000)])
    assert ventas.generar() == [
        "=== VENTAS DEL DÍA ===",
        "Café: $12,000",
        "Pan: $3,000",
        "Total de líneas: 2",
    ]

    inventario = ReporteInventario("Bodega", {"Pan": 10, "Arroz": 0})
    assert inventario.generar() == [
        "=== BODEGA ===",
        "Arroz: AGOTADO",
        "Pan: 10 unidades",
        "Total de líneas: 2",
    ]

    for clase in (ReporteVentas, ReporteInventario):
        assert "generar" not in clase.__dict__, f"{clase.__name__} no debe sobrescribir generar()"

    print("Todas las pruebas pasaron")
