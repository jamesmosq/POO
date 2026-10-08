"""
Solución - Ejercicio para corregir 05 - Usuario y contraseña

CORRECCIÓN 1: verificar calculaba el hash sin la sal del usuario, así que
nunca coincidía con el guardado. Hay que usar la misma sal con la que se
calculó.

CORRECCIÓN 2 (cualquiera podía cambiar la clave): "not self.verificar" sin
paréntesis pregunta si el MÉTODO existe, y eso siempre es verdadero. La
condición nunca se cumplía y nunca se pedía la clave actual. Hay que
llamarlo con la clave: self.verificar(actual).

CORRECCIÓN 3: la clave nueva se guardaba en texto plano en _hash. Se debe
generar una sal nueva y guardar el hash de la nueva clave.
"""

import hashlib
import secrets


def calcular_hash(sal, clave):
    return hashlib.sha256((sal + clave).encode()).hexdigest()


class Usuario:
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self._sal = secrets.token_hex(16)
        self._hash = calcular_hash(self._sal, clave)

    def verificar(self, clave):
        return calcular_hash(self._sal, clave) == self._hash  # CORRECCIÓN 1

    def cambiar_clave(self, actual, nueva):
        if not self.verificar(actual):  # CORRECCIÓN 2
            raise PermissionError("Clave actual incorrecta")
        self._sal = secrets.token_hex(16)  # CORRECCIÓN 3
        self._hash = calcular_hash(self._sal, nueva)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Usuario("ana", "Secreta123")
    assert ana.verificar("Secreta123") is True, "La clave correcta debe funcionar"
    assert ana.verificar(ana._hash) is False, "Escribir el hash no debe servir como clave"

    try:
        ana.cambiar_clave("incorrecta", "Hackeada99")
        raise AssertionError("Con la clave actual incorrecta debe lanzar PermissionError")
    except PermissionError:
        pass

    ana.cambiar_clave("Secreta123", "NuevaClave1")
    assert ana.verificar("NuevaClave1") is True
    assert "NuevaClave1" not in vars(ana).values(), "La clave nueva quedó guardada en texto plano"

    print("Todas las pruebas pasaron")
