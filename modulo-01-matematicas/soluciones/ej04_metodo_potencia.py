"""Ejercicio 04 — Método de la potencia."""
import numpy as np


def metodo_potencia(A, iters=1000, tol=1e-10, semilla=0):
    """Devuelve (lambda, v): eigenvalor dominante y su eigenvector unitario."""
    A = np.asarray(A, float)
    v = np.random.default_rng(semilla).normal(size=A.shape[0]); v /= np.sqrt(v @ v)
    lam = 0.0
    for _ in range(iters):
        w = A @ v; w /= np.sqrt(w @ w)
        nuevo = w @ A @ w
        if abs(nuevo - lam) < tol:
            return nuevo, w
        v, lam = w, nuevo
    return lam, v


def pagerank(M, d=0.85, iters=100):
    """PageRank. M[i,j]=1 si la página j enlaza a i. Devuelve vector de probabilidades que suma 1."""
    M = np.asarray(M, float); n = len(M)
    salida = M.sum(0); salida[salida == 0] = 1
    P = M / salida
    r = np.ones(n) / n
    for _ in range(iters):
        r = (1 - d) / n + d * P @ r
    return r / r.sum()
