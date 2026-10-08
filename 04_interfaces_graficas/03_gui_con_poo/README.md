# Interfaces gráficas con POO

**Nivel:** avanzado
**Antes de este tema:** `04_interfaces_graficas/02_gestores_de_geometria`
**Después de este tema:** `05_bases_de_datos/01_conexion_y_consultas`

## Objetivos

- Construir cada parte de la interfaz como una clase que hereda de
  `tk.Frame`.
- Separar la lógica del negocio (clases sin Tkinter) de la vista.
- Reutilizar estructura con herencia (formularios base y formularios
  específicos).
- Implementar un CRUD en memoria con `ttk.Treeview`, manteniendo la vista
  y los datos sincronizados.
- Comunicar componentes a través de un modelo compartido (patrón
  observador).

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Componente | `class Panel(tk.Frame):` con `super().__init__(master)` |
| Variable de control | `tk.IntVar` + `textvariable=`; se cambia con `set()` |
| Lógica separada | `Carrito` no importa Tkinter; `VistaCarrito` lo usa |
| Treeview | `insert("", tk.END, values=(a, b))`, `selection()`, `item()`, `delete()` |
| Evento de selección | `tabla.bind("<<TreeviewSelect>>", ...)` |
| Observador | El modelo guarda funciones y las llama en cada cambio |
| Pestañas | `ttk.Notebook` con un `Frame` por pestaña |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 04 | Ventanas como clases, lista de compras, frames con clase, tipos de botones |
| 05 - 08 | Botones y entradas, formularios organizados por secciones |
| 09 - 10 | Treeview con botones, demostración de widgets |
| 11 - 12 | Herencia de ventanas y formularios con herencia |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Contador como Frame | Básico | Heredar de `tk.Frame`, `IntVar` |
| 02 | Lógica separada de la vista | Intermedio | Separar responsabilidades, Treeview |
| 03 | Herencia de formularios | Intermedio | Formulario base, validaciones con `super()` |
| 04 | CRUD con Treeview | Avanzado | Crear, leer, actualizar, eliminar |
| 05 | Pestañas con modelo compartido | Avanzado | Patrón observador, Notebook |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Frame sin iniciar | Básico | 2 | `super().__init__` faltante, Frame sin ubicar |
| 02 | Contador quieto | Básico | 2 | `self.` faltante, `get` sin `set` |
| 03 | Formularios heredados | Intermedio | 2 | Sobrescribir sin `super()`, ignorar el resultado del padre |
| 04 | CRUD desincronizado | Intermedio | 3 | `values` como texto, `selection()` es una tupla, borrar en un solo lugar |
| 05 | Observador roto | Avanzado | 3 | Suscribir el resultado, no notificar, no limpiar antes de redibujar |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, se abre la ventana y puedes
   comparar con `soluciones/`.

El ejercicio 04 propuesto es la base del tema siguiente: en
`05_bases_de_datos` el mismo CRUD guarda los datos en MySQL.
