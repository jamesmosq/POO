"""
Solución - Ejercicio propuesto 05 - Usuario con contraseña
"""

import hashlib
import secrets


class Usuario:
    LONGITUD_MINIMA = 8

    def __init__(self, nombre, clave):
        self.nombre = nombre
        self._guardar_clave(clave)

    def _calcular_hash(self, clave):
        return hashlib.sha256((self._sal + clave).encode()).hexdigest()

    def _guardar_clave(self, clave):
        self._sal = secrets.token_hex(16)
        self._hash = self._calcular_hash(clave)

    def verificar(self, clave):
        # secrets.compare_digest compara en tiempo constante, lo que evita
        # ataques que miden cuánto tarda la comparación.
        return secrets.compare_digest(self._calcular_hash(clave), self._hash)

    def cambiar_clave(self, actual, nueva):
        if not self.verificar(actual):
            raise PermissionError("La clave actual no es correcta")
        if len(nueva) < self.LONGITUD_MINIMA:
            raise ValueError(f"La clave debe tener al menos {self.LONGITUD_MINIMA} caracteres")
        self._guardar_clave(nueva)

    @property
    def clave(self):
        raise AttributeError("La clave no se puede consultar")


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Usuario("ana", "Secreta123")
    assert ana.verificar("Secreta123") is True
    assert ana.verificar("secreta123") is False

    for valor in vars(ana).values():
        assert "Secreta123" not in str(valor), "La clave no debe guardarse en ningún atributo"

    luis = Usuario("luis", "Secreta123")
    assert ana._hash != luis._hash, "Con sal distinta, los hashes deben ser distintos"

    try:
        ana.clave
        raise AssertionError("Leer la clave debe lanzar AttributeError")
    except AttributeError:
        pass

    try:
        ana.cambiar_clave("incorrecta", "NuevaClave1")
        raise AssertionError("Debe lanzar PermissionError")
    except PermissionError:
        pass

    try:
        ana.cambiar_clave("Secreta123", "corta")
        raise AssertionError("Debe lanzar ValueError")
    except ValueError:
        pass

    sal_anterior = ana._sal
    ana.cambiar_clave("Secreta123", "NuevaClave1")
    assert ana.verificar("NuevaClave1") is True
    assert ana.verificar("Secreta123") is False
    assert ana._sal != sal_anterior

    print("Todas las pruebas pasaron")
