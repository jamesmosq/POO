"""
Solución - Ejercicio propuesto 05 - Calculadora
"""

import tkinter as tk

TECLAS = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"],
]
OPERACIONES = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


class Calculadora:
    def __init__(self, raiz):
        raiz.title("Calculadora")
        self.pantalla = tk.Label(raiz, text="0", anchor="e", font=("Arial", 18), width=12, relief="sunken")
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")
        self.botones = {}
        for fila, teclas in enumerate(TECLAS, start=1):
            for columna, texto in enumerate(teclas):
                # t=texto guarda el valor ACTUAL de texto en cada lambda.
                boton = tk.Button(raiz, text=texto, width=4, height=2,
                                  command=lambda t=texto: self.presionar(t))
                boton.grid(row=fila, column=columna, padx=2, pady=2)
                self.botones[texto] = boton
        self.reiniciar()

    def reiniciar(self):
        self.actual = "0"
        self.anterior = None
        self.operador = None
        self.empezar_nuevo = False
        self.mostrar()

    def mostrar(self):
        self.pantalla.config(text=self.actual)

    def presionar(self, tecla):
        if tecla.isdigit():
            if self.actual in ("0", "Error") or self.empezar_nuevo:
                self.actual = tecla
                self.empezar_nuevo = False
            else:
                self.actual += tecla
        elif tecla in OPERACIONES:
            self.anterior = float(self.actual)
            self.operador = tecla
            self.empezar_nuevo = True
        elif tecla == "=":
            self.calcular()
        elif tecla == "C":
            self.reiniciar()
            return
        self.mostrar()

    def calcular(self):
        if self.operador is None:
            return
        try:
            resultado = OPERACIONES[self.operador](self.anterior, float(self.actual))
        except ZeroDivisionError:
            self.actual = "Error"
        else:
            self.actual = str(int(resultado)) if resultado.is_integer() else str(resultado)
        self.operador = None
        self.empezar_nuevo = True


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Calculadora(raiz)

    def teclear(secuencia):
        for tecla in secuencia:
            app.botones[tecla].invoke()
        return app.pantalla.cget("text")

    assert app.pantalla.cget("text") == "0"
    assert set(app.botones) == set("0123456789+-*/=C")
    assert app.botones["7"].grid_info()["row"] == app.botones["9"].grid_info()["row"]

    assert teclear("12+30=") == "42"
    assert teclear("C") == "0"
    assert teclear("7*6=") == "42"
    assert teclear("C9/2=") == "4.5"
    assert teclear("C8/0=") == "Error"
    assert teclear("C") == "0"
    assert teclear("5-8=") == "-3"

    fuente = open(__file__, encoding="utf-8").read().split("# Pruebas")[0]
    assert "eval(" not in fuente, "No uses eval()"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Calculadora(raiz)
        raiz.mainloop()
