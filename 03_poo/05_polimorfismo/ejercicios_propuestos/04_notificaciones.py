"""
Ejercicio propuesto 04 - Notificaciones
Nivel: intermedio

Requisitos:
1. Clase base Notificacion(destino):
   - formatear(mensaje): las hijas lo implementan (en la base lanza
     NotImplementedError).
   - enviar(mensaje): valida que el mensaje no esté vacío (ValueError),
     llama a formatear() y guarda el resultado en la lista de clase
     Notificacion.enviadas. Retorna el texto formateado.
2. Hijas, cada una con su formatear():
       Email(destino)  -> "Para: ana@mail.com | Asunto: Aviso | Hola"
       SMS(destino)    -> "SMS a 3001234567: Hola"   (máximo 20 caracteres
                           del mensaje; si es más largo, corta y agrega "...")
       Push(destino)   -> "[PUSH] Hola"
3. Función notificar_a_todos(notificaciones, mensaje): envía el mensaje
   por cada medio y retorna la lista de textos enviados.

Conceptos: polimorfismo, métodos que llaman a métodos sobrescritos,
atributos de clase compartidos.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Notificacion.enviadas = []
    medios = [Email("ana@mail.com"), SMS("3001234567"), Push("app-123")]
    resultado = notificar_a_todos(medios, "Hola")
    assert resultado == [
        "Para: ana@mail.com | Asunto: Aviso | Hola",
        "SMS a 3001234567: Hola",
        "[PUSH] Hola",
    ]
    assert len(Notificacion.enviadas) == 3

    largo = SMS("300").enviar("Este mensaje es demasiado largo")
    assert largo == "SMS a 300: Este mensaje es dema...", largo

    try:
        Push("x").enviar("")
        raise AssertionError("Un mensaje vacío debe lanzar ValueError")
    except ValueError:
        pass

    try:
        Notificacion("x").enviar("Hola")
        raise AssertionError("La base no sabe formatear: debe lanzar NotImplementedError")
    except NotImplementedError:
        pass

    print("Todas las pruebas pasaron")
