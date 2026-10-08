"""
Ejercicio para corregir 05 - Usuario y contraseña
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - El usuario guarda una sal y el hash de (sal + clave); nunca la clave.
    - verificar(clave) compara el hash de la clave escrita con el guardado.
    - cambiar_clave(actual, nueva) exige la clave actual correcta (si no,
      PermissionError) y guarda el hash de la nueva.

Ojo: este código "funciona" en el caso feliz. Los errores son de
seguridad: alguno deja entrar a quien no debe. Las pruebas intentan
romperlo.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
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
        return calcular_hash("", clave) == self._hash

    def cambiar_clave(self, actual, nueva):
        if not self.verificar:
            raise PermissionError("Clave actual incorrecta")
        self._hash = nueva


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
