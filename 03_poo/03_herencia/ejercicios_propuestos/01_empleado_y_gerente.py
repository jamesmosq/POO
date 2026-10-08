"""
Ejercicio propuesto 01 - Empleado y gerente
Nivel: básico

Una empresa necesita representar a sus empleados. Todos tienen nombre y
salario, pero los gerentes además dirigen un departamento.

Requisitos:
1. Crea la clase Empleado con los atributos nombre y salario.
2. Agrega a Empleado el método descripcion(), que retorne un texto como:
       "Ana gana 2500000"
3. Crea la clase Gerente, que herede de Empleado y reciba además el
   atributo departamento. Usa super().__init__() para no repetir código.
4. Sobrescribe descripcion() en Gerente para que retorne:
       "Luis gana 5000000 y dirige Ventas"
   Reutiliza el método de la clase padre con super().descripcion().

Conceptos: herencia simple, super(), sobrescritura de métodos.

Cuando termines, ejecuta el archivo. Si todo está bien verás el mensaje
"Todas las pruebas pasaron".
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ana = Empleado("Ana", 2500000)
    assert ana.nombre == "Ana"
    assert ana.salario == 2500000
    assert ana.descripcion() == "Ana gana 2500000"

    luis = Gerente("Luis", 5000000, "Ventas")
    assert luis.nombre == "Luis"
    assert luis.departamento == "Ventas"
    assert luis.descripcion() == "Luis gana 5000000 y dirige Ventas"
    assert isinstance(luis, Empleado), "Gerente debe heredar de Empleado"

    print("Todas las pruebas pasaron")
