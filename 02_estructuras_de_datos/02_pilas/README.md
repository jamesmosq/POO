# Pilas

**Nivel:** intermedio
**Antes de este tema:** `02_estructuras_de_datos/01_busqueda_y_ordenamiento`
**Después de este tema:** `02_estructuras_de_datos/03_colas`

## Objetivos

- Entender el principio LIFO (el último en entrar es el primero en salir).
- Implementar una pila con una lista de Python.
- Resolver problemas clásicos con pilas: invertir, validar paréntesis,
  deshacer y rehacer, historial del navegador, evaluar expresiones.
- Manejar el caso de la pila vacía.

## Conceptos clave

| Operación | Con una lista | Qué hace |
|---|---|---|
| Apilar (push) | `pila.append(x)` | Agrega en la cima |
| Desapilar (pop) | `pila.pop()` | Quita y retorna la cima |
| Cima (peek) | `pila[-1]` | Mira la cima sin quitarla |
| Vacía | `not pila` o `len(pila) == 0` | ¿Hay elementos? |

`pila.pop(0)` NO es una operación de pila: saca el primer elemento (eso es
una cola).

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 | Pila completa: operaciones básicas, avanzadas y aplicaciones (invertir, palíndromos, bases, postfija, balanceo) |
| 02 | Pila con manejo de errores |
| 03 - 05 | Aplicaciones: deshacer y rehacer, historial del navegador, decimal a binario |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Pila básica | Básico | Operaciones de la pila, pila vacía |
| 02 | Invertir textos y palíndromos | Básico | LIFO para invertir |
| 03 | Paréntesis balanceados | Intermedio | Validar estructura con una pila |
| 04 | Deshacer y rehacer | Intermedio | Dos pilas que cooperan |
| 05 | Notación postfija y cambio de base | Avanzado | Pila como evaluador, orden de operandos |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Una pila que no es pila | Básico | 2 | LIFO contra FIFO, cima |
| 02 | Invertir con pila | Básico | 2 | Método sin llamar, doble inversión |
| 03 | Paréntesis balanceados | Intermedio | 2 | Pila al final, pareja correcta |
| 04 | Historial del navegador | Intermedio | 3 | Pila vacía, `pop(0)`, limpiar adelante |
| 05 | Calculadora postfija | Avanzado | 3 | Decimales, orden de operandos, operandos sobrantes |

## Cómo trabajar los ejercicios

Los ejercicios con clases traen el esqueleto ya escrito: completa el cuerpo
de cada método. Las clases se estudian a fondo en `03_poo`.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.
