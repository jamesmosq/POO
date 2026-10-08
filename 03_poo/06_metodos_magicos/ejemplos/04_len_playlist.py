"""
3.	__len__: Para la Playlist, __len__ nos permite usar la función len() para obtener el número de canciones en la lista.
Esto hace que nuestra clase se comporte de manera similar a las listas incorporadas de Python.

"""


# 3. __len__
class Playlist:
    def __init__(self, canciones):
        self.canciones = canciones

    def __len__(self):
        return len(self.canciones)


mi_playlist = Playlist(["Canción 1", "Canción 2", "Canción 3","la falla fue tuya"])
print(f"La playlist tiene {len(mi_playlist)} canciones")

#esta sonando la cancion
mi_playlist.canciones[3]
print(f"Esta sonando {mi_playlist.canciones[3]}")