"""
Ejercicio propuesto 05 - Simulaciones con colas
Nivel: avanzado

Requisitos:
1. papa_caliente(nombres, pases): los jugadores están en círculo y se pasan
   la papa. Después de "pases" pases, el que la tiene queda eliminado. Se
   repite hasta que queda uno. Retorna (orden_de_eliminacion, ganador).
   Usa una deque: un pase es mover al primero al final, y deque tiene un
   método que lo hace: rotate(-1).

       papa_caliente(["Ana", "Luis", "Eva", "Pedro"], 2)
           -> (["Eva", "Luis", "Pedro"], "Ana")

2. imprimir_trabajos(trabajos, paginas_por_minuto): una impresora recibe
   trabajos en una cola, como tuplas (nombre, paginas), y los imprime en
   orden. Retorna una lista de tuplas (nombre, minuto_en_que_termina).
   Cada trabajo tarda las páginas divididas entre la velocidad, redondeando
   hacia ARRIBA (math.ceil), y empieza cuando termina el anterior.

       imprimir_trabajos([("tesis", 25), ("foto", 1)], 10)
           -> [("tesis", 3), ("foto", 4)]

Conceptos: deque.rotate, simulación, tiempo acumulado.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert papa_caliente(["Ana", "Luis", "Eva", "Pedro"], 2) == (["Eva", "Luis", "Pedro"], "Ana")
    assert papa_caliente(["Solo"], 5) == ([], "Solo")
    eliminados, ganador = papa_caliente(["A", "B", "C", "D", "E", "F", "G"], 3)
    assert ganador == "B" and eliminados == ["D", "A", "F", "E", "G", "C"], (eliminados, ganador)

    assert imprimir_trabajos([("tesis", 25), ("foto", 1)], 10) == [("tesis", 3), ("foto", 4)]
    assert imprimir_trabajos([("a", 10), ("b", 10), ("c", 5)], 10) == [("a", 1), ("b", 2), ("c", 3)]
    assert imprimir_trabajos([], 10) == []

    print("Todas las pruebas pasaron")
