"""
Ejercicio para corregir 04 - Paquete banco
Nivel: intermedio
Errores a encontrar: 3 (todos dentro de la carpeta banco/)

Qué debería hacer el programa:
    El paquete banco/ tiene tres archivos:
        __init__.py    expone la clase CuentaBancaria
        cuentas.py     define CuentaBancaria
        utilidades.py  define formatear_moneda

    Este archivo lo usa así:
        from banco import CuentaBancaria
        cuenta = CuentaBancaria("Ana", 1500)
        cuenta.depositar(250000)
        cuenta.resumen()  ->  "Ana: $251,500.00"

Pista: dentro de un paquete, para importar un módulo vecino se usa la
importación relativa (con punto).

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo. Fíjate en qué
       archivo y en qué línea ocurre.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from banco import CuentaBancaria


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from banco.utilidades import formatear_moneda

    assert formatear_moneda(1234.5) == "$1,234.50", formatear_moneda(1234.5)

    cuenta = CuentaBancaria("Ana", 1500)
    cuenta.depositar(250000)
    assert cuenta.resumen() == "Ana: $251,500.00", cuenta.resumen()

    print("Todas las pruebas pasaron")
