"""
Ejercicio para corregir 03 - Usar un módulo propio
Nivel: intermedio
Errores a encontrar: 2 (repartidos entre este archivo e impuestos.py)

Qué debería hacer el programa:
    Este archivo usa el módulo impuestos.py, que está en la misma carpeta,
    para calcular el total de una compra con IVA (19 %).

        total_con_iva(1000) -> 1190.0

    Importar el módulo no debe imprimir nada ni cambiar sus datos.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Revisa también impuestos.py: parte del problema está allá.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
from impuestos import calcular_iva


def total_con_iva(valor):
    return valor + calcular_iva(valor)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import impuestos

    assert impuestos.TASAS == {"iva": 19, "consumo": 8}, f"Las tasas cambiaron al importar: {impuestos.TASAS}"
    assert total_con_iva(1000) == 1190.0, total_con_iva(1000)

    print("Todas las pruebas pasaron")
