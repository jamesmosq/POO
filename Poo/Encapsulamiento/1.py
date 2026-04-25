print("\n" + "=" * 70)
print("🚫 ERRORES COMUNES EN ENCAPSULAMIENTO")
print("=" * 70)


class EjemploErrores:
    """Clase que muestra errores comunes y sus soluciones"""

    def __init__(self, nombre):
        # ❌ ERROR 1: Todo público sin control
        # self.saldo = 1000
        # self.pin = "1234"

        # ✅ CORRECTO: Datos sensibles privados
        self.nombre = nombre  # Público (está bien)
        self.__saldo = 1000  # Privado (datos sensibles)
        self.__pin = "1234"  # Privado (crítico)

    # ❌ ERROR 2: Setter sin validaciones
    def establecer_saldo_malo(self, saldo):
        """Ejemplo de setter malo - sin validaciones"""
        self.__saldo = saldo  # ¡Permite valores negativos!

    # ✅ CORRECTO: Setter con validaciones
    def establecer_saldo_bueno(self, saldo):
        """Setter correcto con validaciones"""
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        if saldo > 1000000:
            raise ValueError("Saldo demasiado alto, contacte al banco")
        self.__saldo = saldo

    # ❌ ERROR 3: Exponer demasiada información interna
    def obtener_info_mala(self):
        """Expone demasiados detalles internos"""
        return {
            'saldo': self.__saldo,
            'pin': self.__pin,  # ¡Nunca exponer el PIN!
            'hash_interno': hash(self.__pin),
            'memoria_objeto': id(self)
        }

    # ✅ CORRECTO: Solo información necesaria
    def obtener_info_buena(self):
        """Solo expone información apropiada"""
        return {
            'nombre': self.nombre,
            'tiene_saldo': self.__saldo > 0,
            'estado_cuenta': 'Activa'
        }

    # ❌ ERROR 4: Método público que debería ser privado
    def validar_pin_publico(self, pin):
        """Este método no debería ser público"""
        return pin == self.__pin

    # ✅ CORRECTO: Método privado para uso interno
    def __validar_pin_privado(self, pin):
        """Método privado para validación interna"""
        return pin == self.__pin

    def operacion_segura(self, pin, accion):
        """Método público que usa validación privada"""
        if not self.__validar_pin_privado(pin):
            return "❌ PIN incorrecto"
        return f"✅ {accion} autorizada"


print("Ejemplos de errores comunes y sus soluciones:")
ejemplo = EjemploErrores("Juan")

# Mostrar diferencias
print(f"Info mala (expone demasiado): NO USAR")
print(f"Info buena: {ejemplo.obtener_info_buena()}")
print(f"Operación segura: {ejemplo.operacion_segura('1234', 'Transferencia')}")

# =============================================================================
# 📚 CASOS DE USO COMUNES PARA ENCAPSULAMIENTO
# =============================================================================

print("\n" + "=" * 70)
print("📚 CASOS DE USO COMUNES PARA ENCAPSULAMIENTO")
print("=" * 70)


# Caso 1: Configuración de Sistema
class ConfiguracionSistema:
    """Encapsula configuraciones críticas del sistema"""

    def __init__(self):
        # Configuraciones críticas privadas
        self.__api_key = "sk-1234567890abcdef"
        self.__db_password = "super_secret_password"
        self.__debug_mode = False
        self.__max_conexiones = 100

        # Configuraciones públicas
        self.nombre_aplicacion = "MiApp"
        self.version = "1.0.0"

    def obtener_cadena_conexion_db(self, usuario):
        """Genera cadena de conexión sin exponer password"""
        return f"postgresql://{usuario}:***@localhost:5432/midb"

    def validar_api_request(self, key_recibida):
        """Valida API key sin exponerla"""
        return key_recibida == self.__api_key

    @property
    def modo_debug(self):
        return self.__debug_mode

    def activar_debug(self, admin_password):
        """Solo administradores pueden activar debug"""
        if admin_password == "admin123":
            self.__debug_mode = True
            return "✅ Modo debug activado"
        return "❌ Acceso denegado"


