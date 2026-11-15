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
        v = np.asarray(vector, float)
        self.ids.append(id_)
        self.vecs.append(v / (np.linalg.norm(v) or 1))
        self.meta.append(metadatos or {})

    def _sims(self, consulta):
        q = np.asarray(consulta, float)
        q = q / (np.linalg.norm(q) or 1)
        return np.array(self.vecs) @ q

    def buscar(self, consulta, k=3):
        s = self._sims(consulta)
        orden = np.argsort(-s)[:k]
        return [(self.ids[i], float(s[i])) for i in orden]

    def buscar_mmr(self, consulta, k=3, lambda_=0.5):
        s = self._sims(consulta)
        V = np.array(self.vecs)
        elegidos, restantes = [], list(range(len(self.ids)))
        while restantes and len(elegidos) < k:
            def puntaje(i):
                red = max((V[i] @ V[j] for j in elegidos), default=0.0)
                return lambda_ * s[i] - (1 - lambda_) * red
            mejor = max(restantes, key=puntaje)
            elegidos.append(mejor)
            restantes.remove(mejor)
        return [self.ids[i] for i in elegidos]
