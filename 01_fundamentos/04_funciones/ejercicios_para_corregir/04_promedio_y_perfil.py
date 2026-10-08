"""
Ejercicio para corregir 04 - Promedio y perfil
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - promedio(*notas): promedio de las notas recibidas; 0 si no recibe
      ninguna.
    - promedio_de_lista(lista): promedio de una lista de notas, usando la
      función promedio.
    - crear_perfil(nombre, **datos): diccionario con el nombre y los datos
      adicionales.

        promedio(3, 4, 5)                    -> 4.0
        promedio()                           -> 0
        promedio_de_lista([2, 4])            -> 3.0
        crear_perfil("Ana", edad=20)         -> {"nombre": "Ana", "edad": 20}

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def promedio(*notas):
    return sum(notas) / len(notas)


def promedio_de_lista(lista):
    return promedio(lista)


def crear_perfil(nombre, *datos):
    return {"nombre": nombre, **datos}


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert promedio(3, 4, 5) == 4.0
    assert promedio_de_lista([2, 4]) == 3.0
    assert promedio() == 0
    assert crear_perfil("Ana", edad=20) == {"nombre": "Ana", "edad": 20}
    assert crear_perfil("Luis") == {"nombre": "Luis"}

    print("Todas las pruebas pasaron")