# Caso 2: Carrito de Compras
class CarritoCompras:
    """Encapsula la lógica de un carrito de compras"""

    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

        # Datos privados del carrito
        self.__items = []
        self.__descuento_aplicado = 0
        self.__codigo_descuento_usado = None

        # Configuraciones privadas
        self.__descuentos_disponibles = {
            "PRIMERA_COMPRA": 0.1,
            "ESTUDIANTE": 0.15,
            "VIP": 0.2
        }

    def agregar_item(self, producto, cantidad, precio):
        """Agrega un item al carrito con validaciones"""
        if cantidad <= 0:
            return "❌ La cantidad debe ser positiva"
        if precio < 0:
            return "❌ El precio no puede ser negativo"

        # Buscar si el producto ya existe
        for item in self.__items:
            if item['producto'] == producto:
                item['cantidad'] += cantidad
                return f"✅ Cantidad actualizada para {producto}"

        # Agregar nuevo item
        self.__items.append({
            'producto': producto,
            'cantidad': cantidad,
            'precio': precio
        })
        return f"✅ {producto} agregado al carrito"

    def aplicar_codigo_descuento(self, codigo):
        """Aplica código de descuento"""
        if self.__codigo_descuento_usado:
            return "❌ Ya hay un código de descuento aplicado"

        if codigo not in self.__descuentos_disponibles:
            return "❌ Código de descuento inválido"

        self.__descuento_aplicado = self.__descuentos_disponibles[codigo]
        self.__codigo_descuento_usado = codigo
        return f"✅ Descuento del {self.__descuento_aplicado * 100}% aplicado"

    def calcular_total(self):
        """Calcula el total del carrito"""
        subtotal = sum(item['cantidad'] * item['precio'] for item in self.__items)
        descuento = subtotal * self.__descuento_aplicado
        return subtotal - descuento

    def obtener_resumen(self):
        """Obtiene resumen del carrito sin exponer estructura interna"""
        return {
            'total_items': sum(item['cantidad'] for item in self.__items),
            'subtotal': sum(item['cantidad'] * item['precio'] for item in self.__items),
            'descuento': f"{self.__descuento_aplicado * 100}%" if self.__descuento_aplicado else "Ninguno",
            'total_final': self.calcular_total()
        }


# Demostraciones de casos de uso
print("Caso 1 - Configuración de Sistema:")
config = ConfiguracionSistema()
print(f"App: {config.nombre_aplicacion} v{config.version}")
print(f"Conexión DB: {config.obtener_cadena_conexion_db('admin')}")
print(f"Validación API: {config.validar_api_request('sk-1234567890abcdef')}")

print(f"\nCaso 2 - Carrito de Compras:")
carrito = CarritoCompras("user123")
print(f"{carrito.agregar_item('Laptop', 1, 1200)}")
print(f"{carrito.agregar_item('Mouse', 2, 25)}")
print(f"{carrito.aplicar_codigo_descuento('ESTUDIANTE')}")
print(f"Resumen: {carrito.obtener_resumen()}")

# =============================================================================
# 🎓 EJERCICIOS PRÁCTICOS PARA ENCAPSULAMIENTO
# =============================================================================

print("\n" + "=" * 70)
print("🎓 EJERCICIOS PRÁCTICOS PARA ENCAPSULAMIENTO")
print("=" * 70)

