class MiLista:
    def __init__(self, items):
        self.items = items

    def __repr__(self):
        return f"MiLista({self.items})"

    def __eq__(self, other):
        if isinstance(other, MiLista):
            return self.items == other.items
        return False

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __add__(self, other):
        if isinstance(other, MiLista):
            return MiLista(self.items + other.items)
        return NotImplemented

    def __str__(self):
        return f"MiLista: {', '.join(map(str, self.items))}"

    def __len__(self):
        return len(self.items)

# Uso de la clase
lista1 = MiLista([1, 2, 3])
lista2 = MiLista([4, 5, 6])

print(repr(lista1))  # __repr__
print(lista1 == lista2)  # __eq__
print(lista1[1])  # __getitem__
lista1[1] = 10  # __setitem__
del lista1[0]  # __delitem__
print(lista1 + lista2)  # __add__
print(str(lista1))  # __str__
print(len(lista1))  # __len__