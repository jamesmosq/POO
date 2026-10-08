"""
Ejercicio para corregir 01 - Saludo
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Construir el mensaje "Ana tiene 20 años" a partir de un nombre y una edad.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

1er_nombre = "Ana"
edad = 20

mensaje = 1er_nombre + " tiene " + edad + " años"
print(mensaje)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert edad == 20
    assert mensaje == "Ana tiene 20 años", mensaje

    print("Todas las pruebas pasaron")
