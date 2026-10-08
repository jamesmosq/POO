"""
Ejercicio propuesto 05 - Pestañas con modelo compartido
Nivel: avanzado

Cuando dos partes de la interfaz muestran los mismos datos, no deben
llamarse directamente entre ellas. Ambas usan un MODELO común, y el modelo
avisa a quien esté interesado cuando algo cambia (patrón observador).

Requisitos:
1. Clase ModeloTareas (sin Tkinter):
   - tareas: lista de textos.
   - suscribir(funcion): guarda una función que se llamará en cada cambio.
   - agregar(tarea): agrega la tarea y llama a todas las funciones
     suscritas.
2. PestanaAgregar(tk.Frame) que recibe (master, modelo): Entry
   self.entrada y Button self.boton que agrega al modelo y limpia el Entry.
   No sabe nada de la otra pestaña.
3. PestanaResumen(tk.Frame) que recibe (master, modelo): Label
   self.contador ("N tareas") y Listbox self.lista. En __init__ se suscribe
   al modelo con su método refrescar(), que vuelve a dibujar la lista
   completa (borrando lo anterior) y el contador.
4. Aplicacion(ttk.Notebook) que recibe (master, modelo) y agrega las dos
   pestañas con los títulos "Agregar" y "Resumen". Guárdalas en
   self.pestana_agregar y self.pestana_resumen.

Conceptos: patrón observador, ttk.Notebook, componentes desacoplados.
"""
import tkinter as tk
from tkinter import ttk

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os

    avisos = []
    m = ModeloTareas()
    m.suscribir(lambda: avisos.append(len(m.tareas)))
    m.agregar("a")
    m.agregar("b")
    assert avisos == [1, 2], "El modelo debe avisar a los suscritos en cada cambio"

    raiz = tk.Tk()
    raiz.withdraw()
    modelo = ModeloTareas()
    app = Aplicacion(raiz, modelo)
    assert [app.tab(t, "text") for t in app.tabs()] == ["Agregar", "Resumen"]
    assert app.pestana_resumen.contador.cget("text") == "0 tareas"

    for tarea in ("Leer", "Programar"):
        app.pestana_agregar.entrada.insert(0, tarea)
        app.pestana_agregar.boton.invoke()

    resumen = app.pestana_resumen
    assert resumen.contador.cget("text") == "2 tareas"
    assert resumen.lista.get(0, tk.END) == ("Leer", "Programar"), "La lista no debe repetir tareas"
    assert app.pestana_agregar.entrada.get() == ""
    assert modelo.tareas == ["Leer", "Programar"]
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        Aplicacion(raiz, ModeloTareas()).pack(fill="both", expand=True)
        raiz.mainloop()
