"""
Ejercicio para corregir 05 - Impresora y papa caliente
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    - papa_caliente(nombres, pases): en cada ronda la papa avanza "pases"
      veces (el primero pasa al final) y se elimina a quien la tiene.
      Retorna (orden_de_eliminacion, ganador).
          papa_caliente(["Ana", "Luis", "Eva", "Pedro"], 2)
              -> (["Eva", "Luis", "Pedro"], "Ana")
    - imprimir_trabajos(trabajos, paginas_por_minuto): cada trabajo
      (nombre, paginas) tarda paginas / velocidad minutos, redondeado
      hacia ARRIBA, y empieza cuando termina el anterior. Retorna
      (nombre, minuto_en_que_termina) de cada trabajo.
          imprimir_trabajos([("tesis", 25), ("foto", 1)], 10)
              -> [("tesis", 3), ("foto", 4)]

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from collections import deque


def papa_caliente(nombres, pases):
    circulo = deque(nombres)
    eliminados = []
    while len(circulo) > 1:
        circulo.rotate(pases)
        eliminados.append(circulo.popleft())
    return eliminados, circulo[0]


def imprimir_trabajos(trabajos, paginas_por_minuto):
    cola = deque(trabajos)
    resultado = []
    while cola:
        nombre, paginas = cola.popleft()
        duracion = paginas // paginas_por_minuto
        minuto = duracion
        resultado.append((nombre, minuto))
    return resultado


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert papa_caliente(["Ana", "Luis", "Eva", "Pedro"], 2) == (["Eva", "Luis", "Pedro"], "Ana"), (
        papa_caliente(["Ana", "Luis", "Eva", "Pedro"], 2)
    )
    resultado = imprimir_trabajos([("tesis", 25), ("foto", 1)], 10)
    assert resultado == [("tesis", 3), ("foto", 4)], resultado
    assert imprimir_trabajos([("a", 10), ("b", 10)], 10) == [("a", 1), ("b", 2)]

    print("Todas las pruebas pasaron")
