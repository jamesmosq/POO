"""
Ejercicio propuesto 03 - Búsqueda binaria
Nivel: intermedio

La búsqueda binaria solo funciona sobre listas ORDENADAS. En cada paso
mira el elemento del medio:
    - si es el objetivo, terminó;
    - si el objetivo es menor, descarta la mitad derecha;
    - si es mayor, descarta la mitad izquierda.

Requisitos. Escribe busqueda_binaria(lista, objetivo), que retorne
(posicion, pasos):
    - posicion: índice del objetivo, o -1 si no está.
    - pasos: cuántas veces se revisó un elemento del medio.
Usa dos índices, inicio y fin, y un ciclo while. El medio se calcula con
división entera: (inicio + fin) // 2.

Compara con la búsqueda lineal: en una lista de 1.000.000 de elementos,
la binaria necesita como máximo unos 20 pasos.

Conceptos: divide y vencerás, índices, while.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    datos = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    for i, valor in enumerate(datos):
        posicion, _ = busqueda_binaria(datos, valor)
        assert posicion == i, f"{valor} está en la posición {i}, se obtuvo {posicion}"

    assert busqueda_binaria(datos, 23)[0] == 5
    assert busqueda_binaria(datos, 4)[0] == -1
    assert busqueda_binaria(datos, 100)[0] == -1
    assert busqueda_binaria([], 1)[0] == -1

    grande = list(range(1_000_000))
    posicion, pasos = busqueda_binaria(grande, 999_999)
    assert posicion == 999_999
    assert pasos <= 20, f"Hizo {pasos} pasos; la búsqueda binaria no debería pasar de 20"

    print("Todas las pruebas pasaron")
