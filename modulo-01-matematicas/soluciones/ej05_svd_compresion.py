"""Ejercicio 05 — SVD y aproximación de rango bajo (puedes usar np.linalg.svd)."""
import numpy as np


def rango_bajo(A, k):
    """Mejor aproximación de rango k de A (Eckart-Young)."""
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    return U[:, :k] * s[:k] @ Vt[:k]


def energia_retenida(A, k):
    """Fracción de la suma de valores singulares al cuadrado retenida por los k primeros."""
    s = np.linalg.svd(A, compute_uv=False)
    return float((s[:k] ** 2).sum() / (s ** 2).sum())


def k_minimo(A, umbral=0.9):
    """Menor k que retiene al menos `umbral` de la energía."""
    s2 = np.linalg.svd(A, compute_uv=False) ** 2
    return int(np.searchsorted(np.cumsum(s2) / s2.sum(), umbral) + 1)
