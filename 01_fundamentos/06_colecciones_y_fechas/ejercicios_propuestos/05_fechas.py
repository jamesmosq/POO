"""
Ejercicio propuesto 05 - Fechas
Nivel: avanzado

Todas las funciones reciben la fecha de "hoy" como parámetro en lugar de
usar date.today(). Así las pruebas dan el mismo resultado cualquier día que
se ejecuten. Esta técnica se usa mucho en programas reales.

Requisitos (usa el módulo datetime):
1. calcular_edad(nacimiento, hoy): edad en años cumplidos. Ojo: si este
   año todavía no ha llegado el cumpleaños, la persona tiene un año menos.
   No dividas los días entre 365 (falla con los años bisiestos).
2. dias_hasta(fecha, hoy): cuántos días faltan para la fecha (negativo si
   ya pasó). Pista: restar dos fechas da un timedelta con .days.
3. formatear(fecha): texto "dd/mm/aaaa". Pista: strftime("%d/%m/%Y").
4. leer_fecha(texto): convierte "dd/mm/aaaa" en date. Pista:
   datetime.strptime(texto, "%d/%m/%Y").date().
5. sumar_dias_habiles(fecha, dias): avanza la cantidad de días indicada,
   contando solo de lunes a viernes. weekday() da 0 para lunes y 6 para
   domingo.

Conceptos: date, timedelta, strftime, strptime, weekday.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
