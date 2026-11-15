"""Ej 02 — Inicialización k-means++ (Arthur & Vassilvitskii, 2007)."""
import numpy as np


def kmeanspp(X, k, semilla=0):
    """Elige k centroides: el primero al azar, los siguientes con probabilidad proporcional a D(x)^2."""
    rng = np.random.default_rng(semilla)
    C = [X[rng.integers(len(X))]]
    for _ in range(1, k):
        d2 = np.min(((X[:, None] - np.array(C)[None]) ** 2).sum(-1), axis=1)
        C.append(X[rng.choice(len(X), p=d2 / d2.sum())])
    return np.array(C)
