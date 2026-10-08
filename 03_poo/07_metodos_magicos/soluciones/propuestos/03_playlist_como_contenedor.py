"""
Solución - Ejercicio propuesto 03 - Playlist como contenedor
"""

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self._canciones = []

    def agregar(self, cancion):
        self._canciones.append(cancion)

    def __len__(self):
        return len(self._canciones)

    def __getitem__(self, indice):
        # La lista ya sabe manejar índices negativos y slices.
        return self._canciones[indice]

    def __contains__(self, cancion):
        buscada = cancion.lower()
        return any(c.lower() == buscada for c in self._canciones)

    def __iter__(self):
        return iter(self._canciones)

    def __add__(self, otra):
        nueva = Playlist(f"{self.nombre} + {otra.nombre}")
        for cancion in [*self, *otra]:
            if cancion not in nueva:
                nueva.agregar(cancion)
        return nueva

    def __bool__(self):
        return len(self._canciones) > 0


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    rock = Playlist("Rock")
    assert not rock, "Una playlist vacía es False"
    for cancion in ("Bohemian Rhapsody", "Hotel California", "Imagine"):
        rock.agregar(cancion)

    assert len(rock) == 3
    assert rock[0] == "Bohemian Rhapsody"
    assert rock[-1] == "Imagine"
    assert rock[0:2] == ["Bohemian Rhapsody", "Hotel California"]
    assert "imagine" in rock
    assert "Yesterday" not in rock
    assert [c for c in rock] == ["Bohemian Rhapsody", "Hotel California", "Imagine"]
    assert rock

    pop = Playlist("Pop")
    pop.agregar("Imagine")
    pop.agregar("Thriller")
    mezcla = rock + pop
    assert mezcla.nombre == "Rock + Pop"
    assert list(mezcla) == ["Bohemian Rhapsody", "Hotel California", "Imagine", "Thriller"]
    assert len(rock) == 3, "La suma no debe modificar las originales"

    print("Todas las pruebas pasaron")
