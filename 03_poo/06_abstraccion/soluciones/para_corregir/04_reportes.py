"""
Solución - Ejercicio para corregir 04 - Reportes

CORRECCIÓN 1 (AttributeError: 'ReporteNotas' object has no attribute
'titulo'): el __init__ de la hija no llamaba al del padre, que es quien
guarda el título.

CORRECCIÓN 2: cuerpo() retornaba dentro del for, en la primera vuelta, así
que solo salía la primera nota. La lista se construye completa y se
retorna después del ciclo.

CORRECCIÓN 3: generar() metía la lista del cuerpo como UN elemento
(quedaba una lista dentro de otra). Con *lineas se agregan sus elementos
uno a uno.
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
        return [f"== {self.titulo.upper()} ==", *lineas, f"Fin ({len(lineas)} líneas)"]  # CORRECCIÓN 3


class ReporteNotas(Reporte):
    def __init__(self, titulo, notas):
        super().__init__(titulo)  # CORRECCIÓN 1
        self.notas = notas

    def cuerpo(self):
        return [f"{nombre}: {nota}" for nombre, nota in self.notas.items()]  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    reporte = ReporteNotas("Notas", {"Ana": 4.5, "Luis": 3.0})
    assert reporte.generar() == ["== NOTAS ==", "Ana: 4.5", "Luis: 3.0", "Fin (2 líneas)"], reporte.generar()

    print("Todas las pruebas pasaron")
