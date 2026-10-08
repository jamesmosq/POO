"""
Ejercicio propuesto 02 - Conversor de temperatura
Nivel: básico

Requisitos. Crea la clase Conversor(raiz) con:
1. Título "Conversor".
2. self.entrada: Entry para los grados Celsius.
3. self.boton: Button "Convertir" que llama a convertir().
4. self.resultado: Label con el resultado.
5. convertir(): muestra "77.0 °F" (un decimal). Si lo escrito no es un
   número, muestra "Valor inválido". Acepta coma decimal: "36,5" es 36.5.
6. Que la tecla Enter dentro del Entry también convierta:
       self.entrada.bind("<Return>", lambda evento: self.convertir())

Conceptos: conversión de datos de la interfaz, manejo de errores, eventos
de teclado.
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
    app = Conversor(raiz)
    assert raiz.title() == "Conversor"
    assert app.boton.cget("text") == "Convertir"

    app.entrada.insert(0, "25")
    app.boton.invoke()
    assert app.resultado.cget("text") == "77.0 °F", app.resultado.cget("text")

    app.entrada.delete(0, tk.END)
    app.entrada.insert(0, "36,5")
    app.boton.invoke()
    assert app.resultado.cget("text") == "97.7 °F", app.resultado.cget("text")

    app.entrada.delete(0, tk.END)
    app.entrada.insert(0, "abc")
    app.boton.invoke()
    assert app.resultado.cget("text") == "Valor inválido"

    assert app.entrada.bind("<Return>"), "Falta asociar la tecla Enter al Entry"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Conversor(raiz)
        raiz.mainloop()
