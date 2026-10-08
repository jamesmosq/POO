"""
Ejercicio para corregir 05 - Teclado numérico
Nivel: avanzado
Errores a encontrar: 3

Qué debería hacer el programa:
    Un teclado con botones del 0 al 9 creados en un ciclo, más un botón
    "Sumar". La pantalla acumula los dígitos que se presionan; "Sumar"
    suma los dígitos del número en pantalla y muestra el resultado.

        presionar 1, 2, 3   -> pantalla "123"
        Sumar               -> pantalla "6"

    Los botones del 1 al 9 van en una cuadrícula de 3 x 3 (filas 0, 1 y 2)
    y el 0 en la fila 3.

Pista: si todos los botones escriben el mismo número, investiga cómo
"recuerda" una lambda las variables de un ciclo.

Cómo trabajar:
    1. Ejecuta el archivo y lee el mensaje de error completo.
    2. Corrige un error a la vez y vuelve a ejecutar.
    3. Termina cuando veas "Todas las pruebas pasaron".
    No modifiques las pruebas.
"""
import tkinter as tk


class Teclado:
    def __init__(self, raiz):
        self.pantalla = tk.Label(raiz, text="")
        self.pantalla.grid(row=4, column=0, columnspan=3)
        self.botones = {}
        for numero in range(10):
            boton = tk.Button(raiz, text=str(numero), command=lambda: self.presionar(numero))
            if numero == 0:
                boton.grid(row=3, column=1)
            else:
                boton.grid(row=(numero - 1) // 3, column=(numero - 1) // 3)
            self.botones[numero] = boton
        self.boton_sumar = tk.Button(raiz, text="Sumar", command=self.sumar)
        self.boton_sumar.grid(row=5, column=0, columnspan=3)

    def presionar(self, numero):
        self.pantalla.config(text=self.pantalla.cget("text") + str(numero))

    def sumar(self):
        digitos = self.pantalla.cget("text")
        total = sum(digitos)
        self.pantalla.config(text=str(total))


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
