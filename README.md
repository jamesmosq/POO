# Programación en Python: de los fundamentos a la POO y las bases de datos

Material del curso organizado por temas y en orden de dificultad. Cada tema
tiene ejemplos, ejercicios propuestos, ejercicios para corregir y sus
soluciones.

## Ruta de aprendizaje

| Bloque | Tema | Nivel |
|---|---|---|
| **01 Fundamentos** | `01_variables_y_tipos` | Básico |
| | `02_operadores` | Básico |
| | `03_condicionales` | Básico |
| | `04_funciones` | Básico a intermedio |
| | `05_bucles` | Básico a intermedio |
| | `06_colecciones_y_fechas` | Básico a intermedio |
| | `07_errores_y_excepciones` | Intermedio |
| | `08_modulos_y_paquetes` | Intermedio |
| **02 Estructuras de datos** | `01_busqueda_y_ordenamiento` | Intermedio |
| | `02_pilas` | Intermedio |
| | `03_colas` | Intermedio |
| **03 Programación orientada a objetos** | `01_clases_y_objetos` | Intermedio |
| | `02_encapsulamiento` | Intermedio |
| | `03_herencia` | Intermedio |
| | `04_polimorfismo` | Intermedio |
| | `05_abstraccion` | Intermedio a avanzado |
| | `06_metodos_magicos` | Avanzado |
| **04 Interfaces gráficas (Tkinter)** | `01_ventanas_y_widgets` | Intermedio |
| | `02_gestores_de_geometria` | Intermedio |
| | `03_gui_con_poo` | Avanzado |
| **05 Bases de datos (MySQL, Northwind)** | `01_conexion_y_consultas` | Intermedio |
| | `02_crud_con_poo` | Avanzado |
| | `03_procedimientos_almacenados` | Avanzado |
| | `04_crud_con_interfaz` | Avanzado |
| | `05_seguridad_de_contrasenas` | Avanzado |

`evaluaciones/` contiene las evaluaciones del primer semestre.

## Estructura de cada tema

```
NN_tema/
    README.md                   objetivos, conceptos clave y lista de ejercicios
    ejemplos/                   código explicado para estudiar
    ejercicios_propuestos/      5 ejercicios para resolver desde cero
    ejercicios_para_corregir/   5 programas con errores para encontrar y arreglar
    soluciones/
        propuestos/
        para_corregir/          cada arreglo explicado con su porqué
```

Los ejercicios van de básico a avanzado dentro de cada tema.

## Cómo trabajar un ejercicio

1. Lee el enunciado completo (el texto al inicio del archivo).
2. Escribe tu solución o corrige el código.
3. Ejecuta el archivo. Al final de cada ejercicio hay pruebas automáticas:
   si algo falla, el mensaje te dice qué se esperaba.
4. Cuando veas `Todas las pruebas pasaron`, compara con la solución.

Reglas:

- No modifiques las pruebas: son la especificación de lo que se pide.
- En los ejercicios para corregir, el encabezado dice cuántos errores hay.
  Corrige uno a la vez y vuelve a ejecutar.
- Mira la solución solo después de intentarlo. Leer código ajeno y
  encontrar sus errores es tan importante como escribir el propio.

## Requisitos

- Python 3.10 o superior (se usa `match-case`).
- Para el bloque 05: MySQL o MariaDB con la base Northwind, y los paquetes
  `mysql-connector-python` y `bcrypt`. Ver `05_bases_de_datos/README.md`.

## Para el docente: verificar los ejercicios

`herramientas/verificar_ejercicios.py` comprueba que cada solución pase sus
pruebas, que cada ejercicio sin resolver falle y que ningún ejercicio quede
sin solución:

```
python herramientas/verificar_ejercicios.py              # todos los temas
python herramientas/verificar_ejercicios.py 03_poo       # solo un bloque
```

Para el bloque 05, define antes las variables de la conexión (por ejemplo
`DB_PASSWORD` y `DB_NAME`) y ejecútalo con el intérprete que tenga
`mysql-connector-python`. Conviene usar una copia de Northwind solo para
verificar.
