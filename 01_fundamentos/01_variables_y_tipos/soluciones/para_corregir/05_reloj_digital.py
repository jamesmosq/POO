"""
Solución - Ejercicio para corregir 05 - Reloj digital

CORRECCIÓN 1 (ValueError: Unknown format code 'd' for object of type
'float'): / siempre devuelve un float (1.03...). Para horas completas se usa
la división entera //.

CORRECCIÓN 2: el mismo problema con los minutos. El residuo de la hora
(125 s) se divide con // 60 para obtener 2 minutos completos.

CORRECCIÓN 3 (resultado incorrecto): segundos_totales // 60 da el total de
minutos (62), no los segundos sueltos. Los segundos son el residuo: % 60.
"""

segundos_totales = 3725

horas = segundos_totales // 3600  # CORRECCIÓN 1
minutos = segundos_totales % 3600 // 60  # CORRECCIÓN 2
segundos = segundos_totales % 60  # CORRECCIÓN 3

reloj = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
print(reloj)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert (horas, minutos, segundos) == (1, 2, 5), (horas, minutos, segundos)
    assert reloj == "01:02:05", reloj

    print("Todas las pruebas pasaron")
