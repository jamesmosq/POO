# Gestores de geometría: pack, grid y place

**Nivel:** intermedio
**Antes de este tema:** `04_interfaces_graficas/01_ventanas_y_widgets`
**Después de este tema:** `04_interfaces_graficas/03_gui_con_poo`

## Objetivos

- Ubicar widgets con los tres gestores de Tkinter y saber cuándo usar
  cada uno.
- Controlar cómo crecen los widgets al cambiar el tamaño de la ventana
  (`fill`, `expand`, `weight`, `sticky`).
- Organizar interfaces con `Frame` como contenedores.
- Dibujar en un `Canvas` y manejar sus elementos con tags.

## Conceptos clave

| Gestor | Cuándo usarlo | Opciones clave |
|---|---|---|
| `pack` | Apilar en una dirección: barras, columnas simples | `side`, `fill`, `expand`, `padx`, `pady` |
| `grid` | Formularios y cuadrículas | `row`, `column`, `sticky`, `columnspan`, `rowspan` |
| `place` | Posiciones exactas o superpuestas | `relx`, `rely`, `x`, `y`, `anchor` |

Reglas importantes:

- No mezclar `pack` y `grid` dentro del MISMO contenedor.
- Con `pack`, el orden importa: los bordes primero y lo que se expande al
  final.
- Para que una fila o columna de `grid` crezca:
  `contenedor.columnconfigure(i, weight=1)`.

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 02 | `pack` y sus opciones |
| 03 | `grid` |
| 04 | `place` |
| 05 | Colores en Tkinter |
| 06 | Dibujo con `turtle` |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Franjas con pack | Básico | `side`, `fill`, `expand` |
| 02 | Formulario con grid | Básico | Filas, columnas, `sticky`, `columnspan` |
| 03 | Estructura de una aplicación | Intermedio | Frames, orden de empaquetado |
| 04 | Teclado con grid | Intermedio | Posiciones calculadas, `weight` |
| 05 | place y Canvas | Avanzado | Coordenadas relativas, dibujo, tags |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Mezclar gestores | Básico | 2 | `pack` y `grid` juntos, `fill` faltante |
| 02 | Login con grid | Básico | 2 | Celda repetida, `columnspan` |
| 03 | Estructura desordenada | Intermedio | 2 | `side` equivocado, orden de empaquetado |
| 04 | Teclado que no crece | Intermedio | 3 | Opción mal escrita, desplazamiento de filas, `weight` incompleto |
| 05 | Tablero con place | Avanzado | 3 | Valor de `anchor`, coordenadas del óvalo, borrar por tag |

## Cómo trabajar los ejercicios

Las pruebas revisan dónde quedó cada widget con `pack_info()`,
`grid_info()` y `place_info()`. Esos mismos métodos te sirven para
depurar: imprímelos cuando algo no se vea donde esperas.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, se abre la ventana y puedes
   comparar con `soluciones/`.
