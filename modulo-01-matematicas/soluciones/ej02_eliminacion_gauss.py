"""Ejercicio 02 — Resolver Ax = b con eliminación gaussiana y pivoteo parcial (sin np.linalg.solve)."""
import numpy as np


def resolver(A, b):
    """Devuelve x tal que A x = b. Lanza ValueError si A es singular."""
    A = np.array(A, float); b = np.array(b, float); n = len(b)
    for k in range(n):
        p = k + np.argmax(np.abs(A[k:, k]))
        if abs(A[p, k]) < 1e-12:
            raise ValueError("matriz singular")
        A[[k, p]] = A[[p, k]]; b[[k, p]] = b[[p, k]]
        for i in range(k + 1, n):
            f = A[i, k] / A[k, k]
            A[i, k:] -= f * A[k, k:]; b[i] -= f * b[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i + 1:] @ x[i + 1:]) / A[i, i]
    return x


def determinante(A):
    """Determinante vía eliminación (producto de pivotes con signo por intercambios)."""
    A = np.array(A, float); n = len(A); det = 1.0
    for k in range(n):
        p = k + np.argmax(np.abs(A[k:, k]))
        if abs(A[p, k]) < 1e-12:
            return 0.0
        if p != k:
            A[[k, p]] = A[[p, k]]; det = -det
        det *= A[k, k]
        for i in range(k + 1, n):
            A[i, k:] -= A[i, k] / A[k, k] * A[k, k:]
    return det
