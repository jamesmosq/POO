"""
Solución - Ejercicio para corregir 04 - Edad con fechas

CORRECCIÓN 1 (ValueError: time data '2026-10-08' does not match format):
el formato debe describir exactamente cómo viene el texto. "2026-10-08" es
año-mes-día con guiones: "%Y-%m-%d".

CORRECCIÓN 2 (AttributeError: 'datetime.timedelta' object has no attribute
'day'): la diferencia entre dos fechas es un timedelta, y su atributo es
days (en plural).

CORRECCIÓN 3 (edad incorrecta): dividir los días entre 365 no funciona
porque los años bisiestos tienen 366 días; cerca del cumpleaños el
resultado sale con un año de más. Se restan los años y se descuenta uno si
el cumpleaños todavía no ha llegado.
"""

from datetime import datetime


def leer_fecha(texto):
    return datetime.strptime(texto, "%Y-%m-%d").date()  # CORRECCIÓN 1


def dias_vividos(nacimiento, hoy):
    return (hoy - nacimiento).days  # CORRECCIÓN 2


def edad(nacimiento, hoy):
    anios = hoy.year - nacimiento.year  # CORRECCIÓN 3
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        anios -= 1
    return anios


# ----------------------------------------------------------------------
# Pruebas
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
