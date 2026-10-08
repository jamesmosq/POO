"""
Solución - Ejercicio para corregir 04 - Notificaciones

CORRECCIÓN 1 (AttributeError: 'SMS' object has no attribute 'destino'):
SMS reemplazaba __init__ sin llamar al del padre, y además guardaba el dato
con otro nombre. Si no hay nada nuevo que inicializar, lo mejor es no
escribir __init__ en la hija.

CORRECCIÓN 2: SMS sobrescribía enviar() en lugar de formatear(). Así se
saltaba la validación y el registro en el historial, que están en enviar()
del padre. Las hijas solo deben cambiar la parte que es distinta.

CORRECCIÓN 3: el historial guardaba el mensaje original en lugar del texto
ya formateado.
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
        Notificacion.historial.append(texto)  # CORRECCIÓN 3
        return texto


class Email(Notificacion):
    def formatear(self, mensaje):
        return f"EMAIL a {self.destino}: {mensaje}"


class SMS(Notificacion):  # CORRECCIÓN 1: se usa el __init__ del padre
    def formatear(self, mensaje):  # CORRECCIÓN 2
        return f"SMS a {self.destino}: {mensaje}"


# ----------------------------------------------------------------------
# Pruebas
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
