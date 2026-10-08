# Colecciones y fechas

**Nivel:** básico a intermedio
**Antes de este tema:** `01_fundamentos/05_bucles`
**Después de este tema:** `01_fundamentos/07_errores_y_excepciones`

## Objetivos

- Elegir la colección adecuada: lista, tupla, diccionario o conjunto.
- Agregar, buscar, modificar y eliminar elementos en cada colección.
- Entender la diferencia entre copiar una colección y tener dos nombres
  para la misma.
- Representar matrices como listas de listas.
- Trabajar con fechas: crear, restar, formatear, leer desde texto y
  calcular días hábiles.

## Conceptos clave

| Colección | Se escribe | Características |
|---|---|---|
| Lista | `[1, 2, 3]` | Ordenada, modificable, admite repetidos |
| Tupla | `(1, 2)` | Ordenada, NO modificable |
| Diccionario | `{"clave": valor}` | Clave -> valor; `get`, `items`, `setdefault` |
| Conjunto | `{1, 2}` o `set()` | Sin repetidos; `&`, `\|`, `-` |

| Fechas | Ejemplo |
|---|---|
| Crear | `date(2026, 10, 8)` |
| Diferencia | `(fecha2 - fecha1).days` |
| Sumar | `fecha + timedelta(days=3)` |
| Texto a fecha | `datetime.strptime("08/10/2026", "%d/%m/%Y")` |
| Fecha a texto | `fecha.strftime("%d/%m/%Y")` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 | Tuplas |
| 02 - 03 | Matrices con listas y con NumPy |
| 04 - 17 | Fechas: crear, diferencias, formato, componentes, días de la semana, idioma, ventana |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Lista de compras | Básico | Métodos de listas, `sorted`, slicing |
| 02 | Inventario con diccionario | Básico | `get`, `items`, `values`, validar antes de modificar |
| 03 | Conjuntos | Intermedio | Unión, intersección, diferencia |
| 04 | Matrices | Intermedio | Listas anidadas, validar dimensiones |
| 05 | Fechas | Avanzado | Edad, días restantes, formato, días hábiles |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Tuplas e índices | Básico | 2 | Inmutabilidad, índice fuera de rango |
| 02 | Lista de precios | Básico | 2 | `KeyError`, recorrer un diccionario |
| 03 | Copias y conjuntos | Intermedio | 2 | Alias en lugar de copia, `{}` contra `set()` |
| 04 | Edad con fechas | Intermedio | 3 | Formato de fecha, `days`, cálculo de edad |
| 05 | Agenda telefónica | Avanzado | 3 | `setdefault`, ordenar con clave, borrar al recorrer |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
