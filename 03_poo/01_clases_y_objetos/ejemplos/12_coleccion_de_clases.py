# 1. Clase Estudiante - Gestión de datos académicos
class Estudiante:
    def __init__(self, nombre, edad, numero_estudiante):
        self.nombre = nombre
        self.edad = edad
        self.numero_estudiante = numero_estudiante
        self.calificaciones = {}
        self.asistencias = 0
    
    def agregar_calificacion(self, asignatura, nota):
        if 0 <= nota <= 10:
            self.calificaciones[asignatura] = nota
            return True
        return False
    
    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)
    
    def registrar_asistencia(self):
        self.asistencias += 1
    
    def obtener_info(self):
        return f"Estudiante: {self.nombre}\nEdad: {self.edad}\nPromedio: {self.calcular_promedio():.2f}"

# 2. Clase CuentaBancaria - Gestión de cuenta bancaria
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado
        self.movimientos = []
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            self.movimientos.append(f"Depósito: +{cantidad}")
            return True
        return False
    
    def retirar(self, cantidad):
        if cantidad > 0 and self.__saldo >= cantidad:
            self.__saldo -= cantidad
            self.movimientos.append(f"Retiro: -{cantidad}")
            return True
        return False
    
    def consultar_saldo(self):
        return self.__saldo
    
    def obtener_movimientos(self):
        return self.movimientos

# 3. Clase Libro - Gestión de biblioteca
class Libro:
    def __init__(self, titulo, autor, isbn, copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.copias_disponibles = copias_disponibles
        self.prestados = []
    
    def prestar(self, usuario):
        if self.copias_disponibles > 0:
            self.copias_disponibles -= 1
            self.prestados.append(usuario)
            return True
        return False
    
    def devolver(self, usuario):
        if usuario in self.prestados:
            self.prestados.remove(usuario)
            self.copias_disponibles += 1
            return True
        return False
    
    @property
    def disponible(self):
        return self.copias_disponibles > 0

# 4. Clase Producto - Gestión de inventario
class Producto:
    contador_productos = 0  # Variable de clase
    
    def __init__(self, nombre, precio, stock):
        Producto.contador_productos += 1
        self.id = Producto.contador_productos
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def actualizar_stock(self, cantidad):
        nuevo_stock = self.stock + cantidad
        if nuevo_stock >= 0:
            self.stock = nuevo_stock
            return True
        return False
    
    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            self.precio = self.precio * (1 - porcentaje/100)
            return True
        return False
    
    @classmethod
    def obtener_total_productos(cls):
        return cls.contador_productos

# 5. Clase Vehiculo - Gestión de vehículos
class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.encendido = False
        self.mantenimientos = []
    
    def encender(self):
        if not self.encendido:
            self.encendido = True
            return "Vehículo encendido"
        return "El vehículo ya está encendido"
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            return "Vehículo apagado"
        return "El vehículo ya está apagado"
    
    def agregar_kilometraje(self, km):
        if km > 0:
            self.kilometraje += km
            return True
        return False
    
    def registrar_mantenimiento(self, descripcion, fecha):
        self.mantenimientos.append({
            "fecha": fecha,
            "descripcion": descripcion
        })

# 6. Clase Empleado - Gestión de personal
class Empleado:
    def __init__(self, nombre, id_empleado, salario_base):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base
        self.horas_extra = 0
        self.bonos = 0
    
    def registrar_horas_extra(self, horas):
        if horas >= 0:
            self.horas_extra += horas
            return True
        return False
    
    def agregar_bono(self, cantidad):
        if cantidad > 0:
            self.bonos += cantidad
            return True
        return False
    
    def calcular_salario_total(self):
        pago_horas_extra = self.horas_extra * (self.salario_base/160) * 1.5
        return self.salario_base + pago_horas_extra + self.bonos

# 7. Clase Reserva - Sistema de reservas
class Reserva:
    def __init__(self, id_reserva, cliente, fecha_inicio, fecha_fin):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "pendiente"
        self.servicios_adicionales = []
    
    def confirmar_reserva(self):
        if self.estado == "pendiente":
            self.estado = "confirmada"
            return True
        return False
    
    def cancelar_reserva(self):
        if self.estado != "cancelada":
            self.estado = "cancelada"
            return True
        return False
    
    def agregar_servicio(self, servicio):
        self.servicios_adicionales.append(servicio)

# 8. Clase Tarea - Gestión de tareas
class Tarea:
    def __init__(self, titulo, descripcion, fecha_limite):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.completada = False
        self.subtareas = []
    
    def marcar_completada(self):
        self.completada = True
        return "Tarea completada"
    
    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)
    
    def obtener_progreso(self):
        if not self.subtareas:
            return 100 if self.completada else 0
        completadas = sum(1 for st in self.subtareas if st.completada)
        return (completadas / len(self.subtareas)) * 100

# 9. Clase Usuario - Sistema de usuarios
class Usuario:
    def __init__(self, nombre_usuario, email):
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.__contraseña = None
        self.activo = True
        self.ultimo_acceso = None
    
    def establecer_contraseña(self, contraseña):
        if len(contraseña) >= 8:
            self.__contraseña = hash(contraseña)
            return True
        return False
    
    def verificar_contraseña(self, contraseña):
        return hash(contraseña) == self.__contraseña
    
    def desactivar_cuenta(self):
        self.activo = False
    
    def reactivar_cuenta(self):
        self.activo = True

# 10. Clase Pedido - Sistema de pedidos
class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.items = []
        self.estado = "nuevo"
        self.total = 0
    
    def agregar_item(self, producto, cantidad):
        self.items.append({
            "producto": producto,
            "cantidad": cantidad,
            "subtotal": producto.precio * cantidad
        })
        self.calcular_total()
    
    def calcular_total(self):
        self.total = sum(item["subtotal"] for item in self.items)
    
    def actualizar_estado(self, nuevo_estado):
        estados_validos = ["nuevo", "procesando", "enviado", "entregado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            return True
        return False
