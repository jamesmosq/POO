"""
5.	__getitem__: En la clase Semana, __getitem__ nos permite acceder a los días de la semana usando índices,
como si fuera una lista. Esto hace que nuestra clase sea indexable.
"""


# 5. __getitem__
class Semana:
    def __init__(self):
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def __getitem__(self, indice):
        return self.dias[indice]


mi_semana = Semana()
print(f"El tercer día de la semana es: {mi_semana[6]}")  # Salida: El tercer día de la semana es: Miércoles