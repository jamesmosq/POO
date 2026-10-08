"""
Ejercicio propuesto 03 - Empleado con validaciones
Nivel: intermedio

Requisitos. Crea la clase Empleado(nombre, salario, email) con tres
propiedades validadas. Todas lanzan ValueError con un mensaje claro:
1. nombre: no puede quedar vacío. Se guarda sin espacios al inicio y al
   final y con mayúscula inicial en cada palabra ("  ana  pérez" ->
   "Ana Pérez"). Pista: " ".join(texto.split()).title()
2. salario: no puede ser menor que SALARIO_MINIMO (atributo de clase
   SALARIO_MINIMO = 1_423_500).
3. email: debe contener exactamente una "@" y al menos un "." después de
   ella. Se guarda en minúscula.

Además:
4. aumentar_salario(porcentaje): aumenta el salario usando la propiedad
   (para que pase por la validación).

Conceptos: propiedades con validación, normalizar datos, constantes de
clase.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
def lanza_value_error(funcion):
    try:
        funcion()
    except ValueError:
        return True
    return False


if __name__ == "__main__":
    e = Empleado("  ana  pérez ", 2_000_000, "Ana.Perez@Empresa.com")
    assert e.nombre == "Ana Pérez"
    assert e.email == "ana.perez@empresa.com"

    e.aumentar_salario(10)
    assert e.salario == 2_200_000

    assert lanza_value_error(lambda: Empleado("", 2_000_000, "a@b.co"))
    assert lanza_value_error(lambda: Empleado("Luis", 1_000_000, "a@b.co"))
    assert lanza_value_error(lambda: Empleado("Luis", 2_000_000, "sin-arroba.com"))
    assert lanza_value_error(lambda: Empleado("Luis", 2_000_000, "a@@b.com"))
    assert lanza_value_error(lambda: Empleado("Luis", 2_000_000, "a@sinpunto"))

    def asignar_salario_bajo():
        e.salario = 100
    assert lanza_value_error(asignar_salario_bajo)
    assert e.salario == 2_200_000

    print("Todas las pruebas pasaron")
