"""
Solución - Ejercicio propuesto 03 - Crear tu propio módulo

La solución está en el archivo conversiones.py de esta misma carpeta.

Respuesta a la pregunta: cuando se importa, __name__ vale "conversiones"
(el nombre del módulo). Cuando se ejecuta directamente, vale "__main__".
Por eso el bloque if __name__ == "__main__": solo corre en el segundo caso.
"""

# Este ejercicio se resuelve en el archivo conversiones.py.


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import io
    import contextlib

    salida = io.StringIO()
    with contextlib.redirect_stdout(salida):
        import conversiones
        from conversiones import celsius_a_fahrenheit, fahrenheit_a_celsius

    assert salida.getvalue() == "", (
        "Importar conversiones no debe imprimir nada: "
        "pon la prueba rápida dentro de if __name__ == '__main__':"
    )
    assert celsius_a_fahrenheit(100) == 212
    assert fahrenheit_a_celsius(32) == 0
    assert conversiones.ESCALAS == ("C", "F")
    assert conversiones.__name__ == "conversiones"

    print("Todas las pruebas pasaron")
