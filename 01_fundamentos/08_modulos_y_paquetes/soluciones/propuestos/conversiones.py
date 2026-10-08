"""
Solución del ejercicio propuesto 03: módulo de conversiones de temperatura.
"""

ESCALAS = ("C", "F")


def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    # Solo se ejecuta con: python conversiones.py
    print(celsius_a_fahrenheit(100))
