class EmailNotificador:
    def enviar(self, mensaje):
        return f"📧 Email: {mensaje} 🥶"


class SMSNotificador:
    def enviar(self, mensaje):
        return f"📱 SMS: {mensaje}"


class PushNotificador:
    def enviar(self, mensaje):
        return f"🔔 Push: {mensaje}"


class SistemaNotificaciones:
    def __init__(self):
        self.notificadores = []

    def agregar_notificador(self, notificador):
        # Duck typing: solo necesita tener método 'enviar'
        self.notificadores.append(notificador)

    def notificar_todos(self, mensaje):
        for notificador in self.notificadores:
            print(notificador.enviar(mensaje))


# Uso
sistema = SistemaNotificaciones()
sistema.agregar_notificador(EmailNotificador())
sistema.agregar_notificador(SMSNotificador())
sistema.agregar_notificador(PushNotificador())

sistema.notificar_todos("¡Nueva actualización disponible!")

# https://claude.ai/chat/05235721-c023-496d-996e-b937054ad35d
# chrome