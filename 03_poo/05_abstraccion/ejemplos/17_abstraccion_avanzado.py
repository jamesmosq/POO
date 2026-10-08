from abc import ABC, abstractmethod
import math

# =============================================================================
# 🎯 ¿QUÉ SON LOS MÉTODOS ABSTRACTOS?
# =============================================================================

"""
Un método abstracto es un método que:
1. Se DECLARA en la clase padre pero NO se implementa
2. OBLIGA a las clases hijas a implementarlo
3. Define QUÉ debe hacer, pero no CÓMO hacerlo
4. Garantiza que todas las subclases tengan ese comportamiento

Es como decir: "Todos mis hijos DEBEN saber hacer esto, 
pero cada uno lo hará a su manera"
"""

# =============================================================================
# 📚 EJEMPLO 1: CONCEPTOS BÁSICOS - Animales
# =============================================================================

print("=" * 60)
print("🐾 EJEMPLO 1: MÉTODOS ABSTRACTOS BÁSICOS")
print("=" * 60)


class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # MÉTODO CONCRETO (todos los animales tienen el mismo comportamiento)
    def dormir(self):
        return f"{self.nombre} está durmiendo 😴"

    # MÉTODO ABSTRACTO (cada animal hace sonido diferente)
    @abstractmethod
    def hacer_sonido(self):
        """Cada animal debe implementar su propio sonido"""
        pass

    # MÉTODO ABSTRACTO (cada animal se mueve diferente)
    @abstractmethod
    def moverse(self):
        """Cada animal debe implementar su forma de moverse"""
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau guau! 🐕"

    def moverse(self):
        return f"{self.nombre} corre con sus cuatro patas 🏃‍♂️"


class Pez(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} hace burbujas: blub blub 🐠"

    def moverse(self):
        return f"{self.nombre} nada moviendo su cola 🏊‍♂️"


# Demostración
perro = Perro("Rex", 3)
pez = Pez("Nemo", 1)

print(f"Método concreto - {perro.dormir()}")
print(f"Método abstracto - {perro.hacer_sonido()}")
print(f"Método abstracto - {perro.moverse()}")
print()
print(f"Método concreto - {pez.dormir()}")
print(f"Método abstracto - {pez.hacer_sonido()}")
print(f"Método abstracto - {pez.moverse()}")

# =============================================================================
# 🧮 EJEMPLO 2: MATEMÁTICAS - Figuras Geométricas
# =============================================================================

print("\n" + "=" * 60)
print("📐 EJEMPLO 2: MÉTODOS ABSTRACTOS EN MATEMÁTICAS")
print("=" * 60)


class Figura(ABC):
    def __init__(self, color="blanco"):
        self.color = color

    # Método concreto - todos cambian color igual
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        return f"Color cambiado a {nuevo_color}"

    # Métodos abstractos - cada figura calcula diferente
    @abstractmethod
    def calcular_area(self):
        """Cada figura debe implementar su cálculo de área"""
        pass

    @abstractmethod
    def calcular_perimetro(self):
        """Cada figura debe implementar su cálculo de perímetro"""
        pass

    @abstractmethod
    def describir(self):
        """Cada figura debe describirse a sí misma"""
        pass


class Circulo(Figura):
    def __init__(self, radio, color="blanco"):
        super().__init__(color)
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return round(area, 2)

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return round(perimetro, 2)

    def describir(self):
        return f"Círculo {self.color} con radio {self.radio}"


class Rectangulo(Figura):
    def __init__(self, largo, ancho, color="blanco"):
        super().__init__(color)
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.largo + self.ancho)

    def describir(self):
        return f"Rectángulo {self.color} de {self.largo}x{self.ancho}"


# Demostración con polimorfismo
figuras = [
    Circulo(5, "rojo"),
    Rectangulo(4, 6, "azul"),
    Circulo(3, "verde")
]

print("📊 CALCULANDO PROPIEDADES DE FIGURAS:")
for figura in figuras:
    print(f"\n{figura.describir()}")
    print(f"  Área: {figura.calcular_area()}")
    print(f"  Perímetro: {figura.calcular_perimetro()}")

# =============================================================================
# 💻 EJEMPLO 3: PROCESAMIENTO DE DATOS
# =============================================================================

print("\n" + "=" * 60)
print("💾 EJEMPLO 3: PROCESADORES DE ARCHIVOS")
print("=" * 60)


class ProcesadorArchivo(ABC):
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.datos = []

    # Método concreto - mismo para todos
    def obtener_info_archivo(self):
        return f"Procesando: {self.nombre_archivo}"

    # Métodos abstractos - cada tipo de archivo se procesa diferente
    @abstractmethod
    def leer_archivo(self):
        """Cada procesador debe saber leer su tipo de archivo"""
        pass

    @abstractmethod
    def validar_datos(self):
        """Cada procesador debe validar según su formato"""
        pass

    @abstractmethod
    def procesar_datos(self):
        """Cada procesador debe procesar según su tipo"""
        pass


