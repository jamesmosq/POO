"""
4.	__add__: En la clase Dinero, definimos __add__ para permitir la suma de dos instancias de Dinero.
Esto nos permite usar el operador + de forma intuitiva con nuestros objetos personalizados.
"""


# 4. __add__
class Dinero:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def __add__(self, otro):
        return Dinero(self.cantidad + otro.cantidad)

    def __str__(self):
        return f"${self.cantidad:.2f}"


billetera1 = Dinero(50)
billetera2 = Dinero(30)
total = billetera1 + billetera2
print(f"Total en la billetera: {total}")  # Salida: Total en la billetera: $80.00