# Abstracción

**Nivel:** intermedio a avanzado
**Antes de este tema:** `03_poo/04_polimorfismo`
**Después de este tema:** `03_poo/06_metodos_magicos`

## Objetivos

- Crear clases abstractas con `ABC` y `@abstractmethod`.
- Entender que una clase abstracta define un contrato: qué deben hacer las
  hijas, no cómo.
- Combinar métodos abstractos con métodos concretos (método plantilla).
- Declarar propiedades abstractas con el orden correcto de decoradores.
- Diseñar código extensible: agregar comportamiento con clases nuevas, sin
  modificar el código existente.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Clase abstracta | `class Figura(ABC):` |
| Método abstracto | `@abstractmethod def area(self): pass` |
| Propiedad abstracta | `@property` arriba y `@abstractmethod` abajo |
| No instanciable | `Figura()` lanza `TypeError` |
| Hija incompleta | Si no implementa todos los abstractos, tampoco se puede instanciar |
| Interfaz | Clase abstracta solo con métodos abstractos |
| Método plantilla | Método concreto que llama a pasos abstractos |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 | Introducción completa: animales, figuras y procesamiento de datos |
| 02 - 05 | Sistema bancario, formas, propiedades abstractas, aplicaciones móviles |
| 06 - 13 | Ejercicios resueltos: instrumentos, comidas, personal médico, electrodomésticos, tienda, streaming |
| 14 - 17 | Casos avanzados: personas y rendimiento, vehículos, procesadores de archivos |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Vehículos abstractos | Básico | `ABC`, método abstracto y concreto |
| 02 | Interfaz de almacenamiento | Intermedio | Intercambiar implementaciones (memoria y JSON) |
| 03 | Propiedades abstractas | Intermedio | `@property` + `@abstractmethod` |
| 04 | Plantilla de reportes | Intermedio | Método plantilla |
| 05 | Exportadores | Avanzado | Extensibilidad con `__subclasses__` |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Instrumentos | Básico | 2 | Importación faltante, método abstracto sin implementar |
| 02 | Empleados abstractos | Básico | 2 | Falta heredar de `ABC`, usar `super()` en un método abstracto |
| 03 | Propiedad abstracta | Intermedio | 2 | Orden de decoradores, propiedad contra método |
| 04 | Reportes | Intermedio | 3 | `super().__init__`, `return` en el ciclo, desempaquetar |
| 05 | Exportadores | Avanzado | 3 | Propiedad leída desde la clase, `join` con números, validación |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
