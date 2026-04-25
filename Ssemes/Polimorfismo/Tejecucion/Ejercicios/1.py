# Ejercicio 1: Simulador de vehículos

class Coche:
    def mover(self):
        return "El coche está conduciendo en la carretera."


class Barco:
    def mover(self):
        return "El barco está navegando en el agua."


class Avion:
    def mover(self):
        return "El avión está volando en el aire."


def iniciar_viaje(vehiculo):
    print(vehiculo.mover())


# Uso:
coche = Coche()
barco = Barco()
avion = Avion()

iniciar_viaje(coche)
iniciar_viaje(barco)
iniciar_viaje(avion)


