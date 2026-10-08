"""
Ejercicio propuesto 04 - Plantilla de reportes
Nivel: intermedio

El patrón "método plantilla": la clase abstracta define el algoritmo
completo en un método concreto, y deja algunos pasos como abstractos para
que cada hija los complete.

Requisitos:
1. Clase abstracta Reporte(titulo):
   - generar(): método CONCRETO que retorna una lista de líneas:
         [encabezado, *cuerpo, pie]
     encabezado = "=== TITULO ===" (en mayúsculas)
     pie = f"Total de líneas: {len(cuerpo)}"
   - cuerpo(): método ABSTRACTO que retorna la lista de líneas del medio.
2. ReporteVentas(ventas): ventas es una lista de tuplas (producto, valor).
   cuerpo() -> ["Café: $12,000", "Pan: $3,000"] (formato :,.0f)
3. ReporteInventario(inventario): diccionario producto -> cantidad.
   cuerpo() -> una línea por producto, ordenadas alfabéticamente:
   "Arroz: 5 unidades". Si la cantidad es 0, "Arroz: AGOTADO".

Conceptos: método plantilla, abstracción de pasos, reutilización.
"""

# Escribe tu solución aquí



# ----------------------------------------------------------------------
# Pruebas: no modifiques el código de abajo
# ----------------------------------------------------------------------
if __name__ == "__main__":
    ventas = ReporteVentas("Ventas del día", [("Café", 12000), ("Pan", 3000)])
    assert ventas.generar() == [
        "=== VENTAS DEL DÍA ===",
        "Café: $12,000",
        "Pan: $3,000",
        "Total de líneas: 2",
    ]

    inventario = ReporteInventario("Bodega", {"Pan": 10, "Arroz": 0})
    assert inventario.generar() == [
        "=== BODEGA ===",
        "Arroz: AGOTADO",
        "Pan: 10 unidades",
        "Total de líneas: 2",
    ]

    for clase in (ReporteVentas, ReporteInventario):
        assert "generar" not in clase.__dict__, f"{clase.__name__} no debe sobrescribir generar()"

    print("Todas las pruebas pasaron")
