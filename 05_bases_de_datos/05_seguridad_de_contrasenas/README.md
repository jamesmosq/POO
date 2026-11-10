# Seguridad de contraseñas

**Nivel:** avanzado
**Antes de este tema:** `05_bases_de_datos/04_crud_con_interfaz`
**Después de este tema:** `05_bases_de_datos/06_crud_nosql`

## Objetivos

- Guardar contraseñas como hash con `bcrypt`, nunca en texto plano.
- Verificar contraseñas con `bcrypt.checkpw` (no comparando hashes).
- Registrar usuarios y manejar duplicados con una columna `UNIQUE`.
- Implementar inicio de sesión con bloqueo por intentos fallidos sin
  revelar si el usuario existe.
- Aplicar una política de contraseñas.
- Reconocer y evitar la inyección SQL, incluidos los comodines de `LIKE`.

## Conceptos clave

| Concepto | Ejemplo |
|---|---|
| Hash | `bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()` |
| Verificar | `bcrypt.checkpw(clave.encode(), hash_guardado.encode())` |
| Sal | Viene dentro del hash; por eso dos hashes de la misma clave son distintos |
| bytes y str | `.encode()` para pasar a bytes, `.decode()` para volver a texto |
| Duplicados | `mysql.connector.IntegrityError` con `errno` 1062 |
| Respuesta uniforme | Usuario inexistente y clave incorrecta dan el mismo resultado |
| Inyección SQL | Nunca pegar datos del usuario en el SQL; usar `%s` |
| Comodines de LIKE | Escapar `%` y `_` y usar `ESCAPE '!'` |

## Contenido

### Ejemplos (`ejemplos/`)

| Archivo | Tema |
|---|---|
| 01 | Registro e inicio de sesión con bcrypt (usa la base `gestion_u`) |

### Ejercicios propuestos (`ejercicios_propuestos/`)

| # | Ejercicio | Nivel | Practica |
|---|---|---|---|
| 01 | Hash con bcrypt | Básico | `hashpw`, `checkpw`, bytes y str |
| 02 | Registrar usuarios | Intermedio | Guardar hashes, `UNIQUE`, `IntegrityError` |
| 03 | Inicio de sesión con bloqueo | Intermedio | Intentos fallidos, bloqueo, respuesta uniforme |
| 04 | Política y cambio de clave | Intermedio | Reglas de contraseñas, verificar la clave actual |
| 05 | Inyección SQL | Avanzado | Parámetros, escapar comodines de LIKE |

### Ejercicios para corregir (`ejercicios_para_corregir/`)

| # | Ejercicio | Nivel | Errores | Tipo de errores |
|---|---|---|---|---|
| 01 | Hash mal usado | Básico | 2 | str contra bytes, verificar con `==` |
| 02 | Registro inseguro | Básico | 2 | Método sin llamar, clave en texto plano |
| 03 | Login que falla | Intermedio | 2 | Orden de los argumentos de `checkpw`, usuario inexistente |
| 04 | Bloqueo que no bloquea | Intermedio | 3 | `commit` faltante, reinicio de intentos, límite |
| 05 | Cambio de clave | Avanzado | 3 | Verificar la clave equivocada, parámetros cruzados, `commit` |

## Cómo trabajar los ejercicios

Los ejercicios 02 a 05 crean en tu base de datos la tabla `ej_usuarios` si
no existe. Los usuarios de prueba empiezan por `prueba_ej_` y se borran al
terminar. Si quieres eliminar la tabla después: `DROP TABLE ej_usuarios;`.

1. Abre el ejercicio y lee el enunciado completo.
2. Escribe tu código o, en los de corregir, arregla el código existente.
3. Ejecuta el archivo. Las pruebas al final te dicen qué falta.
4. Cuando veas `Todas las pruebas pasaron`, compara con `soluciones/`.
