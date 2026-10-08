"""
Solución - Ejercicio propuesto 03 - Diamante con super()
"""

class Etapa:
    ejecuciones = 0

    def procesar(self, registro):
        Etapa.ejecuciones += 1
        registro.append("Etapa")


class Validacion(Etapa):
    def procesar(self, registro):
        registro.append("Validacion")
        super().procesar(registro)


class Facturacion(Etapa):
    def procesar(self, registro):
        registro.append("Facturacion")
        super().procesar(registro)


class ProcesoCompleto(Validacion, Facturacion):
    def procesar(self, registro):
        registro.append("ProcesoCompleto")
        super().procesar(registro)


# Respuesta a la pregunta:
# super() lleva a la SIGUIENTE clase del MRO del objeto real. Con un
# ProcesoCompleto el MRO es ProcesoCompleto, Validacion, Facturacion,
# Etapa; dentro de Validacion, super() lleva a Facturacion (que no es su
# padre). Con una Validacion sola, el MRO es Validacion, Etapa, y super()
# lleva a Etapa.


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Etapa.ejecuciones = 0
    registro = []
    ProcesoCompleto().procesar(registro)
    assert registro == ["ProcesoCompleto", "Validacion", "Facturacion", "Etapa"], registro
    assert Etapa.ejecuciones == 1, f"Etapa se ejecutó {Etapa.ejecuciones} veces"

    solo = []
    Validacion().procesar(solo)
    assert solo == ["Validacion", "Etapa"]

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    for nombre in ("Etapa", "Validacion", "Facturacion"):
        assert f"{nombre}.procesar(self" not in fuente, f"No llames a {nombre}.procesar por su nombre: usa super()"

    print("Todas las pruebas pasaron")
