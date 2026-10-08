# Módulos y paquetes

**Nivel:** intermedio
**Antes de este tema:** `01_fundamentos/07_errores_y_excepciones`
**Después de este tema:** `02_estructuras_de_datos/01_busqueda_y_ordenamiento`

## Objetivos

- Usar módulos de la biblioteca estándar: `math`, `random`, `json`, `os`,
  `pathlib`, `collections`.
- Crear módulos propios e importarlos desde otros archivos.
- Entender `if __name__ == "__main__":` y por qué el código suelto de un
  módulo se ejecuta al importarlo.
- Organizar un proyecto en paquetes con `__init__.py` e importaciones
  relativas.
- Guardar y leer datos en archivos JSON.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Importar un módulo | `import math` y luego `math.pi` |
| Importar un nombre | `from math import pi` |
| Módulo propio | `conversiones.py` se importa con `import conversiones` |
| `__name__` | Vale `"__main__"` solo en el archivo que se ejecuta |
| Paquete | Carpeta con `__init__.py` y módulos |
| Importación relativa | `from .utilidades import formatear` dentro del paquete |
| JSON | `json.dump` / `json.load` (archivos), `json.dumps` / `json.loads` (textos) |

## Contenido

### Ejemplos (`ejemplos/`)

| Carpeta o archivo | Tema |
|---|---|
| `01_cajero_automatico/` | Proyecto con paquete `cajero`, datos en JSON y menú |
| `02_biblioteca_modular/` | Paquete `biblioteca` con gestión de libros |
| `03_biblioteca_con_login/` | Sistema con usuarios, préstamos y varios archivos JSON |
| `04_paquete_externo_requests.py` | Usar un paquete instalado con pip (`requests`) |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Módulos math y random | Básico | `import`, semillas aleatorias |
| 02 | Guardar y cargar JSON | Básico | `json`, `os.path` |
| 03 | Crear tu propio módulo | Intermedio | Módulo propio, `__name__` |
| 04 | Crear un paquete | Intermedio | `__init__.py`, importaciones relativas |
| 05 | Counter y pathlib | Avanzado | `collections`, `pathlib` |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Importar math | Básico | 2 | Mayúsculas en módulos y atributos |
| 02 | Sorteo y JSON | Básico | 2 | `from ... import`, `dump` contra `dumps` |
| 03 | Usar un módulo propio | Intermedio | 2 | Código suelto en el módulo, nombre inexistente |
| 04 | Paquete banco | Intermedio | 3 | Importación relativa, `__init__.py`, formato |
| 05 | Configuración en JSON | Avanzado | 3 | Copia contra referencia, orden al combinar, modo de apertura |

Los ejercicios 03 y 04 para corregir tienen errores también en sus módulos
auxiliares (`impuestos.py` y la carpeta `banco/`).

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código (o crea el módulo o el paquete que se pide) o, en los
   de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
