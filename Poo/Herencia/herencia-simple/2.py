# Clase base abstracta
class Notificacion:
    def __init__(self, tipo_transaccion, monto, cuenta_origen, cuenta_destino, fecha):
        self.tipo_transaccion = tipo_transaccion
        self.monto = monto
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino
        self.fecha = fecha
        self.telefono_soporte = "018000931987"

    def enviar(self):
        # Método que será implementado por las clases hijas
        pass


# Implementaciones específicas
class NotificacionEmail(Notificacion):
    def __init__(self, tipo_transaccion, monto, cuenta_origen, cuenta_destino, fecha, correo):
        super().__init__(tipo_transaccion, monto, cuenta_origen, cuenta_destino, fecha)
        self.correo = correo

    def enviar(self):
        print("\n=== NOTIFICACIÓN POR CORREO ELECTRÓNICO ===")
        print(f"De: Alertas y Notificaciones <alertasynotificaciones@notificacionesbancolombia.com>")
        print(f"Para: {self.correo}")
        print(f"Fecha: {self.fecha}")
        print("\n[Logo de Bancolombia]")
        print("\n¡Listo!")
        print(f"Todo salió bien con tus movimientos")
        print(
            f"\nBancolombia: {self.tipo_transaccion} ${self.monto:,.2f} por QR desde tu cuenta {self.cuenta_origen} a la cuenta {self.cuenta_destino}, el")
        print(f"{self.fecha}. ¿Dudas? Llámanos al {self.telefono_soporte}. Estamos cerca.")
        print("================================================")


class NotificacionSMS(Notificacion):
    def __init__(self, tipo_transaccion, monto, cuenta_origen, cuenta_destino, fecha, telefono):
        super().__init__(tipo_transaccion, monto, cuenta_origen, cuenta_destino, fecha)
        self.telefono = telefono

    def enviar(self):
        print("\n=== NOTIFICACIÓN POR SMS ===")
        print(f"Para: {self.telefono}")
        print(f"Mensaje:")
        print(f"Bancolombia: {self.tipo_transaccion} ${self.monto:,.2f}")
        print(f"desde tu cuenta *{self.cuenta_origen} a la cuenta")
        print(f"*{self.cuenta_destino} el {self.fecha}.")
        print(f"¿Dudas? Llámanos al {self.telefono_soporte}.")
        print(f"Estamos cerca.")
        print(f"{self.fecha}")
        print("===========================")


class NotificacionApp(Notificacion):
    def __init__(self, tipo_transaccion, monto, cuenta_origen, cuenta_destino, fecha, moneda="COP"):
        super().__init__(tipo_transaccion, monto, cuenta_origen, cuenta_destino, fecha)
        self.moneda = moneda

    def enviar(self):
        # Formatear fecha para mostrar solo día y mes
        fecha_corta = ' '.join(self.fecha.split()[:2]).upper()
        operacion = "-" if "TRANSFERENCIA" in self.tipo_transaccion else ""

        print("\n=== NOTIFICACIÓN EN LA APP ===")
        print("Cuenta de Ahorros")
        print("       Detalles       Movimientos       Plan")
        print("                      -----------")
        print(f"{fecha_corta}")
        print(f"{self.tipo_transaccion}")
        print(f"{self.moneda} {operacion}${self.monto:,.2f}")
        print("===============================")


# Función que demuestra el polimorfismo
def notificar_cliente(notificaciones):
    print("SISTEMA DE NOTIFICACIONES BANCARIAS")
    print("-----------------------------------")
    for notificacion in notificaciones:
        notificacion.enviar()  # Mismo método, diferentes comportamientos


# Ejemplo de uso
if __name__ == "__main__":
    # Transacción 1 - Transferencia por QR (correo)
    email = NotificacionEmail(
        tipo_transaccion="Transferiste",
        monto=8800.00,
        cuenta_origen="4071",
        cuenta_destino="6692",
        fecha="2025/05/06 18:39",
        correo="cliente@ejemplo.com"
    )

    # Transacción 2 - Transferencia (SMS)
    sms = NotificacionSMS(
        tipo_transaccion="Transferiste",
        monto=450000.00,
        cuenta_origen="4071",
        cuenta_destino="3119304844",
        fecha="04/05/2025 a las 21:23",
        telefono="+573123456789"
    )

    # Transacción 3 - Transferencia (APP)
    app = NotificacionApp(
        tipo_transaccion="TRANSFERENCIA A CTA SUC VIRTUAL",
        monto=475000.00,
        cuenta_origen="",
        cuenta_destino="",
        fecha="14 MAY 2025"
    )

    # Enviar todas las notificaciones
    notificar_cliente([email, sms, app])

    # Segunda transacción en la app
    app2 = NotificacionApp(
        tipo_transaccion="TRANSFERENCIA A NEQUI",
        monto=12000.00,
        cuenta_origen="",
        cuenta_destino="",
        fecha="14 MAY 2025"
    )

    print("\nNotificación adicional:")
    app2.enviar()