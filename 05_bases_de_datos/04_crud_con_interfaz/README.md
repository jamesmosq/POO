# CRUD con interfaz gráfica

**Nivel:** avanzado
**Antes de este tema:** `05_bases_de_datos/03_procedimientos_almacenados`
**Después de este tema:** `05_bases_de_datos/05_seguridad_de_contrasenas`

## Objetivos

- Mostrar datos de Northwind en widgets de Tkinter (Treeview, Listbox,
  Combobox).
- Filtrar desde la interfaz con consultas parametrizadas.
- Separar lo que ve el usuario (nombres) de lo que usa la base de datos
  (ids).
- Construir un CRUD completo con interfaz, donde la base de datos es la
  fuente de verdad.
- Armar pantallas maestro-detalle.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Llenar un Treeview | Vaciar con `delete(*get_children())` y luego `insert` fila por fila |
| Id de la fila | `insert("", tk.END, iid=str(id), values=(...))` |
| Combobox con ids | `values=[nombres]` y un diccionario `nombre -> id` |
| Eventos | `<<ComboboxSelected>>`, `<<TreeviewSelect>>` |
| Fuente de verdad | Modificar la base de datos y después recargar la vista |
| Fechas | `fecha.strftime("%Y-%m-%d")` para mostrarlas sin hora |
| Comparar el estado de ttk | `str(combobox.cget("state")) == "readonly"` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 03 | Buscar, ver detalle y eliminar empleados con interfaz |
| 04 | CRUD de empleados con imágenes y calendario (usa `tkcalendar`) |
| 05 | Empleados con imagen |
| 06 - 08 | Formularios de Northwind en pestañas y con menú |
| `img/`, `img_muestra/` | Imágenes que usan los ejemplos |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Listar productos | Básico | Llenar y recargar un Treeview |
| 02 | Buscar con filtro | Intermedio | Filtro con LIKE, JOIN, tecla Enter |
| 03 | Combobox de categorías | Intermedio | Nombres en pantalla, ids en la consulta |
| 04 | CRUD de transportadoras | Avanzado | CRUD completo contra la base de datos |
| 05 | Maestro y detalle | Avanzado | Cliente, pedidos y productos encadenados |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Tabla que se duplica | Básico | 2 | Usar un widget antes de crearlo, no vaciar al recargar |
| 02 | Buscador desfasado | Básico | 2 | Método sin llamar, contador actualizado antes de tiempo |
| 03 | Combobox con ids | Intermedio | 2 | Tuplas en el Combobox, lista sin vaciar |
| 04 | CRUD que no guarda | Intermedio | 3 | Vista sin recargar, tupla de selección, borrar solo en pantalla |
| 05 | Detalle de pedido | Avanzado | 3 | Formato de fecha, total mal calculado, detalle sin limpiar |

## Cómo trabajar los ejercicios

Las pruebas usan la ventana oculta y revisan tanto la interfaz como la base
de datos. Cuando pasan, se abre la ventana real conectada a tu Northwind.
Los ejercicios que escriben datos usan nombres que empiezan por
`PRUEBA_EJ_` y los borran al terminar.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.
