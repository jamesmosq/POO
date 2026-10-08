# Procedimientos almacenados

**Nivel:** avanzado
**Antes de este tema:** `05_bases_de_datos/02_crud_con_poo`
**Después de este tema:** `05_bases_de_datos/04_crud_con_interfaz`

## Objetivos

- Llamar procedimientos almacenados desde Python con `callproc`.
- Leer sus resultados con `stored_results()`, incluso cuando retornan
  varios conjuntos de filas.
- Crear procedimientos desde Python (sin `DELIMITER`).
- Usar parámetros `IN` y `OUT`.
- Validar dentro del procedimiento con `SIGNAL` y traducir esos errores a
  excepciones de Python.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Llamar | `cursor.callproc("nombre", [arg1, arg2])` |
| Leer filas | `for r in cursor.stored_results(): r.fetchall()` |
| Parámetros OUT | `resultado = cursor.callproc(...)`; los OUT están en `resultado` |
| Crear | `cursor.execute("DROP PROCEDURE IF EXISTS ...")` y luego `CREATE PROCEDURE ...` |
| `DELIMITER` | Solo existe en la consola y en Workbench; desde Python no se usa |
| Validar | `SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '...'` |
| Error recibido | `error.sqlstate == "45000"`, `error.msg` es el mensaje (`errno` vale 1644) |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 05 | Leer, buscar, crear, actualizar y eliminar llamando procedimientos |

Los procedimientos de los ejemplos están en
`05_bases_de_datos/sql/northwind_procedimientos_almacenados.sql`.

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Llamar un procedimiento | Básico | `callproc`, `stored_results` |
| 02 | Procedimiento de búsqueda | Básico | Varios resultados en una llamada |
| 03 | Crear un procedimiento | Intermedio | `CREATE PROCEDURE` desde Python, `DROP IF EXISTS` |
| 04 | Parámetros de salida | Intermedio | `OUT`, `SELECT ... INTO`, valores `NULL` |
| 05 | Validar dentro del procedimiento | Avanzado | `SIGNAL`, excepciones propias |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Llamada mal hecha | Básico | 2 | `execute` contra `callproc`, dónde quedan los resultados |
| 02 | Resultados de búsqueda | Básico | 2 | Argumentos como lista, filas contra valores |
| 03 | Crear desde Python | Intermedio | 2 | `DELIMITER`, procedimiento que ya existe |
| 04 | Valores de salida | Intermedio | 3 | Lista enviada contra tupla retornada, posiciones, orden del `INTO` |
| 05 | Errores del procedimiento | Avanzado | 3 | `errno` contra `sqlstate`, excepciones cruzadas, `commit` |

## Cómo trabajar los ejercicios

Cada ejercicio crea en tu base de datos los procedimientos que necesita,
todos con el prefijo `ej_` para no tocar los que ya tengas. Puedes
borrarlos cuando termines con `DROP PROCEDURE ej_...`.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.
