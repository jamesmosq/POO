"""
Ejercicio propuesto 03 - Acceso a un evento
Nivel: intermedio

Las reglas de entrada a un concierto son:
    - Puede entrar quien sea mayor de edad (18 o más) Y tenga boleta.
    - Los invitados VIP entran siempre, aunque no tengan boleta ni edad.
    - Nadie que esté en la lista negra puede entrar, ni siquiera un VIP.

Requisitos:
1. Crea la variable puede_entrar (bool) con UNA sola expresión que use
   and, or y not.
2. Usa paréntesis para dejar claro el orden. Recuerda: not se evalúa
   primero, luego and y por último or.

Conceptos: operadores lógicos, precedencia, paréntesis.
"""

edad = 20
tiene_boleta = True
es_vip = False
en_lista_negra = False

# >>> tu código empieza aquí

# <<< tu código termina aquí


# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
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
