# Polimorfismo

**Nivel:** intermedio
**Antes de este tema:** `03_poo/04_herencia_multiple`
**Después de este tema:** `03_poo/06_abstraccion`

## Objetivos

- Escribir código que trabaje con objetos de clases distintas a través de
  una misma interfaz (los mismos métodos).
- Reemplazar cadenas de `if type(...)` por llamadas polimórficas.
- Aplicar duck typing: no importa la clase, importa que tenga el método.
- Diseñar clases base cuyos métodos llaman a métodos que las hijas
  sobrescriben (método plantilla).
- Mantener la misma "forma" del método en todas las clases: nombre,
  parámetros y tipo de resultado.

## Conceptos clave

| Concepto | Idea |
|---|---|
| Polimorfismo | La misma llamada (`figura.area()`) hace cosas distintas según el objeto |
| Sobrescritura | La hija redefine un método del padre |
| `NotImplementedError` | La base indica que las hijas deben implementar el método |
| Duck typing | Si tiene el método, se puede usar; no hace falta herencia |
| Método plantilla | La base define los pasos; las hijas completan solo una parte |
| Sobrecarga | Python no la tiene como Java; se simula con valores por defecto o `*args` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 04 | Polimorfismo con herencia: animales, notificadores, tipos de polimorfismo, electrodomésticos |
| 05 | Duck typing |
| 06 - 10 | Ejercicios resueltos: vehículos, áreas, notificaciones, pagos, reproductor |
| 11 - 16 | Sobrecarga de métodos simulada: formas, calculadora, empleados, conversor, base de datos |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Figuras | Básico | Sobrescritura, funciones que usan cualquier figura |
| 02 | Duck typing | Básico | Polimorfismo sin herencia, `hasattr` |
| 03 | Medios de pago | Intermedio | Método plantilla, atributos de clase |
| 04 | Notificaciones | Intermedio | La base valida y registra; las hijas formatean |
| 05 | Nómina | Avanzado | Varios niveles de herencia, `super()`, `__str__` |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Sonidos de animales | Básico | 2 | Nombre del método, llamar sin paréntesis |
| 02 | Áreas con if | Básico | 2 | `self` faltante, `type()` en lugar de polimorfismo |
| 03 | Procesar pagos | Intermedio | 2 | Firma distinta, tipo de retorno distinto |
| 04 | Notificaciones | Intermedio | 3 | `__init__` de la hija, sobrescribir el método equivocado, registro |
| 05 | Nómina | Avanzado | 3 | Horas extra, `super()` faltante, orden del reporte |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
