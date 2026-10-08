"""
Ejercicio para corregir 04 - Lista de notas protegida
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - Boletin.agregar_nota(nota): solo acepta notas entre 0 y 5.
    - Boletin.notas: propiedad que retorna las notas SIN permitir que se
      modifiquen desde afuera (retorna una tupla).
    - Boletin.promedio: propiedad con el promedio (0 si no hay notas).

Ojo: el programa no lanza errores, pero se puede "colar" una nota inválida
de dos maneras distintas.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Boletin:
    def __init__(self):
        self._notas = []

    def agregar_nota(self, nota):
        if nota < 0 and nota > 5:
            raise ValueError("La nota debe estar entre 0 y 5")
        self._notas.append(nota)

    @property
    def notas(self):
        return self._notas

    @property
    def promedio(self):
        if not self._notas:
            return 0
        sum(self._notas) / len(self._notas)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    b = Boletin()
    b.agregar_nota(4.0)
    b.agregar_nota(3.0)

    try:
        b.agregar_nota(7)
        raise AssertionError("Una nota de 7 debe lanzar ValueError")
    except ValueError:
        pass

    notas = b.notas
    try:
        notas.append(99)
    except AttributeError:
        pass
    assert b.notas == (4.0, 3.0), f"Las notas cambiaron desde afuera: {b.notas}"
    assert b.promedio == 3.5, f"promedio vale {b.promedio}"

    print("Todas las pruebas pasaron")
