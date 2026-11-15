"""Ejercicio 1 — Embeddings simples y similitud.

- `tokenizar(texto)`: minúsculas, separa por cualquier carácter no alfanumérico; descarta vacíos.
- `tf_idf(documentos)`: devuelve (vocab: list ordenada, matriz np.ndarray n_docs x |vocab|)
  con tf = conteo/len(doc) e idf = log((1+N)/(1+df)) + 1. Cada fila normalizada L2.
- `vectorizar(texto, vocab, idf)`: vector TF-IDF normalizado para una consulta.
- `similitud_coseno(a, b)`.
En producción usarías un modelo de embeddings (sentence-transformers, mlx-embeddings);
la mecánica de recuperación es idéntica.
"""
import math
import re
import numpy as np


def tokenizar(texto):
    raise NotImplementedError  # TODO: implementa esta función


def calcular_idf(documentos):
    raise NotImplementedError  # TODO: implementa esta función


def vectorizar(texto, vocab, idf):
    raise NotImplementedError  # TODO: implementa esta función


def tf_idf(documentos):
    raise NotImplementedError  # TODO: implementa esta función


def similitud_coseno(a, b):
    raise NotImplementedError  # TODO: implementa esta función
