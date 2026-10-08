"""
Ejercicio propuesto 03 - try, except, else y finally
Nivel: intermedio

Un bloque try completo tiene cuatro partes:
    try:      el código que puede fallar
    except:   se ejecuta solo si hubo un error
    else:     se ejecuta solo si NO hubo error
    finally:  se ejecuta SIEMPRE, haya error o no

Requisitos. Escribe procesar(texto, registro). registro es una lista en la
que vas a anotar cada paso:
    - Al empezar, agrega "inicio".
    - En el try, convierte texto a int.
    - Si falla (ValueError), agrega "error".
    - Si no falla, agrega "ok" desde el bloque else.
    - En el finally, agrega "fin".
La función retorna el número convertido, o None si hubo error.

Pregunta para pensar (respóndela en un comentario): ¿por qué conviene
poner el código del caso exitoso en else y no al final del try?

Conceptos: flujo de try / except / else / finally.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    registro = []
    assert procesar("10", registro) == 10
    assert registro == ["inicio", "ok", "fin"], registro

    registro = []
    assert procesar("diez", registro) is None
    assert registro == ["inicio", "error", "fin"], registro

    print("Todas las pruebas pasaron")
