"""Ej 05 — DBSCAN desde cero."""
import numpy as np


def dbscan(X, eps, min_pts):
    """Devuelve etiquetas (n,): 0..c-1 para clusters y -1 para ruido."""
    n = len(X)
    D = np.sqrt(((X[:, None] - X[None]) ** 2).sum(-1))
    vecinos = [np.where(D[i] <= eps)[0] for i in range(n)]
    et = np.full(n, -1)
    visit = np.zeros(n, bool)
    c = 0
    for i in range(n):
        if visit[i] or len(vecinos[i]) < min_pts:
            continue
        cola = [i]
        while cola:
            j = cola.pop()
            if et[j] == -1:
                et[j] = c
            if visit[j]:
                continue
            visit[j] = True
            if len(vecinos[j]) >= min_pts:
                cola.extend(vecinos[j])
        c += 1
    return et
