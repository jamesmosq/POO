"""
Solución - Ejercicio para corregir 05 - Impresora multifuncional

CORRECCIÓN 1 (Dispositivo se inicializaba dos veces): Impresora, Escaner y
Multifuncional llamaban a sus padres por nombre. En un diamante eso hace
que Dispositivo.__init__ se ejecute una vez por cada camino. Con super(),
Python sigue el MRO y ejecuta cada __init__ una sola vez:
    Multifuncional -> Impresora -> Escaner -> Dispositivo -> object
Ojo: dentro de Impresora, super() NO apunta a Dispositivo sino a Escaner,
porque super() sigue el MRO del objeto real, no el de la clase donde está
escrito.

CORRECCIÓN 2 (imprimía "Este equipo no imprime"): el orden de los padres
define el MRO. Con (Escaner, Impresora), Python encuentra primero
Escaner.imprimir. Para que imprima como Impresora, Impresora va primero.

CORRECCIÓN 3 (AttributeError: type object 'super' has no attribute
'encender'): faltaban los paréntesis. 'super' es la clase; 'super()' crea el
objeto que permite llamar al método del padre.
"""


class Dispositivo:
    total_creados = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Dispositivo.total_creados += 1

    def encender(self):
        return f"{self.nombre} encendido"


class Impresora(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre)  # CORRECCIÓN 1

    def imprimir(self, texto):
        return f"Imprimiendo: {texto}"


class Escaner(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre)  # CORRECCIÓN 1

    def escanear(self):
        return "Escaneando documento"

    def imprimir(self, texto):
        return "Este equipo no imprime"


class Multifuncional(Impresora, Escaner):  # CORRECCIÓN 2
    def __init__(self, nombre):
        super().__init__(nombre)  # CORRECCIÓN 1

    def encender(self):
        return super().encender() + ", modo multifuncional"  # CORRECCIÓN 3


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Dispositivo.total_creados = 0
    equipo = Multifuncional("HP 2775")
    assert Dispositivo.total_creados == 1, (
        f"Se inicializó Dispositivo {Dispositivo.total_creados} veces"
    )

    assert equipo.imprimir("informe.pdf") == "Imprimiendo: informe.pdf"
    assert equipo.escanear() == "Escaneando documento"
    assert equipo.encender() == "HP 2775 encendido, modo multifuncional"

    assert Escaner("Epson").imprimir("x") == "Este equipo no imprime"

    print("Todas las pruebas pasaron")
