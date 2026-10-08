"""
Ejercicio para corregir 03 - Copias y conjuntos
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    - con_iva(precios): retorna una lista NUEVA con cada precio más el 19 %.
      La lista original no debe cambiar.
          con_iva([100, 200]) -> [119.0, 238.0]
    - etiquetas_unicas(etiquetas): retorna un conjunto con las etiquetas
      sin repetir, en minúscula.
          etiquetas_unicas(["Python", "python", "POO"]) -> {"python", "poo"}

Ojo: uno de los errores no lanza ninguna excepción y daña datos que no
deberían tocarse.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


def con_iva(precios):
    resultado = precios
    for i in range(len(resultado)):
        resultado[i] = resultado[i] * 1.19
    return resultado


def etiquetas_unicas(etiquetas):
    unicas = {}
    for etiqueta in etiquetas:
        unicas.add(etiqueta.lower())
    return unicas


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    originales = [100, 200]
    assert [round(p, 2) for p in con_iva(originales)] == [119.0, 238.0]
    assert originales == [100, 200], f"La lista original cambió: {originales}"

    assert etiquetas_unicas(["Python", "python", "POO"]) == {"python", "poo"}
    assert etiquetas_unicas([]) == set()

    print("Todas las pruebas pasaron")
