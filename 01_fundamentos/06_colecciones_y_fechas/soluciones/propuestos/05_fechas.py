"""
Solución - Ejercicio propuesto 05 - Fechas
"""

from datetime import datetime, timedelta


def calcular_edad(nacimiento, hoy):
    edad = hoy.year - nacimiento.year
    # Las tuplas (mes, día) se comparan en orden: primero el mes, luego el día.
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        edad -= 1
    return edad


def dias_hasta(fecha, hoy):
    return (fecha - hoy).days


def formatear(fecha):
    return fecha.strftime("%d/%m/%Y")


def leer_fecha(texto):
    return datetime.strptime(texto, "%d/%m/%Y").date()


def sumar_dias_habiles(fecha, dias):
    actual = fecha
    contados = 0
    while contados < dias:
        actual += timedelta(days=1)
        if actual.weekday() < 5:  # 0 = lunes ... 4 = viernes
            contados += 1
    return actual


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from datetime import date

    hoy = date(2026, 10, 8)  # jueves
    assert calcular_edad(date(2000, 10, 8), hoy) == 26
    assert calcular_edad(date(2000, 10, 9), hoy) == 25, "Todavía no cumple años"
    assert calcular_edad(date(2004, 2, 29), hoy) == 22

    assert dias_hasta(date(2026, 12, 25), hoy) == 78
    assert dias_hasta(date(2026, 10, 1), hoy) == -7

    assert formatear(date(2026, 1, 5)) == "05/01/2026"
    assert leer_fecha("24/12/2026") == date(2026, 12, 24)

    assert sumar_dias_habiles(hoy, 1) == date(2026, 10, 9)    # viernes
    assert sumar_dias_habiles(hoy, 2) == date(2026, 10, 12)   # salta el fin de semana
    assert sumar_dias_habiles(hoy, 0) == hoy

    print("Todas las pruebas pasaron")
