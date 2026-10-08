"""
Ejercicio propuesto 03 - Atributos y métodos de clase
Nivel: intermedio

Hay datos que pertenecen a la CLASE (compartidos por todos los objetos) y
no a cada objeto.

Requisitos. Crea la clase Estudiante:
1. Atributo de clase total_creados = 0. Cada vez que se crea un
   estudiante, súmale 1 usando Estudiante.total_creados (no self).
2. Cada estudiante recibe un codigo automático "EST-001", "EST-002", ...
   a partir de total_creados.
3. __init__(self, nombre, nota).
4. @staticmethod es_nota_valida(nota): True si 0 <= nota <= 5. No usa self
   ni la clase: es una función que vive dentro de la clase.
5. @classmethod desde_texto(cls, texto): crea un estudiante a partir de un
   texto "Ana;4.5". Retorna cls(nombre, nota). Lanza ValueError si la nota
   no es válida.

Conceptos: atributos de clase, @staticmethod, @classmethod, constructores
alternativos.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Estudiante.total_creados = 0
    ana = Estudiante("Ana", 4.5)
    luis = Estudiante("Luis", 3.0)
    assert Estudiante.total_creados == 2
    assert ana.codigo == "EST-001"
    assert luis.codigo == "EST-002"

    assert Estudiante.es_nota_valida(5) is True
    assert Estudiante.es_nota_valida(5.1) is False

    eva = Estudiante.desde_texto("Eva;3.8")
    assert isinstance(eva, Estudiante)
    assert eva.nombre == "Eva" and eva.nota == 3.8
    assert eva.codigo == "EST-003"

    try:
        Estudiante.desde_texto("Pedro;9")
        raise AssertionError("Debe lanzar ValueError")
    except ValueError:
        pass

    print("Todas las pruebas pasaron")
