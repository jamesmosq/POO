"""
Verifica que los ejercicios de la repo estén bien construidos.

Para cada tema revisa que:
  1. Toda solución se ejecute sin errores y pase sus pruebas.
  2. Todo ejercicio para corregir FALLE tal como se entrega al estudiante.
  3. Todo ejercicio propuesto sin resolver FALLE (sus pruebas no pasan solas).
  4. Cada ejercicio tenga su archivo de solución con el mismo nombre.

Uso (desde la raíz de la repo):
    python herramientas/verificar_ejercicios.py            # todos los temas
    python herramientas/verificar_ejercicios.py 03_poo     # solo una carpeta

Los ejercicios que requieren un servidor de base de datos o una ventana
gráfica se pueden excluir con un comentario "# verificar: omitir" en el
archivo.
"""
import os
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MENSAJE_EXITO = "Todas las pruebas pasaron"
TIEMPO_MAXIMO = 20


def ejecutar(archivo):
    entorno = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        r = subprocess.run(
            [sys.executable, archivo.name],
            cwd=archivo.parent,
            capture_output=True,
            text=True,
            encoding="utf-8",
            stdin=subprocess.DEVNULL,
            timeout=TIEMPO_MAXIMO,
            env=entorno,
        )
        return r.returncode, r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        return None, "tiempo agotado (¿hay un input() o un ciclo infinito?)"


def omitido(archivo):
    return "# verificar: omitir" in archivo.read_text(encoding="utf-8")


def ultima_linea(texto):
    lineas = [l for l in texto.strip().splitlines() if l.strip()]
    return lineas[-1][:120] if lineas else "(sin salida)"


def verificar_tema(tema):
    problemas = []
    revisados = 0
    for tipo, carpeta_sol in (("ejercicios_propuestos", "propuestos"),
                              ("ejercicios_para_corregir", "para_corregir")):
        # Solo son ejercicios los archivos numerados (01_..., 02_...); los demás
        # son módulos auxiliares que los ejercicios importan.
        for ejercicio in sorted((tema / tipo).glob("[0-9][0-9]_*.py")):
            solucion = tema / "soluciones" / carpeta_sol / ejercicio.name
            nombre = ejercicio.relative_to(RAIZ)
            if not solucion.exists():
                problemas.append(f"{nombre}: no tiene solución")
                continue
            if omitido(ejercicio):
                continue
            revisados += 1

            codigo, salida = ejecutar(solucion)
            if codigo != 0 or MENSAJE_EXITO not in salida:
                problemas.append(f"{solucion.relative_to(RAIZ)}: la solución falla -> {ultima_linea(salida)}")

            codigo, salida = ejecutar(ejercicio)
            if codigo == 0:
                problemas.append(f"{nombre}: pasa las pruebas sin que el estudiante haga nada")
    return revisados, problemas


def main():
    filtro = sys.argv[1] if len(sys.argv) > 1 else ""
    temas = sorted(
        p.parent for p in RAIZ.rglob("ejercicios_propuestos")
        if p.is_dir() and filtro in str(p.relative_to(RAIZ))
    )
    total, todos = 0, []
    for tema in temas:
        revisados, problemas = verificar_tema(tema)
        total += revisados
        estado = "OK" if not problemas else f"{len(problemas)} problema(s)"
        print(f"{str(tema.relative_to(RAIZ)):<55} {revisados:>3} ejercicios  {estado}")
        todos += problemas
    print(f"\nEjercicios revisados: {total}")
    if todos:
        print("\nProblemas encontrados:")
        for p in todos:
            print("  -", p)
        sys.exit(1)
    print("Todo correcto")


if __name__ == "__main__":
    main()
