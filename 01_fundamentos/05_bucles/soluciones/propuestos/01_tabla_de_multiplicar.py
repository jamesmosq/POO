"""
Solución - Ejercicio propuesto 01 - Tabla de multiplicar
"""

def tabla(numero, hasta=10):
    resultado = []
    for i in range(1, hasta + 1):  # range no incluye el final, por eso + 1
        resultado.append(f"{numero} x {i} = {numero * i}")
    return resultado


for linea in tabla(7):
    print(linea)


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert tabla(3, 4) == ["3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9", "3 x 4 = 12"]
    assert len(tabla(5)) == 10
    assert tabla(5)[-1] == "5 x 10 = 50"
    assert tabla(2, 0) == []

    print("Todas las pruebas pasaron")
