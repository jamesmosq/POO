"""
Solución - Ejercicio para corregir 03 - Copias y conjuntos

CORRECCIÓN 1 (la lista original cambiaba): resultado = precios no copia la
lista, solo crea otro nombre para la MISMA lista. Todo lo que se haga con
resultado afecta a precios. Hay que construir una lista nueva (o copiar con
precios.copy() o list(precios)).

CORRECCIÓN 2 (AttributeError: 'dict' object has no attribute 'add'): {}
crea un diccionario vacío, no un conjunto. El conjunto vacío se crea con
set().
"""

def con_iva(precios):
    resultado = []  # CORRECCIÓN 1
    for precio in precios:
        resultado.append(precio * 1.19)
    return resultado


def etiquetas_unicas(etiquetas):
    unicas = set()  # CORRECCIÓN 2
    for etiqueta in etiquetas:
        unicas.add(etiqueta.lower())
    return unicas


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    originales = [100, 200]
    assert [round(p, 2) for p in con_iva(originales)] == [119.0, 238.0]
    assert originales == [100, 200], f"La lista original cambió: {originales}"

    assert etiquetas_unicas(["Python", "python", "POO"]) == {"python", "poo"}
    assert etiquetas_unicas([]) == set()

    print("Todas las pruebas pasaron")
