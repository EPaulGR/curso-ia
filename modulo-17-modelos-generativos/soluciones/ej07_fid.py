"""Ej 07 — Distancia de Fréchet entre gaussianas (base de la métrica FID)."""
import numpy as np
from scipy import linalg


def frechet(mu1, S1, mu2, S2):
    """‖μ1-μ2‖² + Tr(S1 + S2 - 2(S1 S2)^{1/2})."""
    raiz = linalg.sqrtm(S1 @ S2)
    if np.iscomplexobj(raiz):
        raiz = raiz.real
    return float(((mu1 - mu2) ** 2).sum() + np.trace(S1 + S2 - 2 * raiz))


def fid_desde_features(A, B):
    """A, B (n, d) activaciones; ajusta gaussianas y devuelve la distancia de Fréchet."""
    return frechet(A.mean(0), np.cov(A, rowvar=False), B.mean(0), np.cov(B, rowvar=False))
