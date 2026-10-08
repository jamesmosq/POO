# Condicionales: if, elif, else y match-case

**Nivel:** básico
**Antes de este tema:** `01_fundamentos/02_operadores`
**Después de este tema:** `01_fundamentos/04_funciones`

## Objetivos

- Tomar decisiones con `if`, `elif` y `else`.
- Ordenar las condiciones cuando se solapan (la más restrictiva primero).
- Usar `match-case` para comparar un valor contra varias opciones.
- Combinar opciones con `|` y agregar guardas con `if` dentro de un `case`.
- Lanzar un error con `raise` cuando un dato no es válido.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| `if / elif / else` | Solo se ejecuta el primer bloque cuya condición se cumple |
| Indentación | Define qué instrucciones pertenecen a cada bloque |
| `match-case` | `match opcion:` seguido de `case 1:`, `case 2:`, ... |
| Varias opciones | `case "sábado" \| "domingo":` |
| Guarda | `case "/" if b == 0:` |
| Comodín | `case _:` atrapa todo y va siempre al final |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 06 | `if`, `if-else`, `if-elif-else`: edad, temperatura, notas, calculadora, contraseña |
| 07 - 09 | Prácticas: validador de contraseña, conversor de temperatura, clasificador de edades |
| 10 - 15 | `match-case`: introducción, días, calculadora, conversor de unidades, comandos de juego |
| 16 - 17 | `match-case` en programas completos: propinas y cafetería |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Clasificar una nota | Básico | `if-elif-else`, orden de las condiciones |
| 02 | Tarifa de parqueadero | Básico | Condiciones anidadas, limpiar texto |
| 03 | Calculadora con match-case | Intermedio | `match`, guardas |
| 04 | Tipo de día | Intermedio | Patrones con `\|` |
| 05 | Impuesto progresivo | Avanzado | Tramos, límites, `raise` |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Mayor de edad | Básico | 2 | Indentación, límite |
| 02 | Clima | Básico | 2 | `else if`, orden de las condiciones |
| 03 | Precio con descuentos | Intermedio | 2 | Acumular con `+=`, mayúsculas |
| 04 | Menú con match-case | Intermedio | 3 | Comodín, tipos en los `case`, captura de nombres |
| 05 | Impuesto progresivo | Avanzado | 3 | `raise` faltante, lógica de tramos |

## Cómo trabajar los ejercicios

Las funciones se estudian en el tema 04. Aquí la línea `def` ya viene
escrita: solo completas el cuerpo y entregas el resultado con `return`.

1. Abre el ejercicio y lee el enunciado completo.
2. Completa la función o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
