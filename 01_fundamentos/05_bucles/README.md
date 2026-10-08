# Bucles: for y while

**Nivel:** básico a intermedio
**Antes de este tema:** `01_fundamentos/04_funciones`
**Después de este tema:** `01_fundamentos/06_colecciones_y_fechas`

## Objetivos

- Recorrer listas, textos, diccionarios y rangos con `for`.
- Repetir mientras se cumpla una condición con `while`.
- Controlar el ciclo con `break`, `continue` y salidas anticipadas con `return`.
- Usar acumuladores y contadores.
- Recorrer varias listas a la vez con `zip` y numerar con `enumerate`.
- Escribir ciclos anidados y reconocer los errores típicos (límites,
  modificar una lista mientras se recorre, listas repetidas con `*`).

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| `range` | `range(1, 11)` va de 1 a 10; `range(10, 0, -1)` cuenta hacia atrás |
| Acumulador | `total = 0` antes del ciclo y `total += n` dentro |
| `while` | `while intentos < 5:` |
| `break` / `continue` | Salir del ciclo / saltar a la siguiente vuelta |
| `enumerate` | `for i, x in enumerate(lista, start=1):` |
| `zip` | `for nombre, nota in zip(nombres, notas):` |
| Ciclos anidados | `for i ...: for j in range(i + 1, n):` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 10 | `for` sobre listas, textos, diccionarios, conjuntos y `range` |
| 11 - 21 | `enumerate` y `zip` |
| 22 - 33 | `while`: contadores, `break`, `continue`, `else`, menús |
| 34 - 45 | Llenar y procesar colecciones con ciclos |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Tabla de multiplicar | Básico | `for`, `range`, construir listas |
| 02 | Acumuladores y contadores | Básico | `range` con paso, recorrer textos |
| 03 | Adivinar el número | Intermedio | `while` con condición compuesta |
| 04 | Números primos | Intermedio | Salida anticipada, ciclos que llaman funciones |
| 05 | Boletín de notas | Avanzado | `zip`, `enumerate`, validación |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Cuenta regresiva | Básico | 2 | `range` hacia atrás, indentación |
| 02 | Promedio de una lista | Básico | 2 | Acumulador reiniciado, `return` dentro del ciclo |
| 03 | Número mayor | Intermedio | 2 | Valor inicial, error de uno |
| 04 | Quitar pares y buscar | Intermedio | 3 | Modificar la lista al recorrerla, efectos secundarios, `else` mal ubicado |
| 05 | Ciclos anidados | Avanzado | 3 | Rango interno, `append` contra `extend`, listas repetidas con `*` |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

Si un programa se queda "pegado", probablemente hay un ciclo infinito:
detenlo con el botón de parar de PyCharm o con Ctrl + C.
