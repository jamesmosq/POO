# Ventanas y widgets (Tkinter)

**Nivel:** intermedio
**Antes de este tema:** `03_poo/06_metodos_magicos`
**Después de este tema:** `04_interfaces_graficas/02_gestores_de_geometria`

## Objetivos

- Crear una ventana con `tk.Tk()` y configurar su título y tamaño.
- Usar los widgets principales: `Label`, `Button`, `Entry`, `Text`,
  `Checkbutton`, `Radiobutton`, `Listbox`, `Combobox`, `Scrollbar`,
  `Treeview`, `Notebook`, `messagebox`.
- Responder a eventos: `command` en los botones y `bind` para el teclado.
- Leer y actualizar widgets: `get()`, `insert()`, `delete()`, `config()`.
- Usar variables de control (`StringVar`, `BooleanVar`, `IntVar`).

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Ventana principal | `raiz = tk.Tk()` ... `raiz.mainloop()` al final |
| Mostrar un widget | Crear + ubicar: `tk.Label(raiz).pack()` |
| Evento de botón | `command=self.guardar` (sin paréntesis) |
| Lambda en un ciclo | `command=lambda t=texto: self.presionar(t)` |
| Leer un Entry | `self.entrada.get()` dentro del método del evento |
| Cambiar un Label | `self.etiqueta.config(text="...")` |
| Variable de control | `tk.BooleanVar()` conectada con `variable=` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 05 | Ventana principal, Label, Button, Entry y Entry con ttk |
| 06 - 10 | Text, Checkbutton, Radiobutton, Listbox, Menu |
| 11 - 16 | Messagebox, Combobox, Frame, Scrollbar, Treeview |
| 17 - 19 | Pestañas con Notebook, Treeview en pestañas, ventana de ejemplo |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Saludo | Básico | Entry, Button, Label, `config` |
| 02 | Conversor de temperatura | Básico | Validar datos, evento de teclado |
| 03 | Formulario de registro | Intermedio | Combobox, Checkbutton, variables de control |
| 04 | Lista de tareas | Intermedio | Listbox, selección, Scrollbar |
| 05 | Calculadora | Avanzado | `grid`, widgets creados en ciclos, estado |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Botón que no responde | Básico | 2 | Widget sin ubicar, `command` con paréntesis |
| 02 | Conversor que no lee | Básico | 2 | Atributo en lugar de `config`, leer en el momento equivocado |
| 03 | Formulario con opciones | Intermedio | 2 | Método sin llamar, Checkbutton sin variable |
| 04 | Lista de tareas | Intermedio | 3 | `delete` incompleto, selección vacía, vista sin actualizar |
| 05 | Teclado numérico | Avanzado | 3 | Lambdas en un ciclo, posición en `grid`, sumar texto |

## Cómo trabajar los ejercicios

Los ejercicios se prueban sin abrir la ventana: las pruebas escriben en los
campos y hacen clic con `invoke()`. Cuando todas pasan, se abre la ventana
para que la uses. Por eso los widgets deben guardarse en atributos con el
nombre exacto que pide el enunciado (`self.entrada`, `self.boton`, ...).

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.
