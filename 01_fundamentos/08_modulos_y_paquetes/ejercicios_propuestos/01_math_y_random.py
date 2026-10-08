"""
Ejercicio propuesto 01 - Módulos math y random
Nivel: básico

Python trae muchos módulos listos para usar (la "biblioteca estándar").
Se usan con import.

Requisitos:
1. Importa el módulo math y escribe:
   - area_circulo(radio): usa math.pi. Redondea a 2 decimales.
   - hipotenusa(a, b): usa math.sqrt (o math.hypot).
2. Importa el módulo random y escribe:
   - lanzar_dados(cantidad, semilla): retorna una lista con cantidad
     números entre 1 y 6. Crea un generador con random.Random(semilla) y
     usa su método randint(1, 6).

   ¿Para qué sirve la semilla? Con la misma semilla, el generador produce
   siempre la misma secuencia. Así un programa con azar se puede probar.

Conceptos: import, módulos de la biblioteca estándar, math, random.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert area_circulo(1) == 3.14
    assert area_circulo(2.5) == 19.63
    assert hipotenusa(3, 4) == 5

    tirada = lanzar_dados(100, semilla=42)
    assert len(tirada) == 100
    assert all(1 <= d <= 6 for d in tirada), "Los dados van de 1 a 6"
    assert set(tirada) == {1, 2, 3, 4, 5, 6}, "En 100 lanzamientos deberían salir todos los números"
    assert lanzar_dados(10, semilla=7) == lanzar_dados(10, semilla=7), "La misma semilla da los mismos dados"

    print("Todas las pruebas pasaron")
