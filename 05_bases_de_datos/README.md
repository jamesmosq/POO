# Bases de datos con Python (Northwind)

**Nivel:** avanzado
**Antes de este bloque:** `04_interfaces_graficas`

Todo el bloque trabaja con la base de datos de ejemplo **Northwind** en
MySQL o MariaDB.

## 1. Preparar la base de datos

En la carpeta `sql/` hay tres scripts:

| Script | Qué crea |
|---|---|
| `northwind_procedimientos_almacenados.sql` | Base `Northwindx` con todas las tablas, **los datos** y los procedimientos almacenados de los ejemplos |
| `northwind_basico.sql` | Solo las tablas de Northwind, sin datos |
| `northwind_mejorado.sql` | Base `NorthwindMejorado`, una versión ampliada (más columnas, vistas) |

Los ejercicios necesitan las tablas **con datos**:

- **Si ya tienes una base `northwind` con datos** (la que se usa en clase),
  no necesitas hacer nada: los ejercicios se conectan a ella por defecto.
- **Si no la tienes**, abre `northwind_procedimientos_almacenados.sql` en
  Workbench, HeidiSQL o la consola de MySQL y ejecútalo TAL CUAL. Crea la
  base `Northwindx`; luego indica ese nombre en la conexión
  (`DB_NAME=northwindx`, ver el paso 2).

Cuidado: el script BORRA y vuelve a crear las tablas de la base que indica
(`DROP TABLE IF EXISTS ...`). No le cambies el nombre de la base por el de
una base que tenga datos que quieras conservar.

## 2. Configurar la conexión

Cada ejercicio tiene al inicio un diccionario `CONFIG`:

```python
CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "northwind"),
}
```

Tienes dos opciones:

- **Variables de entorno (recomendado):** en PyCharm, `Run > Edit
  Configurations > Environment variables`, agrega por ejemplo
  `DB_PASSWORD=tu_clave`. Así la contraseña no queda escrita en el código.
- **Cambiar el valor por defecto** en el archivo (por ejemplo
  `os.getenv("DB_PASSWORD", "tu_clave")`). Es más rápido, pero no subas
  ese archivo a un repositorio público.

## 3. Instalar los paquetes

```
pip install mysql-connector-python bcrypt
```

Los ejercicios funcionan con versiones antiguas y nuevas del conector,
porque usan `with closing(con.cursor()) as cursor:`. El paquete
`mysql-connector` (sin `-python`) está descontinuado; si lo tienes
instalado, conviene reemplazarlo:

```
pip uninstall mysql-connector
pip install mysql-connector-python
```

## Temas

| Carpeta | Tema | Nivel |
|---|---|---|
| `01_conexion_y_consultas` | Conexión, SELECT con parámetros, JOIN, agregaciones | Intermedio |
| `02_crud_con_poo` | Clase de conexión, repositorios, entidades, transacciones | Avanzado |
| `03_procedimientos_almacenados` | `callproc`, parámetros OUT, `SIGNAL` | Avanzado |
| `04_crud_con_interfaz` | Tkinter + MySQL: listas, filtros, CRUD, maestro-detalle | Avanzado |
| `05_seguridad_de_contrasenas` | bcrypt, inicio de sesión, inyección SQL | Avanzado |

## Qué modifican los ejercicios en tu base de datos

Los ejercicios que escriben datos limpian lo que crean, aunque fallen:

- Transportadoras y categorías con nombres que empiezan por `PRUEBA_EJ_`.
- Pedidos con fecha 1999-09-09.
- Procedimientos almacenados con prefijo `ej_` (quedan creados; se pueden
  borrar con `DROP PROCEDURE`).
- La tabla `ej_usuarios` del tema de seguridad (queda creada, sin filas).
- El ejercicio 05 de procedimientos cambia el precio de un producto y lo
  restaura al terminar.
