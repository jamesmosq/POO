"""
Ejercicio para corregir 04 - Cola circular
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Una cola de tamaño fijo cuyos índices dan la vuelta al llegar al final
    de la lista, para reutilizar las posiciones que se liberan.

        cola = ColaCircular(3)
        encolar a, b, c       -> llena
        encolar d             -> OverflowError
        desencolar()          -> "a"
        encolar d             -> se guarda en la posición 0

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.frente = 0
        self.cantidad = 0

    def esta_llena(self):
        return self.cantidad > self.capacidad

    def encolar(self, elemento):
        if self.esta_llena():
            raise OverflowError("La cola está llena")
        posicion = self.frente + self.cantidad
        self.datos[posicion] = elemento
        self.cantidad += 1

    def desencolar(self):
        if self.cantidad == 0:
            raise IndexError("La cola está vacía")
        elemento = self.datos[self.frente]
        self.frente = (self.frente + 1) % self.capacidad
        return elemento


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cola = ColaCircular(3)
    for letra in "abc":
        cola.encolar(letra)
    try:
        cola.encolar("d")
        raise AssertionError("La cola está llena: debe lanzar OverflowError")
    except OverflowError:
        pass

    assert cola.desencolar() == "a"
    assert cola.cantidad == 2, f"Después de desencolar, cantidad vale {cola.cantidad}"
    cola.encolar("d")
    assert cola.datos[0] == "d"
    assert [cola.desencolar() for _ in range(3)] == ["b", "c", "d"]

    print("Todas las pruebas pasaron")
