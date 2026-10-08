"""
Solución - Ejercicio propuesto 04 - Tiempo en segundos
"""

segundos_totales = 7384

horas = segundos_totales // 3600          # 7384 // 3600 = 2
segundos_restantes = segundos_totales % 3600  # 7384 % 3600 = 184
minutos = segundos_restantes // 60        # 184 // 60 = 3
segundos = segundos_restantes % 60        # 184 % 60 = 4

texto = f"{horas}h {minutos}m {segundos}s"
print(texto)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert (horas, minutos, segundos) == (2, 3, 4), (horas, minutos, segundos)
    assert type(horas) is int and type(minutos) is int and type(segundos) is int, (
        "Los tres valores deben ser enteros: usa // y %"
    )
    assert texto == "2h 3m 4s", texto

    print("Todas las pruebas pasaron")
