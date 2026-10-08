"""
Ejercicio propuesto 02 - Leer el MRO
Nivel: básico

Las clases de abajo ya están escritas y forman un diamante. Tu trabajo es
escribir dos funciones que expliquen cómo busca Python un método.

Requisitos:
1. orden(clase): retorna la lista con los NOMBRES de las clases del MRO,
   sin incluir object.
       orden(D) -> ["D", "B", "C", "A"]
2. definido_en(clase, metodo): retorna el nombre de la clase de la que
   Python tomará ese método, recorriendo el MRO y revisando el __dict__ de
   cada clase. Si ninguna lo define, retorna None.
       definido_en(D, "saludar") -> "B"
3. Antes de ejecutar las pruebas, escribe en un comentario qué crees que
   retornarán definido_en(D, "despedir") y definido_en(D, "presentar"), y
   después compara.

Conceptos: MRO, mro(), __mro__, __dict__, búsqueda de métodos.
"""


class A:
    def saludar(self):
        return "Hola desde A"

    def presentar(self):
        return "Soy A"


class B(A):
    def saludar(self):
        return "Hola desde B"


class C(A):
    def saludar(self):
        return "Hola desde C"

    def despedir(self):
        return "Adiós desde C"


class D(B, C):
    pass

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert orden(D) == ["D", "B", "C", "A"]
    assert orden(B) == ["B", "A"]

    assert definido_en(D, "saludar") == "B"
    assert definido_en(D, "despedir") == "C", "B no lo tiene, así que Python sigue con C (no con A)"
    assert definido_en(D, "presentar") == "A"
    assert definido_en(D, "volar") is None

    # Lo que retorna el objeto coincide con el método de la clase indicada.
    clases = {"A": A, "B": B, "C": C, "D": D}
    d = D()
    for metodo in ("saludar", "despedir", "presentar"):
        origen = clases[definido_en(D, metodo)]
        assert getattr(d, metodo)() == getattr(origen, metodo)(d)

    print("Todas las pruebas pasaron")
