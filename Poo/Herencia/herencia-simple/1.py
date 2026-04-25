# Clase base abstracta
class Notificacion:
    def __init__(self, usuario, monto, comercio, fecha):
        self.usuario = usuario
        self.monto = monto
        self.comercio = comercio
        self.fecha = fecha

    def enviar(self):
        # Método que será implementado por las clases hijas
        pass


# Implementaciones específicas
class NotificacionEmail(Notificacion):
    def __init__(self, usuario, monto, comercio, fecha, correo):
        super().__init__(usuario, monto, comercio, fecha)
        self.correo = correo

    def enviar(self):
        print(f"CORREO ELECTRÓNICO para {self.correo}:")
        print(f"Asunto: Confirmación de pago - Banco XYZ")
        print(f"Estimado/a {self.usuario},")
        print(f"Le informamos que se ha realizado un cargo de ${self.monto} en {self.comercio} el día {self.fecha}.")
        print(f"Acceda a su banca en línea para más detalles.")
        print("----------------------------------")


class NotificacionSMS(Notificacion):
    def __init__(self, usuario, monto, comercio, fecha, telefono):
        super().__init__(usuario, monto, comercio, fecha)
        self.telefono = telefono

    def enviar(self):
        print(f"SMS para {self.telefono}:")
        print(f"Banco XYZ: Pago de ${self.monto} en {self.comercio} completado el {self.fecha}.")
        print("----------------------------------")


class NotificacionApp(Notificacion):
    def __init__(self, usuario, monto, comercio, fecha, id_dispositivo):
        super().__init__(usuario, monto, comercio, fecha)
        self.id_dispositivo = id_dispositivo

    def enviar(self):
        print(f"NOTIFICACIÓN PUSH para dispositivo {self.id_dispositivo}:")
        print(f"🔔 Banco XYZ - Nuevo movimiento")
        print(f"Pago de ${self.monto} realizado")
        print(f"Comercio: {self.comercio}")
        print("----------------------------------")


# Función que demuestra el polimorfismo
def notificar_cliente(notificaciones):
    for notificacion in notificaciones:
        notificacion.enviar()  # Mismo método, diferentes comportamientos


# Ejemplo de uso
if __name__ == "__main__":
    # Datos del pago
    pago_datos = {
        "usuario": "Ana García",
        "monto": 125.50,
        "comercio": "Supermercado El Ahorro",
        "fecha": "15/05/2025"
    }

    # Crear diferentes tipos de notificaciones para el mismo pago
    email = NotificacionEmail(**pago_datos, correo="ana.garcia@ejemplo.com")
    sms = NotificacionSMS(**pago_datos, telefono="+34612345678")
    app = NotificacionApp(**pago_datos, id_dispositivo="SAMSUNG-G21-XYZ")

    # Enviar todas las notificaciones
    print("Enviando notificaciones de pago por diferentes canales:")
    notificar_cliente([email, sms, app])


    # https://claude.ai/chat/5f177ce5-b3b6-4c5e-94e3-5b9515ea9fca