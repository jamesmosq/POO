"""
Solución - Ejercicio para corregir 02 - Clima

CORRECCIÓN 1 (SyntaxError: expected ':'): en Python no existe "else if";
se escribe elif. El mensaje confunde porque Python lee "else" y espera que
lo siga ":" de inmediato.

CORRECCIÓN 2 (resultado incorrecto): las condiciones se revisan en orden y
se ejecuta solo la primera que se cumple. Como 30 > 10 es verdadero, nunca
se llegaba a "Caluroso". Cuando las condiciones se solapan, la más
restrictiva (> 25) debe ir primero.
"""

def clima(temperatura):
    if temperatura > 25:  # CORRECCIÓN 2
        return "Caluroso"
    elif temperatura > 10:  # CORRECCIÓN 1
        return "Templado"
    else:
        return "Frío"


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert clima(30) == "Caluroso", f"clima(30) retornó {clima(30)!r}"
    assert clima(26) == "Caluroso"
    assert clima(25) == "Templado"
    assert clima(11) == "Templado"
    assert clima(10) == "Frío"
    assert clima(-3) == "Frío"

    print("Todas las pruebas pasaron")
