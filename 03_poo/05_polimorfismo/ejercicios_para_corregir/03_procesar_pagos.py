"""
Ejercicio para corregir 03 - Procesar pagos
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    Todos los medios de pago tienen el método cobrar(monto), que retorna
    el valor final a cobrar (un número). total_cobrado(pagos) los suma.

        Efectivo().cobrar(1000)  -> 1000
        Tarjeta().cobrar(1000)   -> 1030   (3 % de comisión)
        Nequi().cobrar(1000)     -> 1000

Pista: para que el polimorfismo funcione, todas las clases deben ofrecer el
método con la misma "forma": el mismo nombre, los mismos parámetros y el
mismo tipo de resultado.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""


class Efectivo:
    def cobrar(self, monto):
        return monto


class Tarjeta:
    def cobrar(self):
        return self.monto * 1.03


class Nequi:
    def cobrar(self, monto):
        return f"${monto}"


def total_cobrado(pagos):
    return sum(medio.cobrar(monto) for medio, monto in pagos)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    pagos = [(Efectivo(), 1000), (Tarjeta(), 1000), (Nequi(), 1000)]
    assert round(total_cobrado(pagos), 2) == 3030

    print("Todas las pruebas pasaron")
