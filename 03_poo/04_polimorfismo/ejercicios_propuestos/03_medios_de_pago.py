"""
Ejercicio propuesto 03 - Medios de pago
Nivel: intermedio

Una tienda acepta varios medios de pago. Cada uno cobra una comisión
distinta, pero la tienda los procesa todos igual.

Requisitos:
1. Clase base MedioDePago con:
   - nombre (atributo de clase, por ejemplo "Genérico").
   - comision(monto): retorna 0 (las hijas la sobrescriben).
   - cobrar(monto): retorna monto + comision(monto). NO lo sobrescriban
     las hijas: es igual para todos.
2. Hijas:
       Efectivo          nombre "Efectivo"  comisión 0
       TarjetaCredito    nombre "Tarjeta"   comisión 3 % del monto
       PSE               nombre "PSE"       comisión fija de 2500
3. Función procesar_pagos(pagos): recibe tuplas (medio, monto) y retorna
   un diccionario {nombre_del_medio: total_cobrado}, acumulando si un medio
   se repite.

Observa que cobrar() se escribe una sola vez pero da resultados distintos
según la clase: llama al comision() de cada hija.

Conceptos: polimorfismo con herencia, método plantilla, atributos de clase.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    assert Efectivo().cobrar(10000) == 10000
    assert TarjetaCredito().cobrar(10000) == 10300
    assert PSE().cobrar(10000) == 12500

    pagos = [(Efectivo(), 5000), (TarjetaCredito(), 20000), (PSE(), 1000), (Efectivo(), 3000)]
    assert procesar_pagos(pagos) == {"Efectivo": 8000, "Tarjeta": 20600, "PSE": 3500}

    for clase in (Efectivo, TarjetaCredito, PSE):
        assert "cobrar" not in clase.__dict__, f"{clase.__name__} no debe sobrescribir cobrar()"

    print("Todas las pruebas pasaron")
