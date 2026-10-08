"""
Ejercicio propuesto 01 - Lista de compras
Nivel: básico

Requisitos:
1. agregar(lista, producto): agrega el producto al final, pero solo si no
   está ya en la lista (sin importar mayúsculas: "Pan" y "pan" son el
   mismo). Guarda los productos en minúscula. Retorna True si lo agregó y
   False si ya estaba.
2. quitar(lista, producto): elimina el producto si está. Retorna True o
   False según si lo encontró.
3. ordenada(lista): retorna una lista NUEVA ordenada alfabéticamente; la
   original no cambia. Pista: sorted() frente a lista.sort().
4. primeros(lista, n): retorna los primeros n productos usando slicing:
   lista[inicio:fin].

Conceptos: listas, in, append, remove, sorted, slicing.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
