"""
Ejercicio propuesto 01 - Hash con bcrypt
Nivel: básico

bcrypt es un algoritmo hecho para guardar contraseñas: es lento a
propósito (para dificultar los ataques de fuerza bruta) y agrega una sal
aleatoria en cada hash. La sal queda guardada DENTRO del mismo hash.

    hash = bcrypt.hashpw(clave_en_bytes, bcrypt.gensalt())
    bcrypt.checkpw(clave_en_bytes, hash_en_bytes)  -> True / False

bcrypt trabaja con bytes, no con textos: se convierte con .encode() y se
vuelve a texto con .decode().

Requisitos:
1. hashear(clave): retorna el hash como TEXTO (str), listo para guardar en
   una columna VARCHAR.
2. verificar(clave, hash_guardado): True si la clave corresponde al hash.
   OJO: no se puede verificar calculando otro hash y comparando con ==,
   porque cada hash lleva una sal distinta. Usa bcrypt.checkpw.

Este ejercicio no usa la base de datos.

Conceptos: hashing de contraseñas, sal, bytes y str.
"""
import bcrypt

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
