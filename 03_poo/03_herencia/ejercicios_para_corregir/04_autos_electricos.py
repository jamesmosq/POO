"""
Ejercicio para corregir 04 - Autos eléctricos (herencia multinivel)
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Vehiculo -> Auto -> AutoElectrico. Cada nivel agrega un dato y amplía
    el texto de __str__ del nivel anterior.

        str(AutoElectrico("BYD", 4, 400))
            ->  "Vehículo BYD de 4 puertas, autonomía 400 km"

    La función contar_electricos(lista) recibe una lista de vehículos y
    retorna cuántos son eléctricos.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def __str__(self):
        return f"Vehículo {self.marca}"


class Auto(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def __str__(self):
        return super().__str__() + f" de {self.puertas} puertas"


class AutoElectrico(Auto):
    def __init__(self, marca, puertas, autonomia_km):
        Vehiculo.__init__(self, marca)
        self.autonomia_km = autonomia_km

    def __str__(self):
        super().__str__() + f", autonomía {self.autonomia_km} km"


def contar_electricos(vehiculos):
    return sum(1 for v in vehiculos if isinstance(AutoElectrico, v))


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert str(Auto("Mazda", 4)) == "Vehículo Mazda de 4 puertas"

    byd = AutoElectrico("BYD", 4, 400)
    assert byd.puertas == 4
    assert str(byd) == "Vehículo BYD de 4 puertas, autonomía 400 km"

    flota = [Auto("Mazda", 4), byd, Vehiculo("Genérico"), AutoElectrico("Tesla", 2, 500)]
    assert contar_electricos(flota) == 2

    print("Todas las pruebas pasaron")
