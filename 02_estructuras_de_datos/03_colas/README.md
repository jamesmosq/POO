# Colas

**Nivel:** intermedio
**Antes de este tema:** `02_estructuras_de_datos/02_pilas`
**Después de este tema:** `03_poo/01_clases_y_objetos`

## Objetivos

- Entender el principio FIFO (el primero en entrar es el primero en salir).
- Implementar una cola con una lista y con `collections.deque`.
- Conocer variantes: cola de prioridad y cola circular.
- Simular procesos reales con colas: turnos, impresoras, juegos por turnos.

## Conceptos clave

| Operación | Con una lista | Con `deque` |
|---|---|---|
| Encolar | `cola.append(x)` | `cola.append(x)` |
| Desencolar | `cola.pop(0)` (lento en listas grandes) | `cola.popleft()` (rápido) |
| Frente | `cola[0]` | `cola[0]` |
| Rotar | No existe | `cola.rotate(-1)` pasa el primero al final |

| Variante | Idea |
|---|---|
| Cola de prioridad | Sale primero el más urgente; entre iguales, el que llegó antes |
| Cola circular | Tamaño fijo; los índices dan la vuelta con `%` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 | Cola básica con lista |
| 02 | Cola completa con más operaciones |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Cola básica | Básico | Operaciones de la cola, cola vacía |
| 02 | Turnos con deque | Básico | `popleft`, `appendleft` |
| 03 | Cola de prioridad | Intermedio | Inserción ordenada y estable |
| 04 | Cola circular | Intermedio | Aritmética modular, tamaño fijo |
| 05 | Simulaciones con colas | Avanzado | `rotate`, tiempo acumulado |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Una cola que no es cola | Básico | 2 | FIFO contra LIFO, frente |
| 02 | Atender turnos | Básico | 2 | Método sin llamar, cola vacía |
| 03 | Cola de prioridad | Intermedio | 2 | Estabilidad, extremo equivocado |
| 04 | Cola circular | Intermedio | 3 | Condición de llena, contador, índice circular |
| 05 | Impresora y papa caliente | Avanzado | 3 | Dirección de `rotate`, redondeo, acumulador |

## Cómo trabajar los ejercicios

Los ejercicios con clases traen el esqueleto ya escrito: completa el cuerpo
de cada método.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.
