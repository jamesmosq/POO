"""
Ejercicio propuesto 02 - Estadísticas de notas
Nivel: básico

Requisitos:
1. Escribe la función estadisticas(nota1, nota2, nota3) que retorne TRES
   valores: la nota más baja, la más alta y el promedio redondeado a 2
   decimales.
       estadisticas(3.0, 4.5, 4.0)  ->  (3.0, 4.5, 3.83)
2. Escribe la función aprobo(nota1, nota2, nota3) que retorne True si el
   promedio es 3.0 o más. Reutiliza estadisticas() en lugar de volver a
   calcular el promedio.

Pistas: min(), max() y round() son funciones que ya trae Python.
Una función retorna varios valores separándolos con comas:
    return a, b, c
y quien la llama los recibe así:
    minimo, maximo, promedio = estadisticas(3.0, 4.5, 4.0)

Conceptos: retornar varios valores, desempaquetar, reutilizar funciones.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert estadisticas(3.0, 4.5, 4.0) == (3.0, 4.5, 3.83)
    minimo, maximo, promedio = estadisticas(5, 5, 5)
    assert (minimo, maximo, promedio) == (5, 5, 5)

    assert aprobo(3.0, 3.0, 3.0) is True
    assert aprobo(2.0, 3.5, 3.4) is False
    assert aprobo(4.0, 2.0, 3.5) is True

    print("Todas las pruebas pasaron")
