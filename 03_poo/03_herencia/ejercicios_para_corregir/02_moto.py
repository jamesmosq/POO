"""
Ejercicio para corregir 02 - Moto
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Una Moto es un Vehiculo que además tiene cilindraje. Su descripción
    agrega el cilindraje a la descripción del vehículo.

        Moto("Yamaha", "FZ", 150).descripcion()  ->  "Yamaha FZ de 150 cc"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(self, marca, modelo)
        self.cilindraje = cilindraje

    def descripcon(self):
        return f"{super().descripcion()} de {self.cilindraje} cc"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    carro = Vehiculo("Mazda", "3")
    assert carro.descripcion() == "Mazda 3"

    moto = Moto("Yamaha", "FZ", 150)
    assert moto.marca == "Yamaha"
    assert moto.descripcion() == "Yamaha FZ de 150 cc"

    print("Todas las pruebas pasaron")
