def filtrar_por_condicion(lista, condicion):
    """Filtra los elementos de una lista que cumplen con una condición.

    Args:
        lista: Una lista de cualquier tipo de elemento.
        condicion: Una función que recibe un elemento de la lista y retorna True si cumple la condición.

    Returns:
        Una nueva lista con los elementos filtrados.
    """

    lista_filtrada = [elemento for elemento in lista if condicion(elemento)]
    return lista_filtrada

# Ejemplo de uso
lista_numeros = [1, 4, 7, 2, 9, 5]

# Filtrar números pares
def es_par(numero):
    return numero % 2 == 0

numeros_pares = filtrar_por_condicion(lista_numeros, es_par)

# Filtrar números mayores a 5
def mayor_a_5(numero):
    return numero > 5

numeros_mayores_a_5 = filtrar_por_condicion(lista_numeros, mayor_a_5)

print("Lista original:", lista_numeros)
print("Números pares:", numeros_pares)
print("Números mayores a 5:", numeros_mayores_a_5)