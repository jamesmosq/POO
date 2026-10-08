"""
Solución - Ejercicio para corregir 02 - Smartphone

CORRECCIÓN 1 (TypeError: unsupported operand type(s) for +: 'method' and
'str'): super().descripcion sin paréntesis es el método, no su resultado.

CORRECCIÓN 2 (se describía como teléfono): con (Telefono, Camara) el MRO
pone primero a Telefono, y super() encuentra su descripcion(). El orden de
los padres decide quién gana: Camara debe ir primero.
"""

class Telefono:
    def llamar(self, numero):
        return f"Llamando a {numero}"

    def descripcion(self):
        return "Teléfono con llamadas"


class Camara:
    def fotografiar(self):
        return "Foto tomada"

    def descripcion(self):
        return "Cámara de 50 MP"


class Smartphone(Camara, Telefono):  # CORRECCIÓN 2
    def descripcion(self):
        return super().descripcion() + " con apps"  # CORRECCIÓN 1


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    s = Smartphone()
    assert s.llamar("300") == "Llamando a 300"
    assert s.fotografiar() == "Foto tomada"
    assert s.descripcion() == "Cámara de 50 MP con apps", s.descripcion()

    print("Todas las pruebas pasaron")
