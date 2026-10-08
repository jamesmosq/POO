"""
Solución - Ejercicio para corregir 03 - Contador de visitas

CORRECCIÓN 1 (UnboundLocalError: cannot access local variable 'visitas'):
al asignar visitas dentro de la función, Python la trata como una variable
local nueva, que todavía no tiene valor cuando se intenta sumar. Para
modificar la variable global hay que declararlo con global.
Nota: en programas grandes es mejor evitar variables globales y pasar o
retornar los valores; aquí se usa global para entender el concepto.

CORRECCIÓN 2 (mensaje era una función): mensaje_de_bienvenida sin
paréntesis es la función en sí, no su resultado. Para ejecutarla hacen
falta los paréntesis: mensaje_de_bienvenida().
"""

visitas = 0


def registrar_visita():
    global visitas  # CORRECCIÓN 1
    visitas = visitas + 1
    return visitas


def mensaje_de_bienvenida():
    return f"Bienvenido, eres la visita número {visitas}"


registrar_visita()
registrar_visita()
registrar_visita()
mensaje = mensaje_de_bienvenida()  # CORRECCIÓN 2


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert visitas == 3, f"visitas vale {visitas}"
    assert mensaje == "Bienvenido, eres la visita número 3", f"mensaje vale {mensaje!r}"

    print("Todas las pruebas pasaron")
