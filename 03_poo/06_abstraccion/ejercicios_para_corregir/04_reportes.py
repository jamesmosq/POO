"""
Ejercicio para corregir 04 - Reportes
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Reporte.generar() arma el reporte completo: encabezado, cuerpo y pie.
    Las hijas solo implementan cuerpo(), que retorna una lista de líneas.

        ReporteNotas("Notas", {"Ana": 4.5}).generar()
            -> ["== NOTAS ==", "Ana: 4.5", "Fin (1 líneas)"]

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from abc import ABC, abstractmethod


class Reporte(ABC):
    def __init__(self, titulo):
        self.titulo = titulo

    @abstractmethod
    def cuerpo(self):
        pass

    def generar(self):
        lineas = self.cuerpo()
        return [f"== {self.titulo.upper()} ==", lineas, f"Fin ({len(lineas)} líneas)"]


class ReporteNotas(Reporte):
    def __init__(self, titulo, notas):
        self.notas = notas

    def cuerpo(self):
        for nombre, nota in self.notas.items():
            return [f"{nombre}: {nota}"]


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    reporte = ReporteNotas("Notas", {"Ana": 4.5, "Luis": 3.0})
    assert reporte.generar() == ["== NOTAS ==", "Ana: 4.5", "Luis: 3.0", "Fin (2 líneas)"], reporte.generar()

    print("Todas las pruebas pasaron")
