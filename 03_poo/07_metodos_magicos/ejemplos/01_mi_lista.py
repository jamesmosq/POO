class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __str__(self):
        return f"MiLista: {self.elementos}"

    def __len__(self):
        return len(self.elementos)

    def __add__(self, otra_lista):
        return MiLista(self.elementos + otra_lista.elementos)

    def __getitem__(self, indice):
        return self.elementos[indice]

# Uso de la clase
lista1 = MiLista([1, 2, 3])
lista2 = MiLista([4, 5, 6])

print(lista1)  # Salida: MiLista: [1, 2, 3]
print(len(lista1))  # Salida: 3
lista3 = lista1 + lista2
print(lista3)  # Salida: MiLista: [1, 2, 3, 4, 5, 6]
print(lista1[1])  # Salida: 2