ejercicios_practicos = """
🎯 **EJERCICIO 1: Sistema de Biblioteca**
Crea una clase 'Libro' que encapsule:
- Datos privados: ISBN, número de copias disponibles, historial de préstamos
- Datos públicos: título, autor, año
- Métodos: prestar(), devolver(), obtener_disponibilidad()
- Validaciones: No prestar si no hay copias, validar ISBN

🎯 **EJERCICIO 2: Cuenta de Ahorro**
Crea una clase 'CuentaAhorro' que encapsule:
- Datos privados: saldo, tasa de interés, fecha último movimiento
- Métodos: depositar(), retirar(), calcular_intereses(), obtener_estado()
- Reglas: Mínimo de saldo, límite de retiros mensuales, interés automático

🎯 **EJERCICIO 3: Sistema de Calificaciones**
Crea una clase 'Estudiante' que encapsule:
- Datos privados: lista de calificaciones, promedio calculado
- Métodos: agregar_calificacion(), obtener_promedio(), obtener_estado_academico()
- Validaciones: Calificaciones entre 0-10, cálculo automático de promedio

🎯 **EJERCICIO 4: Termostato Inteligente**
Crea una clase 'Termostato' que encapsule:
- Datos privados: temperatura actual, programación, consumo energético
- Métodos: establecer_temperatura(), programar_horario(), obtener_estadisticas()
- Validaciones: Rangos de temperatura, programación válida

🎯 **EJERCICIO 5: Inventario de Tienda**
Crea una clase 'ProductoInventario' que encapsule:
- Datos privados: stock actual, punto de reorden, historial movimientos
- Métodos: agregar_stock(), vender(), necesita_reorden(), obtener_reporte()
- Validaciones: Stock no negativo, alertas automáticas de stock bajo
"""

print(ejercicios_practicos)

# =============================================================================
# 🏆 EJEMPLO COMPLETO: SISTEMA BANCARIO AVANZADO
# =============================================================================

print("\n" + "=" * 70)
print("🏆 EJEMPLO COMPLETO: SISTEMA BANCARIO AVANZADO")
print("=" * 70)


