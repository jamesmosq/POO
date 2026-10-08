# CRUD con POO

**Nivel:** avanzado
**Antes de este tema:** `05_bases_de_datos/01_conexion_y_consultas`
**Después de este tema:** `05_bases_de_datos/03_procedimientos_almacenados`

## Objetivos

- Encapsular la conexión en una clase que se usa con `with`.
- Implementar las operaciones CRUD (crear, leer, actualizar, eliminar) en
  un repositorio, sin repartir SQL por todo el programa.
- Representar filas como objetos (entidades con `@dataclass`).
- Confirmar cambios con `commit()` y deshacerlos con `rollback()`.
- Usar transacciones para operaciones que tocan varias tablas.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Commit | Sin `con.commit()`, los cambios no quedan guardados |
| Id generado | `cursor.lastrowid` (del cursor, no de la conexión) |
| Filas afectadas | `cursor.rowcount`; léelo antes de cerrar el cursor |
| Repositorio | Clase con `crear`, `obtener`, `listar`, `actualizar`, `eliminar` |
| Entidad | `@dataclass class Categoria:` |
| Transacción | Varios cambios, un solo `commit()` al final, `rollback()` si algo falla |
| `__exit__` | Cierra recursos; no debe retornar `True` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 | Probar la conexión con una clase |
| 02 - 06 | CRUD de empleados en Northwind: crear, leer, buscar, actualizar, eliminar |
| 07 | CRUD completo con menú |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Clase BaseDeDatos | Básico | Encapsular la conexión, `with`, `commit` |
| 02 | Repositorio de transportadoras | Intermedio | CRUD completo, `rowcount` |
| 03 | Entidad y repositorio | Intermedio | `@dataclass`, mapear filas a objetos |
| 04 | Transacciones | Avanzado | Pedido con detalles, `commit` y `rollback` |
| 05 | Reporte de ventas | Avanzado | Agregaciones con expresiones, exportar a CSV |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Conexión olvidada | Básico | 2 | Atributo sin `self`, `commit` faltante |
| 02 | Crear transportadora | Básico | 2 | Texto pegado en el SQL, `lastrowid` |
| 03 | Obtener y eliminar | Intermedio | 2 | Tupla contra diccionario, `rowcount` |
| 04 | Base de datos con with | Intermedio | 3 | `__exit__` que esconde errores, orden de parámetros, orden del resultado |
| 05 | Pedido a medias | Avanzado | 3 | `commit` antes de tiempo, `rollback` faltante, id equivocado |

## Cómo trabajar los ejercicios

Las pruebas de este tema escriben en la base de datos. Usan transportadoras
y categorías cuyo nombre empieza por `PRUEBA_EJ_` y pedidos con fecha
1999-09-09, y los borran al terminar, aunque la prueba falle. Tus datos de
Northwind no se modifican.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.
