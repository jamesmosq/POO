"""
Ejercicio propuesto 03 - Herencia de formularios
Nivel: intermedio

Muchos formularios se parecen: etiquetas, campos y un botón Guardar. Con
herencia, la estructura se escribe una vez y cada formulario solo define
sus campos y sus reglas.

Requisitos:
1. Clase FormularioBase(tk.Frame):
   - Atributo de clase CAMPOS = [] (las hijas lo reemplazan).
   - En __init__ crea, para cada campo de CAMPOS, un Label y un Entry con
     grid. Guarda los Entry en self.entradas (campo -> Entry).
   - self.boton ("Guardar"), self.mensaje (Label) y self.guardados (lista).
   - guardar(): arma un diccionario campo -> texto (sin espacios a los
     lados), llama a self.validar(datos). Si retorna un error, lo muestra
     en self.mensaje. Si no, agrega los datos a self.guardados y muestra
     "Guardado".
   - validar(datos): retorna "Falta <campo>" para el primer campo vacío,
     o None.
2. FormularioCliente(FormularioBase): CAMPOS = ["Nombre", "Correo"].
   validar() usa la validación del padre y además exige "@" en el correo
   ("Correo inválido").
3. FormularioProducto(FormularioBase): CAMPOS = ["Nombre", "Precio"].
   validar() usa la del padre y además exige que el precio sea un número
   ("Precio inválido").

Conceptos: herencia en interfaces, atributos de clase, super() en un
método sobrescrito.
"""
import tkinter as tk

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()

    def enviar(formulario, valores):
        for campo, valor in valores.items():
            formulario.entradas[campo].delete(0, tk.END)
            formulario.entradas[campo].insert(0, valor)
        formulario.boton.invoke()
        return formulario.mensaje.cget("text")

    cliente = FormularioCliente(raiz)
    assert list(cliente.entradas) == ["Nombre", "Correo"]
    assert enviar(cliente, {"Nombre": "", "Correo": "a@b.co"}) == "Falta Nombre"
    assert enviar(cliente, {"Nombre": "Ana", "Correo": "ana"}) == "Correo inválido"
    assert enviar(cliente, {"Nombre": " Ana ", "Correo": "ana@mail.com"}) == "Guardado"
    assert cliente.guardados == [{"Nombre": "Ana", "Correo": "ana@mail.com"}]

    producto = FormularioProducto(raiz)
    assert list(producto.entradas) == ["Nombre", "Precio"]
    assert enviar(producto, {"Nombre": "Café", "Precio": ""}) == "Falta Precio"
    assert enviar(producto, {"Nombre": "Café", "Precio": "doce"}) == "Precio inválido"
    assert enviar(producto, {"Nombre": "Café", "Precio": "12000"}) == "Guardado"

    for clase in (FormularioCliente, FormularioProducto):
        assert "__init__" not in clase.__dict__, f"{clase.__name__} no necesita su propio __init__"
        assert "guardar" not in clase.__dict__
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        FormularioCliente(raiz).pack(padx=10, pady=10)
        FormularioProducto(raiz).pack(padx=10, pady=10)
        raiz.mainloop()
