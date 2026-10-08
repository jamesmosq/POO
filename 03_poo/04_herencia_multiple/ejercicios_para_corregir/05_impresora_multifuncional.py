"""
Ejercicio para corregir 05 - Impresora multifuncional (herencia en diamante)
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    Impresora y Escaner heredan de Dispositivo. Multifuncional hereda de
    las dos, lo que forma un "diamante":

                Dispositivo
                /         \\
          Impresora     Escaner
                \\         /
              Multifuncional

    - Crear una Multifuncional debe inicializar Dispositivo UNA sola vez
      (Dispositivo.total_creados cuenta cuántos dispositivos se crearon).
    - Una Multifuncional imprime como una Impresora.
    - encender() agrega ", modo multifuncional" al mensaje de Dispositivo.

Pista: investiga qué es el MRO y por qué super() es la forma correcta de
inicializar en herencia múltiple, en lugar de llamar a cada padre por su
nombre.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Dispositivo:
    total_creados = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Dispositivo.total_creados += 1

    def encender(self):
        return f"{self.nombre} encendido"


class Impresora(Dispositivo):
    def __init__(self, nombre):
        Dispositivo.__init__(self, nombre)

    def imprimir(self, texto):
        return f"Imprimiendo: {texto}"


class Escaner(Dispositivo):
    def __init__(self, nombre):
        Dispositivo.__init__(self, nombre)

    def escanear(self):
        return "Escaneando documento"

    def imprimir(self, texto):
        return "Este equipo no imprime"


class Multifuncional(Escaner, Impresora):
    def __init__(self, nombre):
        Impresora.__init__(self, nombre)
        Escaner.__init__(self, nombre)

    def encender(self):
        return super.encender() + ", modo multifuncional"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Dispositivo.total_creados = 0
    equipo = Multifuncional("HP 2775")
    assert Dispositivo.total_creados == 1, (
        f"Se inicializó Dispositivo {Dispositivo.total_creados} veces"
    )

    assert equipo.imprimir("informe.pdf") == "Imprimiendo: informe.pdf"
    assert equipo.escanear() == "Escaneando documento"
    assert equipo.encender() == "HP 2775 encendido, modo multifuncional"

    assert Escaner("Epson").imprimir("x") == "Este equipo no imprime"

    print("Todas las pruebas pasaron")
