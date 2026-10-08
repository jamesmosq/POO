"""
Ejercicio propuesto 03 - Crear tu propio módulo
Nivel: intermedio

Un módulo es simplemente un archivo .py. Cualquier función que escribas en
él se puede importar desde otro archivo de la misma carpeta.

Requisitos:
1. Crea, en esta misma carpeta, el archivo conversiones.py con:
       celsius_a_fahrenheit(c)  -> c * 9 / 5 + 32
       fahrenheit_a_celsius(f)  -> (f - 32) * 5 / 9
       ESCALAS = ("C", "F")     (una constante)
2. Al final de conversiones.py agrega un bloque de prueba rápida:
       if __name__ == "__main__":
           print(celsius_a_fahrenheit(100))
   Ese bloque se ejecuta cuando corres conversiones.py directamente, pero
   NO cuando otro archivo lo importa.
3. No modifiques este archivo: las pruebas de abajo importan tu módulo.

Pregunta para pensar: ¿qué valor tiene __name__ dentro de conversiones.py
cuando lo importas? ¿Y cuando lo ejecutas directamente?

Conceptos: módulos propios, import, from ... import, __name__.
"""

# Este ejercicio se resuelve en el archivo conversiones.py.


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
