"""
Ejercicio propuesto 02 - Interfaz de almacenamiento
Nivel: intermedio

Una clase abstracta también sirve como "contrato" (interfaz): el resto del
programa trabaja con ella sin saber si los datos se guardan en memoria, en
un archivo o en una base de datos.

Requisitos:
1. Clase abstracta Almacenamiento con tres métodos abstractos:
       guardar(clave, valor)
       obtener(clave)        -> retorna el valor o None si no existe
       eliminar(clave)       -> retorna True si existía, False si no
2. AlmacenamientoMemoria: guarda en un diccionario.
3. AlmacenamientoJSON(ruta): guarda en un archivo JSON. Cada operación lee
   el archivo, hace el cambio y lo vuelve a escribir. Si el archivo no
   existe, se considera vacío.
4. Función registrar_visita(almacen, usuario): suma 1 al contador de
   visitas de ese usuario (clave = usuario) y retorna el nuevo total.
   Debe funcionar igual con cualquiera de los dos almacenamientos.

Conceptos: interfaces, inversión de dependencias, intercambiar
implementaciones.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os
    import tempfile

    try:
        Almacenamiento()
        raise AssertionError("Almacenamiento debe ser abstracta")
    except TypeError:
        pass

    ruta = os.path.join(tempfile.mkdtemp(), "datos.json")
    for almacen in (AlmacenamientoMemoria(), AlmacenamientoJSON(ruta)):
        assert almacen.obtener("x") is None
        almacen.guardar("x", 10)
        assert almacen.obtener("x") == 10
        assert almacen.eliminar("x") is True
        assert almacen.eliminar("x") is False

        assert registrar_visita(almacen, "ana") == 1
        assert registrar_visita(almacen, "ana") == 2
        assert registrar_visita(almacen, "luis") == 1

    assert AlmacenamientoJSON(ruta).obtener("ana") == 2, "Los datos deben quedar en el archivo"

    print("Todas las pruebas pasaron")
