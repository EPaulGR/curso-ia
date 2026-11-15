"""Ej 06 — Clustering jerárquico aglomerativo (enlace simple)."""
import numpy as np


def aglomerativo_simple(X, k):
    """Une clusters por distancia mínima hasta quedar k. Devuelve etiquetas 0..k-1."""
    clusters = [[i] for i in range(len(X))]
    D = np.sqrt(((X[:, None] - X[None]) ** 2).sum(-1))
    while len(clusters) > k:
        mejor = (np.inf, 0, 1)
        for a in range(len(clusters)):
            for b in range(a + 1, len(clusters)):
                d = D[np.ix_(clusters[a], clusters[b])].min()
                if d < mejor[0]:
                    mejor = (d, a, b)
        _, a, b = mejor
        clusters[a] += clusters.pop(b)
    et = np.empty(len(X), int)
    for j, c in enumerate(clusters):
        et[c] = j
    return et
