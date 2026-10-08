"""
Solución - Ejercicio propuesto 04 - Números primos
"""

def es_primo(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False  # ya hay un divisor: no hace falta seguir
    return True


def primos_hasta(limite):
    primos = []
    for n in range(2, limite + 1):
        if es_primo(n):
            primos.append(n)
    return primos


# ----------------------------------------------------------------------
# Pruebas
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
