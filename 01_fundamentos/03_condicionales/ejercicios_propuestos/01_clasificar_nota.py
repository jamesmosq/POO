"""
Ejercicio propuesto 01 - Clasificar una nota
Nivel: básico

Completa la función clasificar_nota(nota) para que retorne (con return) el
texto que corresponde a una nota en escala de 0 a 5:

    Menor que 0 o mayor que 5  -> "Nota inválida"
    De 0 a menos de 3.0        -> "Reprobado"
    De 3.0 a menos de 4.0      -> "Aceptable"
    De 4.0 a menos de 4.5      -> "Bueno"
    De 4.5 a 5.0               -> "Excelente"

La línea def ya está escrita; solo completa el cuerpo. Las funciones se
estudian a fondo en el tema 04. Por ahora basta saber que:
    - nota es el valor que recibe la función.
    - return entrega el resultado y termina la función.

Conceptos: if, elif, else, orden de las condiciones.
"""


def clasificar_nota(nota):
    # Escribe tu solución aquí
    pass


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    casos = {
        -1: "Nota inválida", 5.1: "Nota inválida",
        0: "Reprobado", 2.9: "Reprobado",
        3.0: "Aceptable", 3.9: "Aceptable",
        4.0: "Bueno", 4.4: "Bueno",
        4.5: "Excelente", 5.0: "Excelente",
    }
    for nota, esperado in casos.items():
        obtenido = clasificar_nota(nota)
        assert obtenido == esperado, f"clasificar_nota({nota}) retornó {obtenido!r}, se esperaba {esperado!r}"

    print("Todas las pruebas pasaron")
