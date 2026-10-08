"""
Ejercicio para corregir 04 - Edad con fechas
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - leer_fecha(texto): convierte un texto "aaaa-mm-dd" en una fecha (date).
    - dias_vividos(nacimiento, hoy): días entre las dos fechas.
    - edad(nacimiento, hoy): años cumplidos. Si este año todavía no ha
      llegado el cumpleaños, la persona tiene un año menos.

        nacimiento "2000-10-09", hoy "2026-10-08" -> edad 25 (cumple mañana)

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from datetime import datetime


def leer_fecha(texto):
    return datetime.strptime(texto, "%d/%m/%Y").date()


def dias_vividos(nacimiento, hoy):
    return (hoy - nacimiento).day


def edad(nacimiento, hoy):
    return dias_vividos(nacimiento, hoy) // 365


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from datetime import date

    hoy = leer_fecha("2026-10-08")
    assert hoy == date(2026, 10, 8)

    assert dias_vividos(date(2026, 10, 1), hoy) == 7
    assert edad(date(2000, 10, 8), hoy) == 26
    assert edad(date(2000, 10, 9), hoy) == 25, f"Todavía no cumple: {edad(date(2000, 10, 9), hoy)}"
    assert edad(date(2000, 1, 1), date(2000, 12, 31)) == 0

    print("Todas las pruebas pasaron")
