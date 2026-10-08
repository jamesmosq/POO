"""
Solución - Ejercicio propuesto 03 - try, except, else y finally
"""

def procesar(texto, registro):
    registro.append("inicio")
    numero = None
    try:
        numero = int(texto)
    except ValueError:
        registro.append("error")
    else:
        registro.append("ok")
    finally:
        registro.append("fin")
    return numero


# Respuesta a la pregunta:
# El try debe contener solo el código que puede lanzar el error que se
# quiere atrapar. Si el código del caso exitoso estuviera dentro del try y
# fallara por otra razón (un error de programación, por ejemplo), el except
# lo atraparía y lo confundiría con el error esperado. En else, ese error
# se vería tal como es.


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    registro = []
    assert procesar("10", registro) == 10
    assert registro == ["inicio", "ok", "fin"], registro

    registro = []
    assert procesar("diez", registro) is None
    assert registro == ["inicio", "error", "fin"], registro

    print("Todas las pruebas pasaron")
