"""
Ejemplo 07 - El CRUD organizado con POO
Paso 7 de la ruta del CRUD con MongoDB.

Qué aprendes:
    - Una clase ConexionMongo que se usa con "with" y cierra sola.
    - Un repositorio: la única clase que habla con la colección. El resto
      del programa (por ejemplo la interfaz gráfica) solo llama métodos
      como crear(), listar() o eliminar().
    - Convertir el _id (ObjectId) a un campo "id" de texto al salir del
      repositorio, y de texto a ObjectId al entrar.
    - Índice único: impedir nombres repetidos y capturar DuplicateKeyError.

Las clases están en repositorio_productos.py (ábrelo y léelo junto con
este archivo). Es la misma idea del tema 02_crud_con_poo, pero con MongoDB.
El ejemplo 08 usa estas mismas clases para construir la interfaz.
"""
from repositorio_productos import ConexionMongo, RepositorioProductos


def main():
    with ConexionMongo() as db:
        repositorio = RepositorioProductos(db)

        # Limpieza por si el ejemplo se ejecutó antes y quedó a medias.
        repositorio.coleccion.delete_many({"nombre": {"$regex": "^Ejemplo 07"}})

        id_nuevo = repositorio.crear({"nombre": "Ejemplo 07 Parlante", "categoria": "Audio",
                                      "precio": "85000", "stock": "4"})
        print("Creado:", repositorio.obtener(id_nuevo))

        try:
            repositorio.crear({"nombre": "Ejemplo 07 Parlante", "precio": 1, "stock": 1})
        except ValueError as error:
            print("No se pudo crear:", error)

        repositorio.actualizar(id_nuevo, {"nombre": "Ejemplo 07 Parlante", "categoria": "Audio",
                                          "precio": 79000, "stock": 6})
        print("Actualizado:", repositorio.obtener(id_nuevo))

        print("Buscar 'parlante':", [p["nombre"] for p in repositorio.listar("parlante")])

        print("¿Eliminado?", repositorio.eliminar(id_nuevo))
        print("Total de productos:", len(repositorio.listar()))


if __name__ == "__main__":
    main()