class ProcesadorCSV(ProcesadorArchivo):
    def leer_archivo(self):
        # Simulación de lectura CSV
        self.datos = [
            ["Juan", "25", "Ingeniero"],
            ["Ana", "30", "Doctora"],
            ["Carlos", "28", "Profesor"]
        ]
        return f"✅ CSV leído: {len(self.datos)} filas"

    def validar_datos(self):
        errores = []
        for i, fila in enumerate(self.datos):
            if len(fila) != 3:
                errores.append(f"Fila {i + 1}: número incorrecto de columnas")
        return "✅ Datos válidos" if not errores else f"❌ Errores: {errores}"

    def procesar_datos(self):
        resultado = []
        for fila in self.datos:
            persona = {
                'nombre': fila[0],
                'edad': int(fila[1]),
                'profesion': fila[2]
            }
            resultado.append(persona)
        return f"📊 Procesados {len(resultado)} registros de personas"


class ProcesadorJSON(ProcesadorArchivo):
    def leer_archivo(self):
        # Simulación de lectura JSON
        self.datos = {
            "productos": [
                {"id": 1, "nombre": "Laptop", "precio": 1200},
                {"id": 2, "nombre": "Mouse", "precio": 25}
            ]
        }
        return f"✅ JSON leído: {len(self.datos['productos'])} productos"

    def validar_datos(self):
        productos = self.datos.get('productos', [])
        for producto in productos:
            required_fields = ['id', 'nombre', 'precio']
            if not all(field in producto for field in required_fields):
                return "❌ Faltan campos requeridos en productos"
        return "✅ Estructura JSON válida"

    def procesar_datos(self):
        productos = self.datos['productos']
        total_valor = sum(p['precio'] for p in productos)
        return f"💰 Inventario procesado: ${total_valor} en {len(productos)} productos"


# Demostración
procesadores = [
    ProcesadorCSV("empleados.csv"),
    ProcesadorJSON("inventario.json")
]

print("🔄 PROCESANDO ARCHIVOS CON MÉTODOS ABSTRACTOS:")
for procesador in procesadores:
    print(f"\n📁 {procesador.obtener_info_archivo()}")
    print(f"  1. {procesador.leer_archivo()}")
    print(f"  2. {procesador.validar_datos()}")
    print(f"  3. {procesador.procesar_datos()}")

# =============================================================================
# 🎮 EJEMPLO 4: SISTEMA DE JUEGO AVANZADO
# =============================================================================

print("\n" + "=" * 60)
print("🎮 EJEMPLO 4: SISTEMA DE JUEGO CON MÚLTIPLES MÉTODOS ABSTRACTOS")
print("=" * 60)


class Personaje(ABC):
    def __init__(self, nombre, vida=100, nivel=1):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel
        self.experiencia = 0

    # Métodos concretos - iguales para todos
    def subir_nivel(self):
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            self.vida += 20
            return f"🆙 {self.nombre} subió al nivel {self.nivel}!"
        return f"📊 {self.nombre} necesita {100 - self.experiencia} EXP más"

    def recibir_daño(self, daño):
        self.vida = max(0, self.vida - daño)
        return f"💔 {self.nombre} recibió {daño} de daño. Vida: {self.vida}"

    # Métodos abstractos - cada clase los implementa diferente
    @abstractmethod
    def atacar(self, objetivo):
        """Cada personaje ataca de forma diferente"""
        pass

    @abstractmethod
    def defender(self):
        """Cada personaje se defiende de forma diferente"""
        pass

    @abstractmethod
    def habilidad_especial(self):
        """Cada personaje tiene habilidades únicas"""
        pass

    @abstractmethod
    def calcular_daño_base(self):
        """Cada personaje calcula daño diferente"""
        pass


class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.fuerza = 15
        self.armadura = 10

    def atacar(self, objetivo):
        daño = self.calcular_daño_base()
        self.experiencia += 10
        return f"⚔️ {self.nombre} ataca con espada causando {daño} de daño!"

    def defender(self):
        defensa = self.armadura + self.nivel * 2
        return f"🛡️ {self.nombre} se defiende con escudo (+{defensa} defensa)"

    def habilidad_especial(self):
        daño_especial = self.fuerza * 2
        self.experiencia += 20
        return f"💥 {self.nombre} usa GOLPE DEVASTADOR ({daño_especial} daño)"

    def calcular_daño_base(self):
        return self.fuerza + self.nivel * 3


