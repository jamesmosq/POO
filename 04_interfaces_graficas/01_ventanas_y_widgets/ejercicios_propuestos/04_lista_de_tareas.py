"""
Ejercicio propuesto 04 - Lista de tareas
Nivel: intermedio

Requisitos. Crea la clase ListaDeTareas(raiz) con:
1. self.entrada (Entry), self.boton_agregar (Button "Agregar"),
   self.lista (Listbox), self.boton_eliminar (Button "Eliminar") y
   self.contador (Label).
2. agregar(): agrega el texto del Entry al final del Listbox y limpia el
   Entry. Ignora textos vacíos o repetidos.
3. eliminar(): elimina la tarea seleccionada en el Listbox. Si no hay
   ninguna seleccionada, no hace nada.
       seleccion = self.lista.curselection()   # tupla de índices
4. self.contador muestra siempre "N tareas" (también "0 tareas" al
   inicio). Usa un método actualizar_contador() y llámalo después de
   cada cambio.
5. Agrega una Scrollbar vertical conectada al Listbox.

Conceptos: Listbox, curselection, Scrollbar, mantener la vista
actualizada.
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
    app = ListaDeTareas(raiz)
    assert app.contador.cget("text") == "0 tareas"

    for tarea in ("Estudiar", "", "Programar", "Estudiar", "Descansar"):
        app.entrada.insert(0, tarea)
        app.boton_agregar.invoke()
        assert app.entrada.get() == "", "El Entry debe quedar vacío después de agregar"
    assert app.lista.get(0, tk.END) == ("Estudiar", "Programar", "Descansar")
    assert app.contador.cget("text") == "3 tareas"

    app.boton_eliminar.invoke()
    assert app.lista.size() == 3, "Sin selección no se elimina nada"

    app.lista.selection_set(1)
    app.boton_eliminar.invoke()
    assert app.lista.get(0, tk.END) == ("Estudiar", "Descansar")
    assert app.contador.cget("text") == "2 tareas"

    assert app.lista.cget("yscrollcommand"), "Conecta una Scrollbar al Listbox"
    raiz.destroy()

    print("Todas las pruebas pasaron")

    if not os.environ.get("VERIFICAR_SIN_VENTANA"):
        raiz = tk.Tk()
        ListaDeTareas(raiz)
        raiz.mainloop()
