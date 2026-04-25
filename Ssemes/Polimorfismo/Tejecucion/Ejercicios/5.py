# Ejercicio 5: Reproductor multimedia

class AudioPlayer:
    def reproducir(self):
        return "Reproduciendo audio"


class VideoPlayer:
    def reproducir(self):
        return "Reproduciendo video"


class Imagen:
    def reproducir(self):
        return "Mostrando imagen"


def mostrar_contenido(media):
    print(media.reproducir())


# Uso:
audio = AudioPlayer()
video = VideoPlayer()
imagen = Imagen()

mostrar_contenido(audio)
mostrar_contenido(video)
mostrar_contenido(imagen)