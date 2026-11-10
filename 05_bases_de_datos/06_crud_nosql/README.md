# CRUD con NoSQL (MongoDB + Tkinter)

**Nivel:** avanzado
**Antes de este tema:** `05_bases_de_datos/05_seguridad_de_contrasenas`
**Después de este tema:** fin de la ruta.

Hasta ahora todo el bloque trabajó con MySQL. En este tema se construye el
mismo tipo de CRUD, paso a paso, con **MongoDB**, una base de datos NoSQL,
y al final se le pone una interfaz con Tkinter.

## Objetivos

- Entender qué cambia entre una base relacional y una de documentos.
- Instalar MongoDB y conectarse desde Python con `pymongo`.
- Hacer las cuatro operaciones del CRUD: `insert_one`, `find`,
  `update_one` y `delete_one`.
- Escribir filtros con operadores (`$gt`, `$in`, `$regex`, ...) y
  actualizar con operadores (`$set`, `$inc`, `$addToSet`, ...).
- Manejar el `_id` (un `ObjectId`) y convertirlo a texto y de vuelta.
- Organizar el acceso a datos en un repositorio y conectarlo a una
  interfaz con Treeview.

## SQL y MongoDB lado a lado

| MySQL | MongoDB |
|---|---|
| Base de datos | Base de datos |
| Tabla | Colección |
| Fila | Documento (en Python, un diccionario) |
| Columna | Campo |
| `PRIMARY KEY` autoincremental | `_id`, un `ObjectId` que se genera solo |
| `CREATE TABLE` con columnas fijas | No hace falta: la colección se crea al insertar y cada documento puede tener campos distintos |
| Tabla aparte para una lista (etiquetas de un producto) | Un campo que guarda una lista: `"etiquetas": ["usb", "gamer"]` |
| `INSERT` | `insert_one(documento)` / `insert_many(lista)` |
| `SELECT ... WHERE` | `find(filtro)` / `find_one(filtro)` |
| `UPDATE ... SET` | `update_one(filtro, {"$set": {...}})` |
| `DELETE ... WHERE` | `delete_one(filtro)` / `delete_many(filtro)` |
| `commit()` | No hace falta: cada operación se guarda al ejecutarse |
| `%s` para evitar inyección SQL | Los filtros son diccionarios, no texto pegado; pero el texto de un `$regex` sí se debe escapar |

Ninguna es "mejor": SQL brilla cuando los datos tienen relaciones fijas
(pedidos, clientes, facturas); MongoDB cuando cada registro puede tener una
forma distinta o se guarda y se lee como un todo (catálogos, perfiles,
registros de eventos).

## Paso 1. Instalar MongoDB

Escoge **una** de estas opciones.

**Opción A: MongoDB en tu equipo (Windows).**

1. Descarga *MongoDB Community Server* desde
   <https://www.mongodb.com/try/download/community> (paquete `.msi`).
2. En el instalador elige *Complete* y deja marcado *Install MongoDB as a
   Service*: así queda encendido siempre que prendas el equipo.
3. Deja marcado también *Install MongoDB Compass*, la herramienta gráfica
   para ver las bases y colecciones (es como el Workbench de MySQL).
4. Abre Compass y conéctate a `mongodb://localhost:27017`. Si entra, el
   servidor está funcionando.

**Opción B: con Docker.**

```
docker run -d --name mongo -p 27017:27017 mongo
```

**Opción C: en la nube con MongoDB Atlas (gratis).**

1. Crea una cuenta en <https://www.mongodb.com/atlas> y un clúster gratuito.
2. Crea un usuario de base de datos y, en *Network Access*, permite tu IP.
3. Copia la cadena de conexión (`mongodb+srv://usuario:clave@...`) y
   úsala como `MONGO_URI` (paso 3).

## Paso 2. Instalar el conector

Desde la raíz de la repo, con el entorno virtual activado:

```
pip install -r requirements.txt
```

o solo el conector:

```
pip install pymongo
```

`pymongo` ya trae el módulo `bson` (de ahí se importa `ObjectId`). **No
instales el paquete `bson` por aparte**: es otro proyecto, choca con el de
`pymongo` y produce errores extraños. Si lo instalaste:

```
pip uninstall bson pymongo
pip install pymongo
```

## Paso 3. Configurar la conexión

Cada archivo empieza así:

```python
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")
```

- Con MongoDB en tu equipo (opciones A y B) no tienes que cambiar nada.
- Con Atlas, en PyCharm: `Run > Edit Configurations > Environment
  variables`, agrega `MONGO_URI=mongodb+srv://...`. No escribas la clave
  de Atlas en el código ni la subas al repositorio.

No hay que crear la base `curso_poo` ni las colecciones: MongoDB las crea
la primera vez que se inserta un documento.

## Paso 4. Recorrer los ejemplos en orden

Cada ejemplo es un paso y se apoya en el anterior. Ejecuta primero el 01
(para saber que hay conexión) y el 02 (carga los datos de muestra que usan
los demás). Mientras avanzas, abre Compass y mira cómo cambia la colección
`curso_poo.productos`.

