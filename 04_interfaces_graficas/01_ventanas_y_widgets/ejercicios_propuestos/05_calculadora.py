"""
Ejercicio propuesto 05 - Calculadora
Nivel: avanzado

Requisitos. Crea la clase Calculadora(raiz):
1. self.pantalla: un Label que muestra el número actual (al inicio "0").
2. self.botones: un diccionario texto -> Button con las teclas
       7 8 9 /
       4 5 6 *
       1 2 3 -
       0 C = +
   ubicadas con grid() en esa disposición. Crea los botones con ciclos,
   no uno por uno.
3. presionar(tecla): la lógica de la calculadora. Cada botón la llama con
   su texto. CUIDADO con las lambdas dentro de un ciclo: usa
       command=lambda t=texto: self.presionar(t)
   para que cada botón recuerde su propio texto.
4. Comportamiento:
   - Dígitos: se agregan al número en pantalla ("0" se reemplaza).
   - Operador: guarda el número y el operador, y el siguiente dígito
     empieza un número nuevo.
   - "=": calcula y muestra el resultado. Si es entero, sin decimales
     ("12", no "12.0"). Dividir entre 0 muestra "Error".
   - "C": vuelve todo al estado inicial.
   No uses eval(): es peligroso con datos que escribe el usuario.

Conceptos: grid, crear widgets en ciclos, lambdas con valores por defecto,
estado de una aplicación.
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
