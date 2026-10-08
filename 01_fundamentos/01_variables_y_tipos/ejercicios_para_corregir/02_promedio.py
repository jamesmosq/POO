"""
Ejercicio para corregir 02 - Promedio de notas
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Calcular el promedio de tres notas. Con 3.5, 4.0 y 4.5 el promedio es 4.0.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

nota1 = 3.5
nota2 = 4.0
nota3 = 4.5

promedio = nota1 + Nota2 + nota3 / 3
print("Promedio:", promedio)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert promedio == 4.0, f"promedio vale {promedio}"

    print("Todas las pruebas pasaron")
