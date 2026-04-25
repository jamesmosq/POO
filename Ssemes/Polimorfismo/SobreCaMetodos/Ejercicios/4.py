# Ejercicio 4: Conversor de unidades

class Conversor:
    def convertir(self, valor, unidad_origen=None, unidad_destino=None):
        if unidad_origen == "km" and unidad_destino == "mi":
            return valor * 0.621371
        elif unidad_origen == "mi" and unidad_destino == "km":
            return valor * 1.60934
        elif unidad_origen is None and unidad_destino is None:
            return valor  # No conversion
        else:
            raise ValueError("Conversión no soportada")

# Uso:
conv = Conversor()
print(conv.convertir(10))                    # 10
print(conv.convertir(10, "km", "mi"))        # 6.21371
print(conv.convertir(10, "mi", "km"))        # 16.0934

