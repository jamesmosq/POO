# ===========================================
# 1. POLIMORFISMO DE SUBTIPO (HERENCIA)
# ===========================================

class Vehiculo:
    def arrancar(self):
        return "El vehículo arranca"


class Coche(Vehiculo):
    def arrancar(self):
        return "El coche arranca con llave"


class Moto(Vehiculo):
    def arrancar(self):
        return "La moto arranca con botón"

class Camion(Vehiculo):
    def arrancar(self):
        return "El camión arranca con un motor potente"


# Uso polimórfico
vehiculos = [Coche(), Moto(), Camion()]
for vehiculo in vehiculos:
    print(vehiculo.arrancar())

print("+" * 50) # no me preginte para qye es
