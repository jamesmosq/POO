"""
Solución - Ejercicio propuesto 03 - Atributos y métodos de clase
"""

class Estudiante:
    total_creados = 0

    def __init__(self, nombre, nota):
        # Se usa el nombre de la clase: con self.total_creados += 1 se
        # crearía un atributo nuevo en el objeto y el de la clase no cambiaría.
        Estudiante.total_creados += 1
        self.codigo = f"EST-{Estudiante.total_creados:03d}"
        self.nombre = nombre
        self.nota = nota

    @staticmethod
    def es_nota_valida(nota):
        return 0 <= nota <= 5

    @classmethod
    def desde_texto(cls, texto):
        nombre, nota = texto.split(";")
        nota = float(nota)
        if not cls.es_nota_valida(nota):
            raise ValueError(f"Nota inválida: {nota}")
        return cls(nombre, nota)


# ----------------------------------------------------------------------
# Pruebas
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
