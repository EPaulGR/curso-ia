"""Ejercicio 3 — Partición de documentos (chunking).

- `chunks_fijos(texto, tamano, solape)`: ventanas de `tamano` palabras con `solape` palabras
  compartidas entre ventanas consecutivas (paso = tamano - solape). Cada chunk es str.
  El último chunk puede ser más corto; no generes chunks que solo repitan el solape.
- `chunks_por_parrafo(texto, max_palabras)`: agrupa párrafos (separados por línea en blanco)
  sin superar max_palabras por chunk (un párrafo más largo va solo).
"""


def chunks_fijos(texto, tamano, solape):
    p = texto.split()
    paso = tamano - solape
    out = []
    for i in range(0, len(p), paso):
        out.append(" ".join(p[i:i + tamano]))
        if i + tamano >= len(p):
            break
    return out


def chunks_por_parrafo(texto, max_palabras):
    parrafos = [x.strip() for x in texto.split("\n\n") if x.strip()]
    out, actual, n = [], [], 0
    for par in parrafos:
        w = len(par.split())
        if actual and n + w > max_palabras:
            out.append("\n\n".join(actual))
            actual, n = [], 0
        actual.append(par)
        n += w
    if actual:
        out.append("\n\n".join(actual))
    return out
