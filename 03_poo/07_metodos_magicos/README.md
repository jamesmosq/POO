# Métodos mágicos

**Nivel:** avanzado
**Antes de este tema:** `03_poo/06_abstraccion`
**Después de este tema:** `04_interfaces_graficas/01_ventanas_y_widgets`

## Objetivos

- Controlar cómo se muestra un objeto con `__str__` y `__repr__`.
- Definir la igualdad y el orden entre objetos (`__eq__`, `__lt__`,
  `functools.total_ordering`).
- Entender la relación entre `__eq__` y `__hash__`.
- Sobrecargar operadores aritméticos (`__add__`, `__mul__`, `__radd__`,
  `__rmul__`).
- Hacer que un objeto se comporte como un contenedor (`__len__`,
  `__getitem__`, `__contains__`, `__iter__`, `__bool__`).

## Conceptos clave

| Método | Se usa con |
|---|---|
| `__str__` / `__repr__` | `print(x)`, `str(x)` / `repr(x)`, consola, listas |
| `__eq__` / `__lt__` | `==` / `<` (y con `total_ordering`, el resto) |
| `__hash__` | `set`, claves de diccionario |
| `__add__` / `__radd__` | `a + b` / `0 + a` (por ejemplo, en `sum()`) |
| `__mul__` / `__rmul__` | `a * 3` / `3 * a` |
| `__len__`, `__getitem__` | `len(x)`, `x[0]`, `x[1:3]` |
| `__contains__`, `__iter__` | `elemento in x`, `for e in x` |
| `__bool__` | `if x:` |
| `NotImplemented` | Retorno que significa "no sé operar con ese tipo" |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 | Una lista propia con varios métodos mágicos |
| 02 - 06 | Un método por ejemplo: `__init__`, `__str__`, `__len__`, `__add__`, `__getitem__` |
| 07 | Lista propia completa con comparación y acceso por índice |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | `__str__`, `__repr__` y `__eq__` | Básico | Representación e igualdad |
| 02 | Vector con operadores | Intermedio | Sobrecarga de operadores, `__rmul__` |
| 03 | Playlist como contenedor | Intermedio | Protocolo de contenedores |
| 04 | Versiones comparables | Intermedio | `total_ordering`, `__hash__` |
| 05 | Dinero | Avanzado | `Decimal`, `__radd__`, objetos de valor |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Libro con `__str__` | Básico | 2 | Tipo de retorno, nombre del método |
| 02 | Suma de vectores | Básico | 2 | `__eq__` faltante, operador que modifica el objeto |
| 03 | Inventario como contenedor | Intermedio | 2 | `__len__` con texto, `__iter__` sin iterador |
| 04 | Versiones | Intermedio | 3 | `__hash__`, comparar textos, `NotImplemented` |
| 05 | Dinero | Avanzado | 3 | `Decimal` desde float, `__radd__`, tipo de retorno |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
