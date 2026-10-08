"""Funciones auxiliares del paquete banco."""


def formatear_moneda(valor):
    """Retorna el valor con signo $, separador de miles y dos decimales."""
    return f"${valor:,.2f}"  # CORRECCIÓN 3
