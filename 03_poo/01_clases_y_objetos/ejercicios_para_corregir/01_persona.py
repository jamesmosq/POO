"""
Ejercicio para corregir 01 - Persona
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Persona("Ana", 20).saludar() -> "Hola, soy Ana"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Persona:
    def __int__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar():
        return f"Hola, soy {self.nombre}"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Persona("Ana", 20)
    assert ana.edad == 20
    assert ana.saludar() == "Hola, soy Ana"

    print("Todas las pruebas pasaron")
