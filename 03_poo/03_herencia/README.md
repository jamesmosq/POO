# Herencia

**Nivel:** intermedio
**Antes de este tema:** `03_poo/01_clases_y_objetos`
**Después de este tema:** `03_poo/04_polimorfismo`

## Objetivos

Al terminar este tema el estudiante puede:

- Crear una clase hija que reutilice atributos y métodos de una clase padre.
- Usar `super()` para inicializar al padre y ampliar sus métodos.
- Sobrescribir métodos sin duplicar código.
- Construir jerarquías de varios niveles (herencia multinivel).
- Combinar varias clases padre (herencia múltiple) y explicar el orden de
  resolución de métodos (MRO).

## Conceptos clave

| Concepto | Idea en una línea |
|---|---|
| Herencia simple | `class Hija(Padre):` la hija recibe todo lo del padre. |
| `super()` | Llama al método del siguiente padre en el MRO, sin pasar `self`. |
| Sobrescritura | La hija define un método con el mismo nombre para cambiar su comportamiento. |
| Herencia multinivel | `A -> B -> C`: cada nivel agrega algo al anterior. |
| Herencia múltiple | `class C(A, B):` el orden de los padres importa. |
| MRO | `Clase.__mro__` muestra el orden en que Python busca los métodos. |
| Mixin | Clase pequeña que aporta una sola capacidad y se combina con otras. |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 08 | Herencia simple: animales, electrodomésticos, vehículos, notificaciones, productos bancarios |
| 09 | Herencia multinivel |
| 10 - 20 | Herencia múltiple: animales, vehículos, dispositivos, roles de empleado, MRO |
| 21 | Un error real de herencia múltiple y su corrección |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Empleado y gerente | Básico | `super().__init__()`, sobrescritura |
| 02 | Figuras geométricas | Básico | Reutilizar un método del padre que llama a uno de la hija |
| 03 | Cuentas bancarias | Intermedio | Sobrescribir con validaciones y excepciones |
| 04 | Estudiantes | Intermedio | Herencia multinivel, atributos de clase |
| 05 | Productos con mixins | Avanzado | Herencia múltiple, mixins, MRO, `__lt__` |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Animal y perro | Básico | 2 | Sintaxis, inicialización del padre |
| 02 | Moto | Básico | 2 | Uso de `super()`, nombre de método |
| 03 | Nómina de vendedores | Intermedio | 3 | Lógica, `return`, argumento mutable |
| 04 | Autos eléctricos | Intermedio | 3 | Cadena de `super()`, `__str__`, `isinstance` |
| 05 | Impresora multifuncional | Avanzado | 3 | Herencia en diamante, MRO |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
