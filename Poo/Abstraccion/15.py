from abc import ABC, abstractmethod
class ProductoTienda(ABC):
    def __init__(self,codigo,nombre,precio,stock,categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    @abstractmethod
    def calcularprecioFinal(self):
        pass
    @abstractmethod
    def VefificarDisponibilidad(self):
        pass
    @abstractmethod
    def AplicarDescuento(self):
        pass

    def MostrarInformacion(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria} el descuento es: {self.AplicarDescuento(0)}"

class ProductoElectronico(ProductoTienda):
    def calcularprecioFinal(self):
        return self.precio * 1.19

    def VefificarDisponibilidad(self):
        return self.stock > 0


    def AplicarDescuento(self,porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        return f"Nuevo precio con descuento: {self.precio}"

p1 = ProductoElectronico("E001", "Smartphone", 300, 1, "Electrónica")
print(p1.MostrarInformacion())
print(f"Precio final: {p1.calcularprecioFinal()}")
print(f"Disponibilidad: {'Disponible' if p1.VefificarDisponibilidad() else 'No disponible'}")