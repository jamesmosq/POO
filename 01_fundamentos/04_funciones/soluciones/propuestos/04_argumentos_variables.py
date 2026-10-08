"""
Solución - Ejercicio propuesto 04 - Argumentos variables
"""

def sumar_todos(*numeros):
    # numeros es una tupla con todos los argumentos recibidos.
    return sum(numeros)


def promedio(*numeros):
    if len(numeros) == 0:
        return 0
    return sumar_todos(*numeros) / len(numeros)


def crear_perfil(nombre, **datos):
    # datos es un diccionario con los argumentos que se pasaron por nombre.
    return {"nombre": nombre, **datos}


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert sumar_todos() == 0
    assert sumar_todos(5) == 5
    assert sumar_todos(1, 2, 3, 4) == 10

    assert promedio() == 0
    assert promedio(2, 4, 6) == 4
    notas = (3.0, 4.0, 5.0)
    assert promedio(*notas) == 4.0

    assert crear_perfil("Ana") == {"nombre": "Ana"}
    assert crear_perfil("Ana", edad=20, ciudad="Cali") == {"nombre": "Ana", "edad": 20, "ciudad": "Cali"}

    print("Todas las pruebas pasaron")
