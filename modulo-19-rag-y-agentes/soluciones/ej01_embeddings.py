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
    return [t for t in re.split(r"[^\wáéíóúñü]+", texto.lower()) if t]


def calcular_idf(documentos):
    toks = [tokenizar(d) for d in documentos]
    vocab = sorted({t for d in toks for t in d})
    N = len(documentos)
    idf = np.array([math.log((1 + N) / (1 + sum(v in d for d in toks))) + 1 for v in vocab])
    return vocab, idf


def vectorizar(texto, vocab, idf):
    toks = tokenizar(texto)
    idx = {v: i for i, v in enumerate(vocab)}
    x = np.zeros(len(vocab))
    for t in toks:
        if t in idx:
            x[idx[t]] += 1 / len(toks)
    x *= idf
    n = np.linalg.norm(x)
    return x / n if n else x


def tf_idf(documentos):
    vocab, idf = calcular_idf(documentos)
    return vocab, np.array([vectorizar(d, vocab, idf) for d in documentos])


def similitud_coseno(a, b):
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    return float(a @ b / (na * nb)) if na and nb else 0.0
