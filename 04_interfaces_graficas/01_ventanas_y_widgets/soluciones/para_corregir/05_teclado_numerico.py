"""
Solución - Ejercicio para corregir 05 - Teclado numérico

CORRECCIÓN 1 (todos los botones escribían 9): una lambda no guarda el
VALOR de numero cuando se crea; guarda la variable y la lee cuando se
ejecuta. Al hacer clic, el ciclo ya terminó y numero vale 9. Con un
parámetro por defecto (n=numero) el valor se fija en cada vuelta.

CORRECCIÓN 2 (botones encimados): la columna se calculaba igual que la
fila, con //. La columna es el residuo: (numero - 1) % 3.

CORRECCIÓN 3 (TypeError: unsupported operand type(s) for +: 'int' and
'str'): sum() no puede sumar los caracteres de un texto. Hay que convertir
cada dígito a int.
"""

import tkinter as tk


class Teclado:
    def __init__(self, raiz):
        self.pantalla = tk.Label(raiz, text="")
        self.pantalla.grid(row=4, column=0, columnspan=3)
        self.botones = {}
        for numero in range(10):
            boton = tk.Button(raiz, text=str(numero), command=lambda n=numero: self.presionar(n))  # CORRECCIÓN 1
            if numero == 0:
                boton.grid(row=3, column=1)
            else:
                boton.grid(row=(numero - 1) // 3, column=(numero - 1) % 3)  # CORRECCIÓN 2
            self.botones[numero] = boton
        self.boton_sumar = tk.Button(raiz, text="Sumar", command=self.sumar)
        self.boton_sumar.grid(row=5, column=0, columnspan=3)

    def presionar(self, numero):
        self.pantalla.config(text=self.pantalla.cget("text") + str(numero))

    def sumar(self):
        digitos = self.pantalla.cget("text")
        total = sum(int(d) for d in digitos)  # CORRECCIÓN 3
        self.pantalla.config(text=str(total))


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    raiz = tk.Tk()
    raiz.withdraw()
    app = Teclado(raiz)

    for n in (1, 2, 3):
        app.botones[n].invoke()
    assert app.pantalla.cget("text") == "123", f"La pantalla muestra {app.pantalla.cget('text')!r}"

    posiciones = {n: (app.botones[n].grid_info()["row"], app.botones[n].grid_info()["column"]) for n in range(1, 10)}
    assert len(set(posiciones.values())) == 9, f"Hay botones encimados: {posiciones}"

    app.boton_sumar.invoke()
    assert app.pantalla.cget("text") == "6"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Teclado(raiz)
        raiz.mainloop()
