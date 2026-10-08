"""
Solución - Ejercicio propuesto 04 - Notificaciones
"""

class Notificacion:
    enviadas = []

    def __init__(self, destino):
        self.destino = destino

    def formatear(self, mensaje):
        raise NotImplementedError("Cada notificación debe implementar formatear()")

    def enviar(self, mensaje):
        if not mensaje:
            raise ValueError("El mensaje no puede estar vacío")
        texto = self.formatear(mensaje)
        Notificacion.enviadas.append(texto)
        return texto


class Email(Notificacion):
    def formatear(self, mensaje):
        return f"Para: {self.destino} | Asunto: Aviso | {mensaje}"


class SMS(Notificacion):
    LIMITE = 20

    def formatear(self, mensaje):
        if len(mensaje) > self.LIMITE:
            mensaje = mensaje[:self.LIMITE] + "..."
        return f"SMS a {self.destino}: {mensaje}"


class Push(Notificacion):
    def formatear(self, mensaje):
        return f"[PUSH] {mensaje}"


def notificar_a_todos(notificaciones, mensaje):
    return [notificacion.enviar(mensaje) for notificacion in notificaciones]


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Notificacion.enviadas = []
    medios = [Email("ana@mail.com"), SMS("3001234567"), Push("app-123")]
    resultado = notificar_a_todos(medios, "Hola")
    assert resultado == [
        "Para: ana@mail.com | Asunto: Aviso | Hola",
        "SMS a 3001234567: Hola",
        "[PUSH] Hola",
    ]
    assert len(Notificacion.enviadas) == 3

    largo = SMS("300").enviar("Este mensaje es demasiado largo")
    assert largo == "SMS a 300: Este mensaje es dema...", largo

    try:
        Push("x").enviar("")
        raise AssertionError("Un mensaje vacío debe lanzar ValueError")
    except ValueError:
        pass

    try:
        Notificacion("x").enviar("Hola")
        raise AssertionError("La base no sabe formatear: debe lanzar NotImplementedError")
    except NotImplementedError:
        pass

    print("Todas las pruebas pasaron")
