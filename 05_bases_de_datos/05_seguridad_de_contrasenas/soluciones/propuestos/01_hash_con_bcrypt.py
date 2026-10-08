"""
Solución - Ejercicio propuesto 01 - Hash con bcrypt
"""

import bcrypt


def hashear(clave):
    return bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()


def verificar(clave, hash_guardado):
    # checkpw extrae la sal del hash guardado y repite el cálculo con ella.
    return bcrypt.checkpw(clave.encode(), hash_guardado.encode())


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    h1 = hashear("Secreta123")
    h2 = hashear("Secreta123")
    assert isinstance(h1, str), "hashear() debe retornar un str"
    assert h1.startswith("$2"), "Debe ser un hash de bcrypt"
    assert "Secreta123" not in h1
    assert h1 != h2, "Cada hash lleva una sal distinta"

    assert verificar("Secreta123", h1) is True
    assert verificar("Secreta123", h2) is True
    assert verificar("secreta123", h1) is False

    print("Todas las pruebas pasaron")
