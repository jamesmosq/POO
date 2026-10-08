"""
Ejercicio propuesto 05 - Usuario con contraseña
Nivel: avanzado

Una contraseña nunca se guarda tal cual. Se guarda su "hash": el resultado
de una función que convierte el texto en otro texto del que no se puede
recuperar el original. Para comprobarla, se calcula el hash de lo que
escribe el usuario y se compara con el guardado.

A la contraseña se le agrega una "sal" (texto aleatorio distinto para cada
usuario), para que dos usuarios con la misma clave tengan hashes
diferentes.

Requisitos. Crea la clase Usuario(nombre, clave):
1. Genera una sal con secrets.token_hex(16) y guárdala en self._sal.
2. Guarda solo el hash en self._hash, calculado así:
       hashlib.sha256((sal + clave).encode()).hexdigest()
   Nunca guardes la clave en ningún atributo.
3. verificar(clave): True si la clave es la correcta.
4. cambiar_clave(actual, nueva): si actual no es correcta, lanza
   PermissionError. La nueva debe tener al menos 8 caracteres (si no,
   ValueError). Genera una sal nueva al cambiar la clave.
5. clave: una propiedad que al LEERLA lance AttributeError("La clave no se
   puede consultar").

Conceptos: hashing, datos sensibles, módulos hashlib y secrets.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
