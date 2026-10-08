# Herencia simple y multinivel

**Nivel:** intermedio
**Antes de este tema:** `03_poo/02_encapsulamiento`
**Después de este tema:** `03_poo/04_herencia_multiple`

## Objetivos

Al terminar este tema el estudiante puede:

- Crear una clase hija que reutilice atributos y métodos de una clase padre.
- Usar `super()` para inicializar al padre y ampliar sus métodos.
- Sobrescribir métodos y atributos de clase sin duplicar código.
- Construir jerarquías de varios niveles (herencia multinivel).

La herencia de varias clases a la vez (herencia múltiple, MRO, diamante,
mixins) tiene su propio tema: `03_poo/04_herencia_multiple`.

## Conceptos clave

| Concepto | Idea en una línea |
|---|---|
| Herencia simple | `class Hija(Padre):` la hija recibe todo lo del padre |
| `super()` | Llama al método del padre, sin pasar `self` |
| Sobrescritura | La hija define un método con el mismo nombre para cambiar su comportamiento |
| Atributo de clase sobrescrito | La hija cambia `TARIFA = ...` y el método del padre usa `self.TARIFA` |
| Herencia multinivel | `A -> B -> C`: cada nivel agrega algo al anterior |
| `isinstance` | `isinstance(objeto, Padre)` es `True` también para las hijas |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 05 | Herencia simple: animales, electrodomésticos, vehículos |
| 06 - 08 | Casos más completos: notificaciones, productos bancarios |
| 09 | Herencia multinivel |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Empleado y gerente | Básico | `super().__init__()`, sobrescritura |
| 02 | Figuras geométricas | Básico | Reutilizar un método del padre que llama a uno de la hija |
| 03 | Cuentas bancarias | Intermedio | Sobrescribir con validaciones y excepciones |
| 04 | Estudiantes | Intermedio | Herencia multinivel, atributos de clase |
| 05 | Peajes | Avanzado | Multinivel con `super()` encadenado, atributos de clase sobrescritos |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Animal y perro | Básico | 2 | Sintaxis, inicialización del padre |
| 02 | Moto | Básico | 2 | Uso de `super()`, nombre de método |
| 03 | Nómina de vendedores | Intermedio | 3 | Lógica, `return`, argumento mutable |
| 04 | Autos eléctricos | Intermedio | 3 | Cadena de `super()`, `__str__`, `isinstance` |
| 05 | Productos de supermercado | Avanzado | 3 | Argumentos de `super()`, `Clase.ATRIBUTO` contra `self.ATRIBUTO`, límite |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