class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.inteligencia = 20
        self.mana = 50

    def atacar(self, objetivo):
        if self.mana >= 10:
            daño = self.calcular_daño_base()
            self.mana -= 10
            self.experiencia += 15
            return f"🔥 {self.nombre} lanza bola de fuego ({daño} daño, mana: {self.mana})"
        return f"💧 {self.nombre} no tiene suficiente mana"

    def defender(self):
        if self.mana >= 5:
            self.mana -= 5
            defensa = self.inteligencia
            return f"✨ {self.nombre} crea escudo mágico (+{defensa} defensa)"
        return f"💧 {self.nombre} no puede crear escudo (sin mana)"

    def habilidad_especial(self):
        if self.mana >= 25:
            self.mana -= 25
            daño_especial = self.inteligencia * 3
            self.experiencia += 30
            return f"⚡ {self.nombre} invoca TORMENTA ELÉCTRICA ({daño_especial} daño)"
        return f"💧 {self.nombre} necesita más mana para la tormenta"

    def calcular_daño_base(self):
        return self.inteligencia + self.nivel * 2


# Demostración de combate
guerrero = Guerrero("Arthas")
mago = Mago("Gandalf")

print("⚔️ SIMULACIÓN DE COMBATE:")
print(f"\n👥 Personajes:")
print(f"  {guerrero.nombre}: Vida={guerrero.vida}, Nivel={guerrero.nivel}")
print(f"  {mago.nombre}: Vida={mago.vida}, Nivel={mago.nivel}, Mana={mago.mana}")

print(f"\n🥊 Turno 1:")
print(f"  {guerrero.atacar(mago)}")
print(f"  {mago.defender()}")

print(f"\n🥊 Turno 2:")
print(f"  {mago.habilidad_especial()}")
print(f"  {guerrero.defender()}")

print(f"\n📊 Estado después del combate:")
print(f"  {guerrero.subir_nivel()}")
print(f"  {mago.subir_nivel()}")

# =============================================================================
# 🎯 EJERCICIOS PARA PRACTICAR
# =============================================================================

print("\n" + "=" * 60)
print("📝 EJERCICIOS PARA PRACTICAR MÉTODOS ABSTRACTOS")
print("=" * 60)

ejercicios = """
🎯 EJERCICIO 1: Sistema de Notificaciones
Crea una clase abstracta 'Notificacion' con métodos abstractos:
- enviar()
- validar_destinatario()
- formatear_mensaje()

Implementa: NotificacionEmail, NotificacionSMS, NotificacionPush

🎯 EJERCICIO 2: Calculadora de Impuestos
Crea una clase abstracta 'CalculadoraImpuestos' con métodos abstractos:
- calcular_impuesto_base()
- aplicar_deducciones()
- generar_reporte()

Implementa: ImpuestoPersonaFisica, ImpuestoEmpresa

🎯 EJERCICIO 3: Reproductores de Media
Crea una clase abstracta 'ReproductorMedia' con métodos abstractos:
- reproducir()
- pausar()
- obtener_duracion()
- cambiar_calidad()

Implementa: ReproductorVideo, ReproductorAudio, ReproductorStreaming

🎯 EJERCICIO 4: Sistema de Autenticación
Crea una clase abstracta 'MetodoAutenticacion' con métodos abstractos:
- validar_credenciales()
- generar_token()
- verificar_permisos()

Implementa: AutenticacionPassword, AutenticacionBiometrica, AutenticacionDosFactores
"""

print(ejercicios)

# =============================================================================
# 🔑 CONSEJOS CLAVE
# =============================================================================

print("\n" + "=" * 60)
print("💡 CONSEJOS PARA USAR MÉTODOS ABSTRACTOS EFECTIVAMENTE")
print("=" * 60)

consejos = """
✅ CUÁNDO USAR MÉTODOS ABSTRACTOS:
1. Cuando TODAS las subclases deben tener un comportamiento, pero cada una lo hace diferente
2. Para garantizar que ninguna subclase olvide implementar métodos críticos
3. Cuando quieres definir una "interfaz común" pero con implementaciones variables

❌ CUÁNDO NO USARLOS:
1. Si el comportamiento es exactamente igual en todas las subclases
2. Si solo algunas subclases necesitan el método
3. Si el método es opcional

🎯 MEJORES PRÁCTICAS:
1. Usa nombres descriptivos que indiquen QUÉ hace el método
2. Incluye docstrings explicando qué debe hacer cada implementación
3. Combina métodos abstractos con métodos concretos
4. No abuses: solo los métodos realmente necesarios deben ser abstractos

🔍 CÓMO IDENTIFICAR QUÉ DEBE SER ABSTRACTO:
- Pregúntate: "¿TODAS mis subclases van a hacer esto, pero de manera diferente?"
- Si la respuesta es SÍ → método abstracto
- Si la respuesta es NO → método concreto o no incluir
"""

print(consejos)

print("\n🎉 ¡Ahora tienes las herramientas para usar métodos abstractos como un profesional!")