| Paso | Archivo | Qué aprendes |
|---|---|---|
| 1 | `01_conexion.py` | `MongoClient`, `ping`, servidor -> base -> colección |
| 2 | `02_insertar.py` | **C**reate: `insert_one`, `insert_many`, el `_id` y el `ObjectId`, esquema flexible |
| 3 | `03_leer.py` | **R**ead: `find`, `find_one`, proyección, `sort`, `limit`, `count_documents`, buscar por `_id` |
| 4 | `04_buscar.py` | Filtros: `$gt`, `$gte`, `$in`, `$or`, `$regex`, listas y documentos anidados |
| 5 | `05_actualizar.py` | **U**pdate: `$set`, `$inc`, `$push`, `$addToSet`, `$unset`, `matched_count`, el peligro de `replace_one` |
| 6 | `06_eliminar.py` | **D**elete: `delete_one`, `delete_many`, `deleted_count` |
| 7 | `07_repositorio_poo.py` y `repositorio_productos.py` | El CRUD en clases: conexión con `with`, repositorio, índice único y `DuplicateKeyError` |
| 8 | `08_crud_con_tkinter.py` | La interfaz completa: formulario, Treeview, buscador y CRUD sobre MongoDB |

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Conectarse | `MongoClient(uri, serverSelectionTimeoutMS=3000)` y `cliente.admin.command("ping")` |
| Colección | `cliente["curso_poo"]["productos"]` |
| Insertar | `coleccion.insert_one({"nombre": "Mouse", "precio": 65000})` |
| Id del nuevo documento | `str(resultado.inserted_id)` |
| Buscar por id | `coleccion.find_one({"_id": ObjectId(id_texto)})` |
| Validar un id | `ObjectId.is_valid(id_texto)` |
| Comparar | `{"precio": {"$gte": 1000, "$lte": 5000}}` |
| Contiene (LIKE) | `{"nombre": {"$regex": re.escape(texto), "$options": "i"}}` |
| Ordenar | `coleccion.find(filtro).sort("nombre", ASCENDING)` |
| Cambiar campos | `update_one(filtro, {"$set": {"precio": 9000}})` |
| Sumar | `update_one(filtro, {"$inc": {"stock": 5}})` |
| Lista sin repetidos | `update_one(filtro, {"$addToSet": {"etiquetas": "oferta"}})` |
| Nombres únicos | `coleccion.create_index("nombre", unique=True)` y capturar `DuplicateKeyError` |
| El cursor se gasta | Si necesitas los datos dos veces: `lista = list(coleccion.find(...))` |
| Treeview | `insert("", tk.END, iid=str(doc["_id"]), values=(...))` y `ObjectId(seleccion[0])` al volver |

## Ejercicios

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Primeros documentos | Básico | `insert_one`, id como texto, `find_one` por `ObjectId`, `count_documents` |
| 02 | Consultas con filtros | Intermedio | `$gte`/`$lte`, `$regex` escapado, `sort`, búsquedas en listas |
| 03 | Actualizar y eliminar | Intermedio | `$set`, `$inc`, `$addToSet`, venta solo con stock suficiente, `delete_one` |
| 04 | Repositorio de productos | Avanzado | Clase repositorio, índice único, `DuplicateKeyError`, `**kwargs` |
| 05 | CRUD con Tkinter | Avanzado | CRUD completo con Treeview, buscador y validación |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | El id como texto | Básico | 2 | Devolver el resultado en vez del id, buscar con texto en vez de `ObjectId` |
| 02 | El cursor vacío | Básico | 2 | `$gt` en vez de `$gte`, recorrer dos veces el mismo cursor |
| 03 | La actualización que borra | Intermedio | 2 | `replace_one` en vez de `$set`, `$set` en vez de `$inc` |
| 04 | Buscador con regex | Intermedio | 2 | Sin `$options: "i"`, texto sin escapar |
| 05 | CRUD con Tkinter que no guarda | Avanzado | 3 | Vista sin recargar, tupla de selección, borrar solo en pantalla |

## Cómo trabajar los ejercicios

Las pruebas trabajan sobre la colección `curso_poo.ej_productos` (no tocan
`productos`, la de los ejemplos). Crean documentos con nombres que empiezan
por `PRUEBA_EJ_` y los borran al terminar, aunque fallen. Los de Tkinter
corren con la ventana oculta y, cuando pasan, abren la ventana real.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

Si el error es `ServerSelectionTimeoutError`, no es tu código: MongoDB no
está encendido o la `MONGO_URI` está mal (vuelve al paso 1).

## Qué crean los ejemplos y ejercicios en MongoDB

- Base `curso_poo` con las colecciones `productos` (ejemplos) y
  `ej_productos` (ejercicios).
- Un índice único sobre `nombre` en las dos colecciones (lo crean el
  ejemplo 07 y el ejercicio propuesto 04).
- Para empezar de cero, en Compass borra la base `curso_poo`, o desde
  Python: `MongoClient().drop_database("curso_poo")`.
