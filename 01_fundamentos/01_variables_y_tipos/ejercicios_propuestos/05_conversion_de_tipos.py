"""
Ejercicio propuesto 05 - Conversión de tipos
Nivel: intermedio

input() siempre entrega texto, aunque el usuario escriba un número. Aquí
simulamos esos datos con variables de tipo str.

Requisitos:
1. Convierte los textos a números:
       edad      -> int a partir de texto_edad
       precio    -> float a partir de texto_precio
       cantidad  -> int a partir de texto_cantidad
2. Calcula total = precio * cantidad.
3. Calcula es_mayor_de_edad (bool): True si edad es 18 o más.
4. Crea mensaje con el formato "Total: 7501.5"  (convierte total a str o
   usa un f-string).

Pregunta para pensar (respóndela en un comentario): ¿qué pasaría si
calcularas texto_precio * 3 sin convertir? ¿Y texto_precio + 3?

Conceptos: str, int, float, bool, conversión de tipos.
"""

texto_edad = "17"
texto_precio = "2500.50"
texto_cantidad = "3"

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert edad == 17 and type(edad) is int
    assert precio == 2500.5 and type(precio) is float
    assert cantidad == 3 and type(cantidad) is int
    assert total == 7501.5, f"total vale {total!r}"
    assert es_mayor_de_edad is False
    assert mensaje == "Total: 7501.5", mensaje

    print("Todas las pruebas pasaron")
