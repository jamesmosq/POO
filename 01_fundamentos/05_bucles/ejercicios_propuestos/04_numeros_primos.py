"""
Ejercicio propuesto 04 - Números primos
Nivel: intermedio

Un número primo es mayor que 1 y solo es divisible entre 1 y entre sí
mismo. Ejemplos: 2, 3, 5, 7, 11, 13.

Requisitos:
1. es_primo(n): retorna True si n es primo.
   - Recorre los posibles divisores con un for.
   - En cuanto encuentres un divisor, ya sabes la respuesta: no sigas
     buscando (usa return o break).
   - Optimización opcional: basta con probar divisores hasta la raíz
     cuadrada de n (int(n ** 0.5) + 1).
2. primos_hasta(limite): retorna una lista con todos los primos desde 2
   hasta limite (incluido). Reutiliza es_primo.

Conceptos: for, salida anticipada, ciclos que llaman funciones.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    for n in [2, 3, 5, 7, 11, 13, 97]:
        assert es_primo(n) is True, f"{n} es primo"
    for n in [-7, 0, 1, 4, 9, 15, 100]:
        assert es_primo(n) is False, f"{n} no es primo"

    assert primos_hasta(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert primos_hasta(1) == []
    assert len(primos_hasta(1000)) == 168

    print("Todas las pruebas pasaron")
