# Herencia múltiple

**Nivel:** intermedio a avanzado
**Antes de este tema:** `03_poo/03_herencia`
**Después de este tema:** `03_poo/05_polimorfismo`

## Objetivos

Al terminar este tema el estudiante puede:

- Definir clases que heredan de varias clases a la vez.
- Explicar y consultar el orden de resolución de métodos (MRO) con
  `Clase.mro()` y `Clase.__mro__`.
- Predecir qué método se ejecuta en el problema del diamante.
- Usar `super()` para que cada clase del diamante se ejecute una sola vez,
  y entender por qué llamar a los padres por su nombre la duplica.
- Escribir constructores cooperativos con `**kwargs` cuando cada padre
  necesita datos distintos.
- Diseñar y usar mixins.
- Reconocer un orden de herencia imposible (`Cannot create a consistent
  method resolution order`).

## Conceptos clave

| Concepto | Idea |
|---|---|
| Sintaxis | `class Hija(Padre1, Padre2):` |
| MRO | Orden en que Python busca un método: la clase, sus padres de izquierda a derecha y `object` al final |
| `mro()` y `__mro__` | El primero es un método que retorna una lista; el segundo, un atributo con una tupla |
| Diamante | `D(B, C)` con `B(A)` y `C(A)`: el MRO es `D, B, C, A`; la base común va al final |
| `super()` | Lleva a la SIGUIENTE clase del MRO del objeto, no necesariamente al padre |
| Llamada explícita | `Clase.metodo(self)` usa la versión de una clase concreta |
| `__init__` cooperativo | Cada clase toma sus argumentos y pasa el resto con `super().__init__(**kwargs)` |
| Mixin | Clase pequeña que aporta una capacidad; va antes de la clase base |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 | Sintaxis, MRO, `mro()` contra `__mro__`, cómo busca Python un método |
| 02 | Problema del diamante: los cuatro casos de resolución |
| 03 | Llamar a los padres por nombre contra `super()` (la base ejecutada dos veces) |
| 04 | `__init__` cooperativo con `**kwargs` |
| 05 | Mixins |
| 06 | MRO imposible y cómo corregirlo |
| 07 - 18 | Más ejemplos: animales, vehículos, dispositivos, roles de empleado, figuras, teléfonos, un error real corregido |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Vehículo anfibio | Básico | Sintaxis, MRO, llamar al método de un padre específico |
| 02 | Leer el MRO | Básico | `mro()`, `__dict__`, cómo se resuelve un método |
| 03 | Diamante con super() | Intermedio | Cada clase una sola vez, a quién lleva `super()` |
| 04 | `__init__` cooperativo | Intermedio | Constructores con datos distintos, `**kwargs` |
| 05 | Productos con mixins | Avanzado | Mixins, `__lt__`, orden de los padres |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Anfibio | Básico | 2 | Sintaxis de los padres, llamada sin `self` |
| 02 | Smartphone | Básico | 2 | Método sin llamar, orden de los padres |
| 03 | Orden imposible | Intermedio | 2 | MRO inconsistente, contrato de un mixin |
| 04 | Monitor | Intermedio | 3 | `kwargs` sin desempaquetar, saltarse una clase del MRO |
| 05 | Impresora multifuncional | Avanzado | 3 | Diamante con llamadas explícitas, orden de los padres, `super` sin paréntesis |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

Consejo: cuando no sepas qué método se va a ejecutar, imprime
`[c.__name__ for c in TuClase.mro()]` y recórrelo de izquierda a derecha.
