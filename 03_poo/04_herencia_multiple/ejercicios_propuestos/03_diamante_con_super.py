"""
Ejercicio propuesto 03 - Diamante con super()
Nivel: intermedio

Un sistema procesa pedidos en varias etapas. Cada etapa es una clase y se
combinan con herencia múltiple en forma de diamante:

                 Etapa
                /     \\
        Validacion   Facturacion
                \\     /
            ProcesoCompleto

Requisitos:
1. Etapa: procesar(self, registro) agrega "Etapa" a la lista registro.
   Tiene además el atributo de clase ejecuciones = 0, que suma 1 cada vez
   que se ejecuta Etapa.procesar.
2. Validacion y Facturacion (hijas de Etapa): procesar agrega su nombre
   ("Validacion" / "Facturacion") y luego llama a super().procesar(registro).
3. ProcesoCompleto(Validacion, Facturacion): procesar agrega
   "ProcesoCompleto" y llama a super().procesar(registro).
4. No llames a ningún padre por su nombre: usa siempre super().

Resultado esperado:
    registro = []
    ProcesoCompleto().procesar(registro)
    registro -> ["ProcesoCompleto", "Validacion", "Facturacion", "Etapa"]
    Etapa.ejecuciones -> 1

Pregunta para pensar (respóndela en un comentario): dentro de Validacion,
¿a qué clase lleva super() cuando el objeto es un ProcesoCompleto? ¿Y
cuando el objeto es una Validacion sola?

Conceptos: problema del diamante, super() y MRO.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
