"""
Ejemplo 01 - Conectarse a MongoDB
Paso 1 de la ruta del CRUD con MongoDB.

Qué aprendes:
    - Crear un MongoClient a partir de una cadena de conexión (URI).
    - Comprobar que el servidor responde con el comando "ping".
    - Entender la jerarquía de MongoDB: servidor -> base de datos ->
      colección -> documento.

Comparación con MySQL:
    MySQL                         MongoDB
    -------------------------     -------------------------
    mysql.connector.connect()     MongoClient(uri)
    base de datos                 base de datos
    tabla                         colección
    fila                          documento (un diccionario)
    columna                       campo

Antes de ejecutar:
    1. Tener MongoDB corriendo (ver el README del tema, paso 1).
    2. pip install pymongo
"""
import os

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# La URI dice dónde está el servidor. Con MongoDB instalado en tu equipo
# es mongodb://localhost:27017. Con MongoDB Atlas (en la nube) es algo como
# mongodb+srv://usuario:clave@cluster0.xxxxx.mongodb.net/
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "curso_poo")


def main():
    # serverSelectionTimeoutMS: cuánto esperar (en milisegundos) antes de
    # rendirse si el servidor no responde. Sin él, el programa se queda
    # 30 segundos "pegado" cuando MongoDB está apagado.
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)

    try:
        # MongoClient NO se conecta al crearse: se conecta la primera vez
        # que lo usas. Por eso hacemos un "ping" para saber si hay servidor.
        cliente.admin.command("ping")
        print("Conexión exitosa a", MONGO_URI)
    except ServerSelectionTimeoutError:
        print("No se pudo conectar. ¿Está encendido el servicio de MongoDB?")
        cliente.close()
        return

    # Una base de datos y una colección se obtienen como si fueran
    # diccionarios. Si no existen, MongoDB las crea automáticamente cuando
    # insertes el primer documento. No hay CREATE DATABASE ni CREATE TABLE.
    db = cliente[MONGO_DB]
    productos = db["productos"]

    print("Bases de datos en el servidor:", cliente.list_database_names())
    print("Colecciones en", MONGO_DB, ":", db.list_collection_names())
    print("Documentos en 'productos':", productos.count_documents({}))

    # Igual que con MySQL: cerrar la conexión al terminar.
    cliente.close()


if __name__ == "__main__":
    main()
