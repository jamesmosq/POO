"""
Solución - Ejercicio propuesto 01 - Lista de compras
"""

def agregar(lista, producto):
    producto = producto.lower()
    if producto in lista:
        return False
    lista.append(producto)
    return True


def quitar(lista, producto):
    producto = producto.lower()
    if producto not in lista:
        return False
    lista.remove(producto)
    return True


def ordenada(lista):
    # sorted() crea una lista nueva; lista.sort() ordenaría la original.
    return sorted(lista)


def primeros(lista, n):
    # El slicing no falla si n es mayor que el largo de la lista.
    return lista[:n]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    compras = []
    assert agregar(compras, "Pan") is True
    assert agregar(compras, "leche") is True
    assert agregar(compras, "PAN") is False
    assert agregar(compras, "Arroz") is True
    assert compras == ["pan", "leche", "arroz"]

    assert ordenada(compras) == ["arroz", "leche", "pan"]
    assert compras == ["pan", "leche", "arroz"], "ordenada() no debe cambiar la original"

    assert primeros(compras, 2) == ["pan", "leche"]
    assert primeros(compras, 10) == ["pan", "leche", "arroz"]

    assert quitar(compras, "Leche") is True
    assert quitar(compras, "huevos") is False
    assert compras == ["pan", "arroz"]

    print("Todas las pruebas pasaron")
