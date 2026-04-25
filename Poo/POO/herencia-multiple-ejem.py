# 1. Dispositivos Electrónicos
class Dispositivo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        return "Dispositivo encendido"


class Conexion:
    def conectar_wifi(self):
        return "Conectado a WiFi"


class Bateria:
    def __init__(self):
        self.nivel = 100

    def mostrar_bateria(self):
        return f"Nivel de batería: {self.nivel}%"


class Smartphone(Dispositivo, Conexion, Bateria):
    def __init__(self, marca, modelo):
        Dispositivo.__init__(self, marca)
        Bateria.__init__(self)
        self.modelo = modelo

    def info_completa(self):
        return f"{self.marca} {self.modelo} - {self.mostrar_bateria()}"


# 2. Sistema de Notificaciones
class EmailSender:
    def enviar_email(self, mensaje):
        return f"Email enviado: {mensaje}"


class SMSSender:
    def enviar_sms(self, mensaje):
        return f"SMS enviado: {mensaje}"


class PushNotification:
    def enviar_push(self, mensaje):
        return f"Notificación push enviada: {mensaje}"


class SistemaNotificaciones(EmailSender, SMSSender, PushNotification):
    def notificar_todos(self, mensaje):
        return [
            self.enviar_email(mensaje),
            self.enviar_sms(mensaje),
            self.enviar_push(mensaje)
        ]


# 3. Personajes de Videojuegos
class Guerrero:
    def atacar(self):
        return "Ataque con espada"


class Mago:
    def lanzar_hechizo(self):
        return "Lanzar bola de fuego"


class Curandero:
    def curar(self):
        return "Curación"


class PersonajeHibrido(Guerrero, Mago, Curandero):
    def __init__(self, nombre):
        self.nombre = nombre

    def usar_habilidad_especial(self):
        return f"{self.atacar()} + {self.lanzar_hechizo()}"


# 4. Sistema de Archivos
class Readable:
    def leer(self):
        return "Leyendo archivo"


class Writable:
    def escribir(self, datos):
        return f"Escribiendo datos: {datos}"


class Executable:
    def ejecutar(self):
        return "Ejecutando archivo"


class ArchivoPrograma(Readable, Writable, Executable):
    def __init__(self, nombre):
        self.nombre = nombre

    def info(self):
        return f"Archivo: {self.nombre}"


# 5. Vehículos Híbridos
class Motor:
    def encender_motor(self):
        return "Motor encendido"


class MotorElectrico:
    def activar_bateria(self):
        return "Batería activada"


class SistemaHibridoControl:
    def cambiar_modo(self, modo):
        return f"Cambiando a modo {modo}"


class AutoHibrido(Motor, MotorElectrico, SistemaHibridoControl):
    def iniciar_sistema(self):
        return [
            self.encender_motor(),
            self.activar_bateria(),
            self.cambiar_modo("híbrido")
        ]


# 6. Interfaces de Usuario
class Clickeable:
    def click(self):
        return "Elemento clickeado"


class Arrastrable:
    def arrastrar(self):
        return "Elemento arrastrado"


class Redimensionable:
    def redimensionar(self, tamaño):
        return f"Redimensionando a {tamaño}"


class ComponenteUI(Clickeable, Arrastrable, Redimensionable):
    def __init__(self, tipo):
        self.tipo = tipo

    def interactuar(self):
        return f"Componente {self.tipo} interactivo"


# 7. Sistema de Logs
class ConsoleLogger:
    def log_to_console(self, mensaje):
        return f"Console: {mensaje}"


class FileLogger:
    def log_to_file(self, mensaje):
        return f"File: {mensaje}"


class DatabaseLogger:
    def log_to_db(self, mensaje):
        return f"DB: {mensaje}"


class SistemaLog(ConsoleLogger, FileLogger, DatabaseLogger):
    def log_all(self, mensaje):
        return [
            self.log_to_console(mensaje),
            self.log_to_file(mensaje),
            self.log_to_db(mensaje)
        ]


# 8. Empleado Multifuncional
class Vendedor:
    def vender(self):
        return "Realizando venta"


class Administrador:
    def administrar(self):
        return "Administrando recursos"


class Tecnico:
    def reparar(self):
        return "Reparando equipo"


class EmpleadoMultifuncional(Vendedor, Administrador, Tecnico):
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar_todas_tareas(self):
        return [self.vender(), self.administrar(), self.reparar()]


# 9. Sistema Multimedia
class Reproductor:
    def reproducir(self, archivo):
        return f"Reproduciendo {archivo}"


class Grabador:
    def grabar(self):
        return "Grabando contenido"


class Editor:
    def editar(self, archivo):
        return f"Editando {archivo}"


class SistemaMultimedia(Reproductor, Grabador, Editor):
    def __init__(self, nombre_app):
        self.nombre_app = nombre_app

    def procesar_medio(self, archivo):
        return [
            self.reproducir(archivo),
            self.grabar(),
            self.editar(archivo)
        ]


# 10. Sistema de Pagos
class PagoTarjeta:
    def pagar_tarjeta(self, monto):
        return f"Pago con tarjeta: ${monto}"


class PagoPayPal:
    def pagar_paypal(self, monto):
        return f"Pago con PayPal: ${monto}"


class PagoCripto:
    def pagar_cripto(self, monto):
        return f"Pago con criptomoneda: ${monto}"


class PasarelaPago(PagoTarjeta, PagoPayPal, PagoCripto):
    def procesar_pago(self, metodo, monto):
        if metodo == "tarjeta":
            return self.pagar_tarjeta(monto)
        elif metodo == "paypal":
            return self.pagar_paypal(monto)
        elif metodo == "cripto":
            return self.pagar_cripto(monto)