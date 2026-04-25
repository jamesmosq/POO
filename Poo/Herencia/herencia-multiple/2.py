# 1. Dispositivo Multifuncional (Impresora/Scanner/Fax)
class Impresora:
    def imprimir(self):
        return "Imprimiendo documento..."

class Scanner:
    def escanear(self):
        return "Escaneando documento..."

class Fax:
    def enviar_fax(self):
        return "Enviando fax..."

class DispositivoMultifuncional(Impresora, Scanner, Fax):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def estado(self):
        return f"Dispositivo {self.marca} {self.modelo} listo"