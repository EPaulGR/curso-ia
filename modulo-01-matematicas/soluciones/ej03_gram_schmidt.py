"""Ejercicio 03 — Gram-Schmidt y descomposición QR."""
import numpy as np


def gram_schmidt(A):
    """Devuelve Q (columnas ortonormales) a partir de las columnas linealmente independientes de A."""
    A = np.asarray(A, float); Q = np.zeros_like(A)
    for k in range(A.shape[1]):
        u = A[:, k] - Q[:, :k] @ (Q[:, :k].T @ A[:, k])
        Q[:, k] = u / np.sqrt(u @ u)
    return Q


def qr(A):
    """Devuelve (Q, R) con A = Q R, R triangular superior."""
    Q = gram_schmidt(A)
    return Q, Q.T @ np.asarray(A, float)
