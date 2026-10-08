"""
Ejercicio propuesto 05 - Peajes
Nivel: avanzado

Un peaje cobra distinto según el tipo de vehículo. Vas a construir una
jerarquía de varios niveles donde cada clase reutiliza el cálculo de su
padre en lugar de repetirlo.

    Vehiculo
    ├── Carro
    └── Camion
        └── CamionRefrigerado

Requisitos:
1. Vehiculo(placa):
   - Valida la placa: 3 letras seguidas de 3 dígitos ("ABC123"). Se guarda
     en mayúscula. Si no cumple, ValueError.
   - Atributo de clase TARIFA_BASE = 10000.
   - peaje(): retorna TARIFA_BASE. Usa self.TARIFA_BASE, para que una hija
     pueda cambiar la tarifa sin reescribir el método.
   - __str__(): "ABC123 - Vehiculo - $10,000" (con el nombre de la clase
     real del objeto: type(self).__name__).
2. Carro(placa): TARIFA_BASE = 12000. No redefine peaje() ni __str__().
3. Camion(placa, ejes): ejes debe ser 2 o más (si no, ValueError).
   peaje() = peaje del padre + 8000 por cada eje adicional después del 2.
4. CamionRefrigerado(placa, ejes): peaje() = peaje del padre (Camion) con
   un recargo del 20 %.
5. Función recaudo_total(vehiculos): suma los peajes de una lista.

Conceptos: herencia multinivel, super() encadenado, atributos de clase
sobrescritos, validación en la clase base.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    v = Vehiculo("abc123")
    assert v.placa == "ABC123"
    assert v.peaje() == 10000
    assert str(v) == "ABC123 - Vehiculo - $10,000"

    c = Carro("XYZ789")
    assert c.peaje() == 12000 and str(c) == "XYZ789 - Carro - $12,000"
    assert "peaje" not in Carro.__dict__, "Carro solo cambia TARIFA_BASE"

    assert Camion("TRK001", 2).peaje() == 10000
    assert Camion("TRK002", 4).peaje() == 26000
    frio = CamionRefrigerado("FRI001", 3)
    assert frio.peaje() == 21600, frio.peaje()
    assert str(frio) == "FRI001 - CamionRefrigerado - $21,600"
    assert isinstance(frio, Camion) and isinstance(frio, Vehiculo)

    for placa, args in (("AB123", ()), ("ABCD12", ()), ("123ABC", ())):
        try:
            Vehiculo(placa, *args)
            raise AssertionError(f"La placa {placa} debe lanzar ValueError")
        except ValueError:
            pass
    try:
        Camion("TRK003", 1)
        raise AssertionError("Un camión con 1 eje debe lanzar ValueError")
    except ValueError:
        pass

    assert recaudo_total([v, c, frio]) == 10000 + 12000 + 21600

    print("Todas las pruebas pasaron")
