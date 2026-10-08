"""
Solución - Ejercicio para corregir 02 - Moto

CORRECCIÓN 1 (TypeError: __init__() takes 3 positional arguments but 4 were
given): super() ya está ligado al objeto, por eso self NO se pasa.
    Incorrecto:  super().__init__(self, marca, modelo)
    Correcto:    super().__init__(marca, modelo)
Solo se pasa self cuando se llama al padre por su nombre:
    Vehiculo.__init__(self, marca, modelo)

CORRECCIÓN 2 (resultado incorrecto, sin excepción): el método se llamaba
'descripcon'. Como el nombre no coincide, no sobrescribe a descripcion() y
la moto usa la versión del padre, que no muestra el cilindraje. Python no
avisa de este error: hay que revisar los nombres con cuidado.
"""


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)  # CORRECCIÓN 1
        self.cilindraje = cilindraje

    def descripcion(self):  # CORRECCIÓN 2
        return f"{super().descripcion()} de {self.cilindraje} cc"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    carro = Vehiculo("Mazda", "3")
    assert carro.descripcion() == "Mazda 3"

    moto = Moto("Yamaha", "FZ", 150)
    assert moto.marca == "Yamaha"
    assert moto.descripcion() == "Yamaha FZ de 150 cc"

    print("Todas las pruebas pasaron")
