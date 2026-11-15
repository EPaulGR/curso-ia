"""Ejercicio 2 — Índice vectorial.

Clase `IndiceVectorial`:
- `agregar(id_, vector, metadatos=None)`.
- `buscar(consulta, k)`: lista de (id, similitud coseno) ordenada desc. (búsqueda exacta).
- `buscar_mmr(consulta, k, lambda_=0.5)`: Maximal Marginal Relevance; en cada paso elige el
  candidato que maximiza lambda*sim(q, d) - (1-lambda)*max sim(d, seleccionados).
Bases reales: FAISS, hnswlib, sqlite-vec, Chroma, pgvector (usan ANN como HNSW).
"""
import numpy as np


class IndiceVectorial:

    def __init__(self):
        self.ids, self.vecs, self.meta = [], [], []

    def agregar(self, id_, vector, metadatos=None):
        raise NotImplementedError  # TODO: implementa esta función

    def _sims(self, consulta):
        q = np.asarray(consulta, float)
        q = q / (np.linalg.norm(q) or 1)
        return np.array(self.vecs) @ q

    def buscar(self, consulta, k=3):
        raise NotImplementedError  # TODO: implementa esta función

    def buscar_mmr(self, consulta, k=3, lambda_=0.5):
        raise NotImplementedError  # TODO: implementa esta función
