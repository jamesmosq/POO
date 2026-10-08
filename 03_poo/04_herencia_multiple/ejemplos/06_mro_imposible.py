"""
Ejemplo 06 - Cuando el MRO es imposible

Python no acepta cualquier orden de padres. Si el orden que escribimos
contradice la jerarquía, no se puede construir un MRO coherente y la clase
ni siquiera se crea:

    TypeError: Cannot create a consistent method resolution order (MRO)
"""


class Animal:
    pass


class Perro(Animal):
    pass


# Escribir la clase base ANTES que su hija es contradictorio: la lista dice
# "Animal antes que Perro", pero Perro hereda de Animal, así que Perro debe
# ir antes. Python lo rechaza al crear la clase.
try:
    class Mascota(Animal, Perro):
        pass
except TypeError as error:
    print("Error al crear la clase:", error)


# Solución: la clase más específica primero (o simplemente no repetir la
# base, porque Perro ya la incluye).
class Mascota(Perro, Animal):
    pass


print([c.__name__ for c in Mascota.mro()])


class MascotaSimple(Perro):
    pass


print([c.__name__ for c in MascotaSimple.mro()])
