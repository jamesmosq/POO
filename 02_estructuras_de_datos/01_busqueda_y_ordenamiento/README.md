# Búsqueda y ordenamiento

**Nivel:** intermedio
**Antes de este tema:** `01_fundamentos/08_modulos_y_paquetes`
**Después de este tema:** `02_estructuras_de_datos/02_pilas`

## Objetivos

- Implementar la búsqueda lineal y la búsqueda binaria.
- Implementar los ordenamientos de burbuja, inserción y merge sort.
- Comparar algoritmos por la cantidad de pasos que hacen (eficiencia).
- Reconocer los errores típicos: límites de los índices, intercambios mal
  hechos, casos base de la recursión.
- Ordenar con `sorted()` y una `key`, y entender qué es un ordenamiento
  estable.

## Conceptos clave

| Algoritmo | Idea | Pasos en el peor caso |
|---|---|---|
| Búsqueda lineal | Revisar uno por uno | n |
| Búsqueda binaria | Descartar la mitad en cada paso (lista ordenada) | log2(n) |
| Burbuja | Intercambiar vecinos desordenados | n² |
| Inserción | Insertar cada elemento en su lugar | n² |
| Merge sort | Dividir, ordenar las mitades y mezclarlas | n · log2(n) |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivos | Tema |
|---|---|
| 01 | Ordenar y buscar con los métodos de Python |
| 02 - 03 | Búsqueda lineal con números y con palabras |
| 04 - 05 | Burbuja con números y con palabras |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Búsqueda lineal | Básico | Recorrido secuencial, contar comparaciones |
| 02 | Burbuja optimizada | Básico | Intercambios, bandera de parada |
| 03 | Búsqueda binaria | Intermedio | Índices `inicio`, `fin` y `medio` |
| 04 | Ordenamiento por inserción | Intermedio | Desplazamientos, orden descendente |
| 05 | Merge sort | Avanzado | Recursión, estabilidad, `key` |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Búsqueda lineal | Básico | 2 | Rango que omite el primero, retornar elemento contra índice |
| 02 | Burbuja | Básico | 2 | Intercambio que pierde un valor, dirección del orden |
| 03 | Búsqueda binaria | Intermedio | 2 | `/` contra `//`, condición del ciclo |
| 04 | Inserción | Intermedio | 3 | Límite del `while`, copia, parámetro sin usar |
| 05 | Merge sort | Avanzado | 3 | Caso base, elementos sobrantes, estabilidad |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

Consejo: antes de programar un algoritmo, hazlo a mano en papel con una
lista de 4 o 5 elementos.
