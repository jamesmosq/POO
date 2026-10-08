"""
Solución - Ejercicio para corregir 02 - Promedio de notas

CORRECCIÓN 1 (NameError: name 'Nota2' is not defined): Python distingue
mayúsculas de minúsculas. Nota2 y nota2 son variables distintas.

CORRECCIÓN 2 (resultado incorrecto, 9.5 en lugar de 4.0): la división se
evalúa antes que la suma, así que solo nota3 se dividía entre 3. Los
paréntesis obligan a sumar primero.
"""

nota1 = 3.5
nota2 = 4.0
nota3 = 4.5

promedio = (nota1 + nota2 + nota3) / 3  # CORRECCIÓN 1 y 2
print("Promedio:", promedio)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert promedio == 4.0, f"promedio vale {promedio}"

    print("Todas las pruebas pasaron")
