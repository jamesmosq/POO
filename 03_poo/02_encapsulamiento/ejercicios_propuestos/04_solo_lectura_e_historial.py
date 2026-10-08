"""
Ejercicio propuesto 04 - Atributos de solo lectura e historial
Nivel: intermedio

Una propiedad sin setter es de solo lectura: si alguien intenta asignarla,
Python lanza AttributeError.

Otro problema de encapsulamiento: si un método retorna una lista interna,
quien la reciba puede modificarla sin pasar por las validaciones. Por eso
se retorna una copia o una tupla.

Requisitos. Crea la clase Producto(codigo, precio):
1. codigo: propiedad de SOLO LECTURA.
2. precio: propiedad con setter que valida que sea mayor que 0. Cada vez
   que el precio cambia, el precio anterior se guarda en un historial
   interno (self._historial).
3. historial_de_precios: propiedad que retorna una TUPLA con los precios
   anteriores, del más antiguo al más reciente.

Conceptos: solo lectura, proteger colecciones internas, tuplas.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    p = Producto("CAF-01", 10000)
    assert p.codigo == "CAF-01"

    try:
        p.codigo = "OTRO"
        raise AssertionError("codigo debe ser de solo lectura")
    except AttributeError:
        pass

    p.precio = 12000
    p.precio = 11500
    assert p.precio == 11500
    assert p.historial_de_precios == (10000, 12000)

    historial = p.historial_de_precios
    try:
        historial.append(1)
        raise AssertionError("El historial no debe poder modificarse desde afuera")
    except AttributeError:
        pass

    try:
        p.precio = 0
        raise AssertionError("Debe lanzar ValueError")
    except ValueError:
        pass
    assert p.historial_de_precios == (10000, 12000), "Un precio inválido no entra al historial"

    print("Todas las pruebas pasaron")
