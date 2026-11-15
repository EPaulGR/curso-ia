"""Ejercicio 3 — Partición de documentos (chunking).

- `chunks_fijos(texto, tamano, solape)`: ventanas de `tamano` palabras con `solape` palabras
  compartidas entre ventanas consecutivas (paso = tamano - solape). Cada chunk es str.
  El último chunk puede ser más corto; no generes chunks que solo repitan el solape.
- `chunks_por_parrafo(texto, max_palabras)`: agrupa párrafos (separados por línea en blanco)
  sin superar max_palabras por chunk (un párrafo más largo va solo).
"""


def chunks_fijos(texto, tamano, solape):
    raise NotImplementedError  # TODO: implementa esta función


def chunks_por_parrafo(texto, max_palabras):
    raise NotImplementedError  # TODO: implementa esta función
