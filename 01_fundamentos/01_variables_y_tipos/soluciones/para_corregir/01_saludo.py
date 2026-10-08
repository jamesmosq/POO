"""
Solución - Ejercicio para corregir 01 - Saludo

CORRECCIÓN 1 (SyntaxError: invalid decimal literal): un nombre de variable
no puede empezar con un número. Se cambia 1er_nombre por primer_nombre.
Reglas: letras, números y guion bajo; nunca empezar con número; sin espacios.

CORRECCIÓN 2 (TypeError: can only concatenate str (not "int") to str):
con + solo se pueden unir textos. La edad es un int y hay que convertirla
con str(edad), o mejor usar un f-string, que convierte solo.
"""

primer_nombre = "Ana"  # CORRECCIÓN 1
edad = 20

mensaje = f"{primer_nombre} tiene {edad} años"  # CORRECCIÓN 2
print(mensaje)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert edad == 20
    assert mensaje == "Ana tiene 20 años", mensaje

    print("Todas las pruebas pasaron")
