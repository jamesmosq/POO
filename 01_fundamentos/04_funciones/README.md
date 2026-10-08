# Funciones

**Nivel:** básico a intermedio
**Antes de este tema:** `01_fundamentos/03_condicionales`
**Después de este tema:** `01_fundamentos/05_bucles`

## Objetivos

- Definir funciones con `def` y entregar resultados con `return`.
- Diferenciar `print()` (mostrar) de `return` (entregar un valor).
- Usar parámetros obligatorios, valores por defecto y argumentos por nombre.
- Recibir una cantidad variable de argumentos con `*args` y `**kwargs`.
- Entender el alcance de las variables (locales y globales).
- Tratar las funciones como valores: `lambda`, `map`, `filter`, `sorted`.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Definir y retornar | `def doble(x): return x * 2` |
| Valor por defecto | `def saludar(nombre, saludo="Hola"):` |
| Varios valores | `return minimo, maximo` y `a, b = funcion()` |
| `*args` | `def sumar(*numeros):` recibe una tupla |
| `**kwargs` | `def perfil(nombre, **datos):` recibe un diccionario |
| `lambda` | `lambda p: p[1]` |
| Llamar contra referenciar | `f()` ejecuta la función; `f` es la función misma |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 - 06 | Sintaxis, parámetros, valores por defecto, `*args`, varios valores de retorno |
| 07 - 09 | Programas con funciones: calculadora, entrada de datos, conversor de temperatura |
| 10 | Funciones que reciben otras funciones |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Saludo por idioma | Básico | Parámetros por defecto, `return` |
| 02 | Estadísticas de notas | Básico | Retornar varios valores, reutilizar funciones |
| 03 | Conversor de unidades | Intermedio | Descomposición en funciones, constantes |
| 04 | Argumentos variables | Intermedio | `*args`, `**kwargs`, desempaquetado |
| 05 | Funciones como valores | Avanzado | `lambda`, composición, clausuras, recursión |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Área del rectángulo | Básico | 2 | Orden de definición, `print` contra `return` |
| 02 | Saludo con valor por defecto | Básico | 2 | Orden de parámetros, f-string |
| 03 | Contador de visitas | Intermedio | 2 | Alcance (`global`), llamar sin paréntesis |
| 04 | Promedio y perfil | Intermedio | 3 | Desempaquetado, división entre cero, `*` contra `**` |
| 05 | Catálogo con lambdas | Avanzado | 3 | Lógica dentro de `lambda`, `map`, `sorted`, `filter` |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
