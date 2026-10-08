"""
Ejercicio para corregir 03 - Compra con descuento
Nivel: básico
Errores a encontrar: 2

Qué debería hacer el programa:
    Un cliente compra 2 unidades de un producto de $15000. Se aplica un
    descuento del 10 %. El total con descuento debe ser 27000.

    El precio llega como texto porque viene de un formulario (así lo
    entregaría input()).

Ojo: uno de los errores no lanza ninguna excepción, solo da un resultado
incorrecto. Imprime las variables intermedias para ver dónde se tuerce el
cálculo.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

precio = "15000"
cantidad = 2

total = precio * cantidad
descuento = total * 10
total_con_descuento = total - descuento

print("Total con descuento:", total_con_descuento)


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert total == 30000, f"total vale {total!r}"
    assert total_con_descuento == 27000, f"total_con_descuento vale {total_con_descuento!r}"

    print("Todas las pruebas pasaron")
