"""
Ejercicio para corregir 05 - Reloj digital
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    Convertir una cantidad de segundos al formato de reloj HH:MM:SS.

        3725 segundos -> 1 hora, 2 minutos y 5 segundos -> "01:02:05"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

segundos_totales = 3725

horas = segundos_totales / 3600
minutos = segundos_totales % 3600 / 60
segundos = segundos_totales // 60

reloj = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
print(reloj)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert (horas, minutos, segundos) == (1, 2, 5), (horas, minutos, segundos)
    assert reloj == "01:02:05", reloj

    print("Todas las pruebas pasaron")
