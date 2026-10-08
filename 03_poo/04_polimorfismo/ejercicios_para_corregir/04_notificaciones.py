"""
Ejercicio para corregir 04 - Notificaciones
Nivel: intermedio
Errores a encontrar: 3

Qué debería hacer el programa:
    - Notificacion.enviar(mensaje) valida el mensaje, llama a formatear() y
      registra el resultado en la lista de la clase Notificacion.historial.
      Las hijas solo deben implementar formatear().
    - Email -> "EMAIL a ana@mail.com: Hola"
    - SMS   -> "SMS a 300: Hola"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Notificacion:
    historial = []

    def __init__(self, destino):
        self.destino = destino

    def formatear(self, mensaje):
        raise NotImplementedError

    def enviar(self, mensaje):
        if not mensaje:
            raise ValueError("Mensaje vacío")
        texto = self.formatear(mensaje)
        Notificacion.historial.append(mensaje)
        return texto


class Email(Notificacion):
    def formatear(self, mensaje):
        return f"EMAIL a {self.destino}: {mensaje}"


class SMS(Notificacion):
    def __init__(self, numero):
        self.numero = numero

    def enviar(self, mensaje):
        return f"SMS a {self.destino}: {mensaje}"


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Notificacion.historial = []
    assert Email("ana@mail.com").enviar("Hola") == "EMAIL a ana@mail.com: Hola"
    assert SMS("300").enviar("Hola") == "SMS a 300: Hola"
    assert Notificacion.historial == ["EMAIL a ana@mail.com: Hola", "SMS a 300: Hola"], Notificacion.historial

    try:
        SMS("300").enviar("")
        raise AssertionError("Un mensaje vacío debe lanzar ValueError")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
