"""
Ejercicio para corregir 03 - Contador de visitas
Nivel: intermedio
Errores a encontrar: 2

Qué debería hacer el programa:
    - registrar_visita() suma 1 a la variable global visitas y retorna el
      nuevo valor.
    - mensaje_de_bienvenida() retorna "Bienvenido, eres la visita número N".
    - El programa registra 3 visitas y guarda el mensaje final en mensaje.

        mensaje -> "Bienvenido, eres la visita número 3"

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""

visitas = 0


def registrar_visita():
    visitas = visitas + 1
    return visitas


def mensaje_de_bienvenida():
    return f"Bienvenido, eres la visita número {visitas}"


registrar_visita()
registrar_visita()
registrar_visita()
mensaje = mensaje_de_bienvenida


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert visitas == 3, f"visitas vale {visitas}"
    assert mensaje == "Bienvenido, eres la visita número 3", f"mensaje vale {mensaje!r}"

    print("Todas las pruebas pasaron")
