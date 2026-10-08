"""
Ejercicio propuesto 02 - Burbuja optimizada
Nivel: básico

El método de la burbuja compara elementos vecinos y los intercambia si
están en el orden equivocado. Después de cada pasada, el mayor queda al
final.

Requisitos. Escribe burbuja(lista), que:
1. Retorne una lista NUEVA ordenada de menor a mayor (no modifiques la
   original; trabaja sobre lista.copy()).
2. Esté optimizada de dos formas:
   a. En cada pasada no revise los elementos que ya quedaron al final.
   b. Si en una pasada no hubo ningún intercambio, la lista ya está
      ordenada: termina antes (usa una variable bandera).
3. Retorne también cuántas pasadas hizo: (lista_ordenada, pasadas).

Para intercambiar dos elementos en Python:
    a, b = b, a

Conceptos: ordenamiento por burbuja, bandera, optimización.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [5, 1, 4, 2, 8]
    ordenada, pasadas = burbuja(datos)
    assert ordenada == [1, 2, 4, 5, 8]
    assert datos == [5, 1, 4, 2, 8], "No debe modificar la lista original"

    _, pasadas = burbuja([1, 2, 3, 4, 5])
    assert pasadas == 1, f"Una lista ya ordenada necesita una sola pasada, hizo {pasadas}"

    _, pasadas = burbuja([5, 4, 3, 2, 1])
    assert pasadas <= 5

    assert burbuja([])[0] == []
    assert burbuja(["pera", "Uva", "manzana"])[0] == ["Uva", "manzana", "pera"]

    print("Todas las pruebas pasaron")
