"""
Ejercicio propuesto 04 - Argumentos variables
Nivel: intermedio

Requisitos:
1. sumar_todos(*numeros): suma todos los números que reciba, sin importar
   cuántos sean. Sin argumentos retorna 0.
       sumar_todos(1, 2, 3)  -> 6
2. promedio(*numeros): retorna el promedio. Sin argumentos retorna 0 (no
   debe dividir entre cero). Reutiliza sumar_todos.
       Pista: para pasar una tupla como argumentos sueltos usa *:
           sumar_todos(*numeros)
3. crear_perfil(nombre, **datos): retorna un diccionario con la clave
   "nombre" más todos los datos con nombre que se le pasen.
       crear_perfil("Ana", edad=20, ciudad="Cali")
           -> {"nombre": "Ana", "edad": 20, "ciudad": "Cali"}

Conceptos: *args, **kwargs, desempaquetado con * y **.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert sumar_todos() == 0
    assert sumar_todos(5) == 5
    assert sumar_todos(1, 2, 3, 4) == 10

    assert promedio() == 0
    assert promedio(2, 4, 6) == 4
    notas = (3.0, 4.0, 5.0)
    assert promedio(*notas) == 4.0

    assert crear_perfil("Ana") == {"nombre": "Ana"}
    assert crear_perfil("Ana", edad=20, ciudad="Cali") == {"nombre": "Ana", "edad": 20, "ciudad": "Cali"}

    print("Todas las pruebas pasaron")
