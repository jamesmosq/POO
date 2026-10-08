"""
Solución - Ejercicio propuesto 03 - Acceso a un evento
"""

edad = 20
tiene_boleta = True
es_vip = False
en_lista_negra = False

# >>> tu código empieza aquí
# Primero se arma la condición normal (edad y boleta), luego se agrega el VIP
# con or, y al final se excluye la lista negra con and not.
puede_entrar = ((edad >= 18 and tiene_boleta) or es_vip) and not en_lista_negra
# <<< tu código termina aquí


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
def probar(**datos):
    """Ejecuta tu código con otros datos y retorna las variables que creó."""
    fuente = open(__file__, encoding="utf-8").read()
    codigo = fuente.split("# >>> tu código empieza aquí")[1].split("# <<< tu código termina aquí")[0]
    variables = dict(datos)
    exec(codigo, variables)
    return variables


if __name__ == "__main__":
    casos = [
        # edad, boleta, vip, lista_negra -> resultado esperado
        ((20, True, False, False), True),
        ((16, True, False, False), False),
        ((20, False, False, False), False),
        ((15, False, True, False), True),
        ((30, True, False, True), False),
        ((30, True, True, True), False),
        ((18, True, False, False), True),
    ]
    for (e, boleta, vip, negra), esperado in casos:
        r = probar(edad=e, tiene_boleta=boleta, es_vip=vip, en_lista_negra=negra)
        assert r["puede_entrar"] is esperado, (
            f"edad={e}, boleta={boleta}, vip={vip}, lista_negra={negra}: "
            f"se esperaba {esperado}"
        )

    print("Todas las pruebas pasaron")
