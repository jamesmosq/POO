"""
Ejercicio propuesto 04 - Tiempo en segundos
Nivel: intermedio

Un cronómetro entrega el tiempo total en segundos. Hay que mostrarlo en
horas, minutos y segundos.

Requisitos:
1. Usa la variable segundos_totales.
2. Calcula horas, minutos y segundos (todos enteros). Usa:
       //  división entera (cuántas veces cabe)
       %   residuo (lo que sobra)
3. Crea la variable texto con el formato "2h 3m 4s".

Ejemplo: 7384 segundos son 2 horas (7200 s), quedan 184 s; eso es 3 minutos
(180 s) y quedan 4 segundos.

Conceptos: división entera, módulo, tipos int.
"""

segundos_totales = 7384

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert (horas, minutos, segundos) == (2, 3, 4), (horas, minutos, segundos)
    assert type(horas) is int and type(minutos) is int and type(segundos) is int, (
        "Los tres valores deben ser enteros: usa // y %"
    )
    assert texto == "2h 3m 4s", texto

    print("Todas las pruebas pasaron")
