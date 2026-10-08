# Errores y excepciones

**Nivel:** intermedio
**Antes de este tema:** `01_fundamentos/06_colecciones_y_fechas`
**Después de este tema:** `01_fundamentos/08_modulos_y_paquetes`

## Objetivos

- Leer un mensaje de error de Python y ubicar la línea y el tipo de error.
- Atrapar errores con `try` / `except` usando el tipo exacto.
- Usar `else` y `finally` y entender en qué orden se ejecutan.
- Lanzar errores propios con `raise` y mensajes claros.
- Crear excepciones personalizadas.
- Trabajar con archivos de forma segura con `with`.

## Conceptos clave

| Error | Cuándo aparece |
|---|---|
| `SyntaxError` | El código está mal escrito; no llega a ejecutarse |
| `NameError` | Se usa un nombre que no existe |
| `TypeError` | Se opera con tipos incompatibles (`"a" + 1`) |
| `ValueError` | El tipo es correcto pero el valor no (`int("abc")`) |
| `IndexError` / `KeyError` | Posición o clave inexistente |
| `ZeroDivisionError` | División entre cero |
| `FileNotFoundError` | El archivo no existe |

| Bloque | Se ejecuta |
|---|---|
| `try` | Siempre, hasta que ocurra un error |
| `except Tipo` | Solo si ocurrió ese tipo de error |
| `else` | Solo si no hubo error |
| `finally` | Siempre, al final |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 05 | Un error de cada tipo, con la versión que falla y la corregida |
| 06 - 08 | Varias excepciones, división segura, archivo no encontrado |
| 09 - 10 | Prácticas: entrada numérica, `try-else-finally` |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Conversiones seguras | Básico | `try` / `except` con tipo exacto |
| 02 | Validar edad | Básico | `raise` con mensajes claros |
| 03 | try, except, else y finally | Intermedio | Flujo completo de un `try` |
| 04 | Excepción personalizada | Intermedio | Clases de excepción, varios `except` |
| 05 | Promedio desde un archivo | Avanzado | Archivos, errores dentro de un ciclo |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Convertir número | Básico | 2 | `try` sin `except`, tipo de excepción equivocado |
| 02 | División con mensajes | Básico | 2 | Código fuera de `else`, orden de los `except` |
| 03 | Lanzar y reportar | Intermedio | 2 | `raise` de un texto, objeto de error contra mensaje |
| 04 | Guardar y contar líneas | Intermedio | 3 | Modo de apertura, saltos de línea, nombre de excepción |
| 05 | Procesar pedidos | Avanzado | 3 | Silenciar errores, `except A or B`, validar antes de modificar |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

Lee el mensaje de error de abajo hacia arriba: la última línea dice el tipo
de error y las anteriores muestran en qué línea ocurrió.
