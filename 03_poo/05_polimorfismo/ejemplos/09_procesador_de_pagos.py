# Ejercicio 4: Procesador de pagos

class PayPal:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} con PayPal"


class Stripe:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} con Stripe"


class CreditCard:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} con tarjeta de crédito"


def realizar_pago(procesador, cantidad):
    print(procesador.procesar_pago(cantidad))


# Uso:
paypal = PayPal()
stripe = Stripe()
credit_card = CreditCard()

realizar_pago(paypal, 100)
realizar_pago(stripe, 200)
realizar_pago(credit_card, 150)


