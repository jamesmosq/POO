"""
Solución - Ejercicio para corregir 04 - Paquete banco

Las tres correcciones están en la carpeta banco/ de esta misma carpeta.

CORRECCIÓN 1 (ModuleNotFoundError: No module named 'utilidades'), en
banco/cuentas.py: dentro de un paquete, "from utilidades import ..." busca
un módulo utilidades fuera del paquete. Para el módulo vecino se usa la
importación relativa: "from .utilidades import ...".

CORRECCIÓN 2 (ImportError: cannot import name 'Cuenta'), en
banco/__init__.py: la clase se llama CuentaBancaria.

CORRECCIÓN 3 (formato sin separador de miles), en banco/utilidades.py: el
formato :.2f solo pone dos decimales; :,.2f agrega además la coma de miles.
"""

from banco import CuentaBancaria


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from banco.utilidades import formatear_moneda

    assert formatear_moneda(1234.5) == "$1,234.50", formatear_moneda(1234.5)

    cuenta = CuentaBancaria("Ana", 1500)
    cuenta.depositar(250000)
    assert cuenta.resumen() == "Ana: $251,500.00", cuenta.resumen()

    print("Todas las pruebas pasaron")
