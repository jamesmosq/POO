# Ejercicio 3: Sistema de notificaciones

class EmailNotifier:
    def enviar(self, mensaje):
        return f"Enviando email: {mensaje}"


class SMSNotifier:
    def enviar(self, mensaje):
        return f"Enviando SMS: {mensaje}"


class PushNotifier:
    def enviar(self, mensaje):
        return f"Enviando notificación push: {mensaje}"


def notificar(notificador, mensaje):
    print(notificador.enviar(mensaje))


# Uso:
email = EmailNotifier()
sms = SMSNotifier()
push = PushNotifier()

notificar(email, "Hola mundo")
notificar(sms, "Hola mundo")
notificar(push, "Hola mundo")


