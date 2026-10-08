# Encapsulamiento

**Nivel:** intermedio
**Antes de este tema:** `03_poo/01_clases_y_objetos`
**Después de este tema:** `03_poo/03_herencia`

## Objetivos

- Proteger el estado interno de un objeto para que solo cambie a través de
  métodos que validan.
- Usar las convenciones de Python: público, `_protegido` y `__privado`.
- Entender el name mangling de los atributos con doble guion bajo.
- Crear propiedades con `@property` y `@nombre.setter`.
- Exponer colecciones internas sin permitir que se modifiquen desde afuera.
- Manejar datos sensibles (contraseñas) de forma segura.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Público | `self.nombre` |
| Protegido (convención) | `self._nombre` |
| Privado (name mangling) | `self.__saldo` se guarda como `self._Clase__saldo` |
| Getter | `@property def precio(self): return self._precio` |
| Setter | `@precio.setter def precio(self, valor): ...` |
| Solo lectura | Una propiedad sin setter |
| Proteger colecciones | Retornar `tuple(self._lista)` en lugar de la lista |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivo | Tema |
|---|---|
| 01 | Errores comunes de encapsulamiento y su solución, casos de uso y un sistema bancario completo |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Cuenta con saldo privado | Básico | Atributo privado, métodos con validación |
| 02 | Propiedades de temperatura | Básico | `@property`, setter, propiedad calculada |
| 03 | Empleado con validaciones | Intermedio | Varias propiedades validadas, normalizar datos |
| 04 | Solo lectura e historial | Intermedio | Propiedad sin setter, proteger una lista |
| 05 | Usuario con contraseña | Avanzado | Hash con sal, `hashlib`, `secrets` |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Saldo privado | Básico | 2 | Nombre del atributo privado, atributo creado por error |
| 02 | Propiedad nombre | Básico | 2 | Recursión en el getter, nombre del setter |
| 03 | Validar desde el constructor | Intermedio | 2 | Name mangling en la clase hija, saltarse el setter |
| 04 | Lista de notas protegida | Intermedio | 3 | `and` contra `or`, lista expuesta, `return` faltante |
| 05 | Usuario y contraseña | Avanzado | 3 | Sal faltante, método sin llamar, clave en texto plano |

## Cómo trabajar los ejercicios

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código donde dice `# Escribe tu solución aquí` o, en los de
   corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.

No modifiques las pruebas: son la especificación de lo que se pide.
