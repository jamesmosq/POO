"""
Ejercicio propuesto 03 - Playlist como contenedor
Nivel: intermedio

Con los métodos mágicos adecuados, un objeto se comporta como una lista:
    len(playlist)          -> __len__
    playlist[0]            -> __getitem__
    "canción" in playlist  -> __contains__
    for c in playlist      -> __iter__

Requisitos. Crea la clase Playlist(nombre):
1. agregar(cancion): agrega un texto a la lista interna.
2. __len__, __getitem__ (acepta índices y también slicing: playlist[0:2]),
   __contains__ (sin importar mayúsculas) y __iter__.
3. __add__(otra): une dos playlists en una NUEVA, con nombre
   "Rock + Pop", sin canciones repetidas (respetando el orden).
4. __bool__: una playlist vacía se considera False.

Conceptos: protocolo de contenedores, iteración, valor de verdad.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
