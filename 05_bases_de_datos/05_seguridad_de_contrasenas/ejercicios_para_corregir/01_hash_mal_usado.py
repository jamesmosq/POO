"""
Ejercicio para corregir 01 - Hash mal usado
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    hashear(clave) retorna el hash de bcrypt como texto y
    verificar(clave, hash_guardado) dice si la clave es correcta.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import bcrypt


def hashear(clave):
    return bcrypt.hashpw(clave, bcrypt.gensalt()).decode()


def verificar(clave, hash_guardado):
    return hashear(clave) == hash_guardado


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    guardado = hashear("Secreta123")
    assert guardado.startswith("$2")
    assert verificar("Secreta123", guardado) is True, "La clave correcta no fue aceptada"
    assert verificar("otra", guardado) is False
    print("Todas las pruebas pasaron")
