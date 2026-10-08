"""
Solución - Ejercicio para corregir 04 - Promedio y perfil

CORRECCIÓN 1 (TypeError: unsupported operand type(s) for +: 'int' and
'list'): promedio(lista) envía la lista como UN solo argumento, entonces
notas queda como ([2, 4],). Con promedio(*lista) cada elemento llega como
argumento separado.

CORRECCIÓN 2 (ZeroDivisionError): sin notas, len(notas) es 0. Hay que
revisar ese caso antes de dividir.

CORRECCIÓN 3 (TypeError: got an unexpected keyword argument 'edad'): *datos
recibe argumentos sueltos por posición (tupla). Para recibir argumentos con
nombre (edad=20) se usa **datos (diccionario).
"""

def promedio(*notas):
    if len(notas) == 0:  # CORRECCIÓN 2
        return 0
    return sum(notas) / len(notas)


def promedio_de_lista(lista):
    return promedio(*lista)  # CORRECCIÓN 1


def crear_perfil(nombre, **datos):  # CORRECCIÓN 3
    return {"nombre": nombre, **datos}


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert promedio(3, 4, 5) == 4.0
    assert promedio_de_lista([2, 4]) == 3.0
    assert promedio() == 0
    assert crear_perfil("Ana", edad=20) == {"nombre": "Ana", "edad": 20}
    assert crear_perfil("Luis") == {"nombre": "Luis"}

    print("Todas las pruebas pasaron")