class CuentaBancariaAvanzada:
    """Ejemplo completo que demuestra todos los aspectos del encapsulamiento"""

    # Atributos de clase (compartidos por todas las instancias)
    _banco_nombre = "Banco Seguro S.A."
    _tasa_interes_base = 0.02

    def __init__(self, titular, saldo_inicial, tipo_cuenta="ahorro"):
        # Validaciones en constructor
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        # Atributos públicos
        self.titular = titular
        self.tipo_cuenta = tipo_cuenta
        self.fecha_creacion = self._obtener_fecha_actual()

        # Atributos protegidos (para herencia)
        self._numero_cuenta = self._generar_numero_cuenta()
        self._sucursal = "001"

        # Atributos privados (datos sensibles)
        self.__saldo = saldo_inicial
        self.__pin = self._generar_pin_inicial()
        self.__intentos_fallidos = 0
        self.__cuenta_bloqueada = False
        self.__historial_transacciones = []
        self.__limite_diario = 5000
        self.__retiros_hoy = 0
        self.__fecha_ultimo_retiro = None

    # Propiedades para acceso controlado
    @property
    def saldo(self):
        """Getter para saldo - solo lectura"""
        return self.__saldo

    @property
    def numero_cuenta(self):
        """Getter para número de cuenta - solo lectura"""
        return self._numero_cuenta

    @property
    def esta_bloqueada(self):
        """Verifica si la cuenta está bloqueada"""
        return self.__cuenta_bloqueada

    @property
    def limite_diario_disponible(self):
        """Calcula el límite diario disponible"""
        if self._es_nuevo_dia():
            self.__retiros_hoy = 0
        return self.__limite_diario - self.__retiros_hoy

    # Métodos públicos principales
    def consultar_saldo(self, pin):
        """Consulta el saldo con autenticación"""
        if not self._autenticar(pin):
            return "❌ Autenticación fallida"

        return {
            'saldo': self.__saldo,
            'limite_disponible': self.limite_diario_disponible,
            'estado': 'Activa' if not self.__cuenta_bloqueada else 'Bloqueada'
        }

    def depositar(self, cantidad, concepto="Depósito"):
        """Deposita dinero con validaciones"""
        if cantidad <= 0:
            return "❌ La cantidad debe ser positiva"

        if cantidad > 100000:
            return "❌ Depósito muy grande, contacte al banco"

        self.__saldo += cantidad
        self._registrar_transaccion("Depósito", cantidad, concepto)

        return {
            'mensaje': f"✅ Depósito exitoso",
            'cantidad': cantidad,
            'saldo_nuevo': self.__saldo,
            'numero_transaccion': len(self.__historial_transacciones)
        }

    def retirar(self, cantidad, pin, concepto="Retiro"):
        """Retira dinero con autenticación y validaciones"""
        # Autenticación
        if not self._autenticar(pin):
            return "❌ Autenticación fallida"

        # Validaciones de negocio
        validacion = self._validar_retiro(cantidad)
        if validacion != "OK":
            return validacion

        # Realizar retiro
        self.__saldo -= cantidad
        self.__retiros_hoy += cantidad
        self.__fecha_ultimo_retiro = self._obtener_fecha_actual()
        self._registrar_transaccion("Retiro", -cantidad, concepto)

        return {
            'mensaje': f"✅ Retiro exitoso",
            'cantidad': cantidad,
            'saldo_nuevo': self.__saldo,
            'limite_restante': self.limite_diario_disponible
        }

    def transferir(self, cantidad, cuenta_destino, pin, concepto="Transferencia"):
        """Transfiere dinero a otra cuenta"""
        if not self._autenticar(pin):
            return "❌ Autenticación fallida"

        # Usar retiro para validaciones y luego depositar en destino
        resultado_retiro = self.retirar(cantidad, pin, f"Transferencia a {cuenta_destino}")

        if "exitoso" in resultado_retiro.get('mensaje', ''):
            # Simular depósito en cuenta destino (en un sistema real, sería otra instancia)
            self._registrar_transaccion("Transferencia", -cantidad, concepto)
            return {
                'mensaje': f"✅ Transferencia exitosa a {cuenta_destino}",
                'cantidad': cantidad,
                'saldo_nuevo': self.__saldo
            }

        return resultado_retiro

    def cambiar_pin(self, pin_actual, pin_nuevo):
        """Cambia el PIN con validaciones de seguridad"""
        if not self._autenticar(pin_actual):
            return "❌ PIN actual incorrecto"

        if len(pin_nuevo) != 4 or not pin_nuevo.isdigit():
            return "❌ El nuevo PIN debe tener 4 dígitos"

        if pin_nuevo == pin_actual:
            return "❌ El nuevo PIN debe ser diferente al actual"

        self.__pin = pin_nuevo
        self._registrar_transaccion("Cambio PIN", 0, "Cambio de PIN de seguridad")

        return "✅ PIN cambiado exitosamente"

    def obtener_historial(self, pin, ultimas=10):
        """Obtiene el historial de transacciones"""
        if not self._autenticar(pin):
            return "❌ Autenticación fallida"

        historial_reciente = self.__historial_transacciones[-ultimas:]
        return {
            'transacciones': historial_reciente,
            'total_transacciones': len(self.__historial_transacciones)
        }

    def calcular_intereses(self):
        """Calcula y aplica intereses mensuales"""
        if self.tipo_cuenta == "ahorro" and self.__saldo > 0:
            interes = self.__saldo * self._tasa_interes_base
            self.__saldo += interes
            self._registrar_transaccion("Interés", interes, "Interés mensual")
            return f"✅ Interés aplicado: ${interes:.2f}"

        return "ℹ️ Esta cuenta no genera intereses"

    # Métodos protegidos (para herencia)
    def _autenticar(self, pin):
        """Método protegido para autenticación"""
        if self.__cuenta_bloqueada:
            return False

        if pin == self.__pin:
            self.__intentos_fallidos = 0
            return True

        self.__intentos_fallidos += 1
        if self.__intentos_fallidos >= 3:
            self.__cuenta_bloqueada = True
            self._registrar_transaccion("Bloqueo", 0, "Cuenta bloqueada por intentos fallidos")

        return False

    def _validar_retiro(self, cantidad):
        """Método protegido para validar retiros"""
        if cantidad <= 0:
            return "❌ La cantidad debe ser positiva"

        if cantidad > self.__saldo:
            return "❌ Fondos insuficientes"

        if self._es_nuevo_dia():
            self.__retiros_hoy = 0

        if cantidad > self.limite_diario_disponible:
            return f"❌ Excede límite diario. Disponible: ${self.limite_diario_disponible}"

        return "OK"

    def _registrar_transaccion(self, tipo, monto, concepto):
        """Método protegido para registrar transacciones"""
        transaccion = {
            'fecha': self._obtener_fecha_actual(),
            'tipo': tipo,
            'monto': monto,
            'concepto': concepto,
            'saldo_resultante': self.__saldo
        }
        self.__historial_transacciones.append(transaccion)

    # Métodos privados (solo uso interno)
    def __generar_numero_cuenta(self):
        """Genera número de cuenta único"""
        import random
        return ''.join([str(random.randint(0, 9)) for _ in range(12)])

    def _generar_numero_cuenta(self):
        """Método protegido para generar número de cuenta"""
        import random
        return ''.join([str(random.randint(0, 9)) for _ in range(12)])

    def _generar_pin_inicial(self):
        """Genera PIN inicial temporal"""
        import random
        return ''.join([str(random.randint(0, 9)) for _ in range(4)])

    def _obtener_fecha_actual(self):
        """Obtiene la fecha actual"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _es_nuevo_dia(self):
        """Verifica si es un nuevo día desde el último retiro"""
        if not self.__fecha_ultimo_retiro:
            return True

        from datetime import datetime
        fecha_actual = datetime.now().date()
        fecha_ultimo = datetime.strptime(self.__fecha_ultimo_retiro, "%Y-%m-%d %H:%M:%S").date()
        return fecha_actual != fecha_ultimo

    def __str__(self):
        """Representación string de la cuenta"""
        return f"Cuenta {self.tipo_cuenta.title()} - {self.titular} ({self._numero_cuenta})"


# Demostración del sistema bancario completo
print("Sistema Bancario Avanzado - Demostración completa:")

# Crear cuenta
cuenta = CuentaBancariaAvanzada("María Elena Rodríguez", 5000, "ahorro")
print(f"Cuenta creada: {cuenta}")
print(f"PIN inicial: {cuenta._generar_pin_inicial()} (en sistema real sería enviado por separado)")

# Simular PIN conocido para demostración
pin_demo = "1234"
cuenta._CuentaBancariaAvanzada__pin = pin_demo

# Operaciones bancarias
print(f"\n📋 Operaciones bancarias:")
print(f"Consulta: {cuenta.consultar_saldo(pin_demo)}")
print(f"Depósito: {cuenta.depositar(1500, 'Salario')}")
print(f"Retiro: {cuenta.retirar(500, pin_demo, 'Compras')}")
print(f"Transferencia: {cuenta.transferir(300, '987654321098', pin_demo)}")

# Cambio de PIN
print(f"\n🔐 Seguridad:")
print(f"Cambio PIN: {cuenta.cambiar_pin(pin_demo, '9876')}")

# Historial
nuevo_pin = "9876"
print(f"\n📊 Historial:")
historial = cuenta.obtener_historial(nuevo_pin, 5)
for transaccion in historial['transacciones']:
    print(f"  {transaccion['fecha']} - {transaccion['tipo']}: ${transaccion['monto']} ({transaccion['concepto']})")

# Aplicar intereses
print(f"\n💰 Intereses:")
print(f"{cuenta.calcular_intereses()}")
print(f"Saldo final: ${cuenta.saldo}")

print("\n🎉 ¡Demostración completa de encapsulamiento realizada!")
print("Este ejemplo muestra todos los aspectos clave del encapsulamiento:")
print("- Datos privados protegidos")
print("- Métodos públicos con validaciones")
print("- Propiedades para acceso controlado")
print("- Métodos protegidos para herencia")
print("- Autenticación y seguridad")
print("- Manejo de estados internos")
print("- Interfaz limpia y fácil de usar")