"""
Ejercicio para corregir 02 - Smartphone
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Telefono y Camara definen los dos el método descripcion(). Un
    Smartphone hereda de ambos y debe describirse PRIMERO como cámara:
    su descripcion() agrega " con apps" a la descripción que hereda.

        Smartphone().descripcion() -> "Cámara de 50 MP con apps"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Telefono:
    def llamar(self, numero):
        return f"Llamando a {numero}"

    def descripcion(self):
        return "Teléfono con llamadas"


class Camara:
    def fotografiar(self):
        return "Foto tomada"

    def descripcion(self):
        return "Cámara de 50 MP"


class Smartphone(Telefono, Camara):
    def descripcion(self):
        return super().descripcion + " con apps"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    s = Smartphone()
    assert s.llamar("300") == "Llamando a 300"
    assert s.fotografiar() == "Foto tomada"
    assert s.descripcion() == "Cámara de 50 MP con apps", s.descripcion()

    print("Todas las pruebas pasaron")
