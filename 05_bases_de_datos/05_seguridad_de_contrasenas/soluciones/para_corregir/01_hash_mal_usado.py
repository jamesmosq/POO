"""
Solución - Ejercicio para corregir 01 - Hash mal usado

CORRECCIÓN 1 (TypeError; según la versión de bcrypt dice "Strings must be
encoded before hashing" o "'str' object cannot be converted to 'PyBytes'"):
bcrypt trabaja con bytes. La clave se convierte con .encode().

CORRECCIÓN 2 (la clave correcta no era aceptada): cada hash lleva una sal
nueva y aleatoria, así que hashear dos veces la misma clave da resultados
DISTINTOS. Para verificar se usa bcrypt.checkpw, que toma la sal del hash
guardado.
"""

import bcrypt


def hashear(clave):
    return bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()  # CORRECCIÓN 1


def verificar(clave, hash_guardado):
    return bcrypt.checkpw(clave.encode(), hash_guardado.encode())  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    guardado = hashear("Secreta123")
    assert guardado.startswith("$2")
    assert verificar("Secreta123", guardado) is True, "La clave correcta no fue aceptada"
    assert verificar("otra", guardado) is False
    print("Todas las pruebas pasaron")
