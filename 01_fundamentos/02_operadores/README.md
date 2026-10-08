# Operadores relacionales y lógicos

**Nivel:** básico
**Antes de este tema:** `01_fundamentos/01_variables_y_tipos`
**Después de este tema:** `01_fundamentos/03_condicionales`

## Objetivos

- Comparar valores con operadores relacionales y obtener un `bool`.
- Combinar condiciones con `and`, `or` y `not`.
- Conocer la precedencia de los operadores y usar paréntesis para aclararla.
- Escribir rangos con comparaciones encadenadas (`1 <= x <= 100`).
- Probar siempre los valores límite de una condición.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Relacionales | `==  !=  >  <  >=  <=` |
| Lógicos | `and`, `or`, `not` |
| Precedencia | `not` antes que `and`, `and` antes que `or` |
| Encadenadas | `18 <= edad <= 59` |
| Pertenencia | `" " in clave` |
| Asignar contra comparar | `=` guarda un valor, `==` compara |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 | Tabla de verdad de `and`, `or` y `not` |
| 02 - 10 | Comparaciones en programas cortos: edad, par o impar, rangos, bisiesto, notas |
| 11 - 18 | Expresiones lógicas combinadas y precedencia |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Comparaciones | Básico | Operadores relacionales, `%` |
| 02 | Rango de edad | Básico | Comparaciones encadenadas, límites |
| 03 | Acceso a un evento | Intermedio | `and`, `or`, `not` y paréntesis |
| 04 | Año bisiesto | Intermedio | Condición compuesta, `bool` como número |
| 05 | Contraseña segura | Avanzado | Condiciones sobre texto |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Mayor de edad y par | Básico | 2 | Sintaxis de operadores, residuo |
| 02 | Número en rango | Básico | 2 | `=` contra `==`, rango mal escrito |
| 03 | ¿Puede votar? | Intermedio | 2 | Valor de verdad de un texto, `and` contra `or` |
| 04 | Año bisiesto | Intermedio | 3 | `%` con texto, precedencia, concatenar `bool` |
| 05 | Contraseña segura | Avanzado | 3 | Límites, condición invertida, `and` contra `or` |

## Cómo trabajar los ejercicios

En este tema el código va entre las marcas `# >>> tu código empieza aquí` y
`# <<< tu código termina aquí`. Las pruebas ejecutan ese bloque varias veces
con datos distintos, por eso no sirve escribir `True` o `False` a mano.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe o corrige el código entre las marcas.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
