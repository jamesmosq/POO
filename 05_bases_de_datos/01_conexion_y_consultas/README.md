# Conexión y consultas

**Nivel:** intermedio
**Antes de este tema:** `04_interfaces_graficas/03_gui_con_poo`
**Después de este tema:** `05_bases_de_datos/02_crud_con_poo`

Antes de empezar, prepara la base de datos siguiendo `05_bases_de_datos/README.md`.

## Objetivos

- Conectarse a MySQL o MariaDB desde Python con `mysql.connector`.
- Ejecutar consultas con un cursor y leer los resultados (`fetchone`,
  `fetchall`).
- Pasar datos a las consultas con parámetros `%s`, nunca pegándolos en el
  texto SQL.
- Consultar varias tablas con `JOIN` y resumir datos con `GROUP BY`,
  `COUNT` y `SUM`.
- Obtener resultados como diccionarios y cerrar siempre los cursores.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Conectar | `con = mysql.connector.connect(**CONFIG)` |
| Cursor | `with closing(con.cursor()) as cursor:` |
| Ejecutar con parámetros | `cursor.execute("... WHERE Country = %s", (pais,))` |
| Una fila | `cursor.fetchone()` (retorna una tupla o `None`) |
| Todas las filas | `cursor.fetchall()` (lista de tuplas) |
| Filas como diccionarios | `con.cursor(dictionary=True)` |
| LIKE con parámetros | El valor lleva los comodines: `(f"%{texto}%",)` |
| Error "Unread result found" | Quedaron filas sin leer; usa `fetchall()` o `cursor(buffered=True)` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 05 | Conexión y operaciones básicas: SELECT, INSERT, UPDATE, DELETE |
| 06 - 07 | Consultas mostradas con `tabulate` |
| 08 | Llamar un procedimiento almacenado |
| 09 | Conexión configurada con variables de entorno |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Probar la conexión | Básico | Conectar, cursor, validar nombres de tabla |
| 02 | Consultas simples | Básico | WHERE, ORDER BY, LIMIT, DISTINCT con parámetros |
| 03 | Búsquedas parametrizadas | Intermedio | LIKE, BETWEEN, inyección SQL |
| 04 | JOIN y agregaciones | Intermedio | INNER JOIN, LEFT JOIN, GROUP BY |
| 05 | Resultados como diccionarios | Avanzado | `dictionary=True`, alias, COALESCE |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Contar productos | Básico | 2 | Nombre del módulo, `fetchall` contra `fetchone()[0]` |
| 02 | Clientes por país | Básico | 2 | Texto pegado en el SQL, orden |
| 03 | Buscar productos | Intermedio | 2 | Tupla de un elemento, comodines de LIKE |
| 04 | Ventas por categoría | Intermedio | 3 | Columna del JOIN, COUNT contra SUM, orden |
| 05 | Ficha de producto | Avanzado | 3 | Tuplas contra diccionarios, `None`, `rowcount` en un SELECT |

## Cómo trabajar los ejercicios

Las pruebas calculan el resultado esperado con su propia consulta a tu
base de datos, así que funcionan aunque tus datos de Northwind tengan
pequeñas diferencias.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.
