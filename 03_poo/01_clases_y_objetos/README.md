# Clases y objetos

**Nivel:** intermedio
**Antes de este tema:** `02_estructuras_de_datos/03_colas`
**Después de este tema:** `03_poo/02_encapsulamiento`

## Objetivos

- Definir clases con atributos y métodos.
- Crear objetos (instancias) y entender que cada uno tiene sus propios datos.
- Usar `self` correctamente.
- Diferenciar atributos de instancia y atributos de clase.
- Usar `@staticmethod` y `@classmethod`.
- Combinar objetos (composición): un objeto que contiene a otros.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Clase | `class Persona:` |
| Constructor | `def __init__(self, nombre):` |
| Atributo de instancia | `self.nombre = nombre` (uno por objeto) |
| Atributo de clase | `total = 0` en el cuerpo de la clase (compartido) |
| Método | `def saludar(self):` |
| Método estático | `@staticmethod` no recibe `self` |
| Método de clase | `@classmethod` recibe `cls`; sirve para constructores alternativos |
| Composición | `Curso` tiene una lista de `Estudiante` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 02 | Atributos de clase, constructor y métodos |
| 03 - 07 | Clases de personas, libros, estudiantes y cursos |
| 08 - 11 | Sistemas pequeños: biblioteca, pedidos, hotel, inventario con menú |
| 12 | Colección de clases de ejemplo |
| 13 | `__new__`, `__init__` y el patrón Singleton |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Clase Persona | Básico | `__init__`, `self`, métodos |
| 02 | Producto | Básico | Métodos que modifican el estado, validación |
| 03 | Atributos y métodos de clase | Intermedio | Contador de clase, `@staticmethod`, `@classmethod` |
| 04 | Curso y estudiantes | Intermedio | Composición, listas de objetos |
| 05 | Carrito de compras | Avanzado | Diseño de varias clases que colaboran |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Persona | Básico | 2 | `__init__` mal escrito, `self` faltante |
| 02 | Producto con descuento | Básico | 2 | Atributo sin `self`, llamar métodos internos |
| 03 | Atributos compartidos | Intermedio | 2 | Lista de clase compartida, contador de clase |
| 04 | Biblioteca | Intermedio | 3 | `@staticmethod`, comparar objetos, `return` faltante |
| 05 | Carrito | Avanzado | 3 | `+=`, cálculo del total, lista por defecto compartida |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
