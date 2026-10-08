# Variables y tipos de datos

**Nivel:** básico
**Antes de este tema:** ninguno, es el punto de partida.
**Después de este tema:** `01_fundamentos/02_operadores`

## Objetivos

- Crear variables y elegir nombres válidos y descriptivos.
- Reconocer los tipos básicos: `str`, `int`, `float` y `bool`.
- Convertir entre tipos con `int()`, `float()` y `str()`.
- Hacer cálculos con operadores aritméticos y respetar su precedencia.
- Construir mensajes con f-strings y dar formato a números.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Asignación | `edad = 20` |
| Tipos | `type("Ana")` es `str`, `type(20)` es `int`, `type(1.65)` es `float` |
| Conversión | `int("17")`, `float("2.5")`, `str(20)` |
| Aritmética | `+  -  *  /  //  %  **` |
| f-string | `f"Tengo {edad} años"`, `f"{precio:,.2f}"` |
| `input()` | Siempre devuelve texto (`str`) |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivo | Tema |
|---|---|
| 01 | Comentarios, indentación y operadores |
| 02 | Operaciones aritméticas |
| 03 - 07 | Programas cortos con `input()`: unidades, descuentos, promedios, edad, áreas |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Datos personales | Básico | Tipos de datos, f-strings |
| 02 | Conversión de temperatura | Básico | Fórmulas, precedencia |
| 03 | Factura simple | Básico | Porcentajes, formato de moneda |
| 04 | Tiempo en segundos | Intermedio | `//` y `%` |
| 05 | Conversión de tipos | Intermedio | `int()`, `float()`, `bool` |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Saludo | Básico | 2 | Nombre de variable, concatenar `str` con `int` |
| 02 | Promedio de notas | Básico | 2 | Mayúsculas, precedencia |
| 03 | Compra con descuento | Básico | 2 | Texto sin convertir, porcentaje |
| 04 | Círculo | Intermedio | 3 | Conversión, operador de potencia, nombres |
| 05 | Reloj digital | Intermedio | 3 | `/` contra `//`, residuo |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
