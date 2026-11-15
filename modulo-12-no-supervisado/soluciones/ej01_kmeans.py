"""Ej 01 — K-means (algoritmo de Lloyd) desde cero con NumPy."""
import numpy as np


def asignar(X, centroides):
    """Devuelve un arreglo (n,) con el índice del centroide más cercano (distancia euclidiana) a cada punto."""
    d = ((X[:, None, :] - centroides[None, :, :]) ** 2).sum(-1)
    return d.argmin(1)


def actualizar(X, etiquetas, k):
    """Devuelve (k, d) con la media de los puntos de cada cluster."""
    return np.stack([X[etiquetas == j].mean(0) for j in range(k)])


def _lloyd(X, k, iters, rng):
    """Una corrida de Lloyd desde k puntos aleatorios de X. Devuelve (centroides, etiquetas, inercia)."""
    C = X[rng.choice(len(X), k, replace=False)]
    for _ in range(iters):
        et = asignar(X, C)
        nuevo = actualizar(X, et, k)
        if np.allclose(nuevo, C):
            break
        C = nuevo
    et = asignar(X, C)
    inercia = float(((X - C[et]) ** 2).sum())
    return C, et, inercia


def kmeans(X, k, iters=100, semilla=0, n_init=10):
    """K-means completo con varios reinicios. Devuelve (centroides, etiquetas, inercia)."""
    rng = np.random.default_rng(semilla)
    return min((_lloyd(X, k, iters, rng) for _ in range(n_init)), key=lambda r: r[2])
