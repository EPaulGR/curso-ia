"""Ej 08 — Estrategias de decodificación: temperatura, top-k y top-p (nucleus)."""
import numpy as np


def con_temperatura(logits, t):
    """Probabilidades softmax(logits / t)."""
    z = logits / t
    e = np.exp(z - z.max())
    return e / e.sum()


def top_k(p, k):
    """Conserva las k probabilidades mayores y renormaliza."""
    q = np.zeros_like(p)
    idx = np.argsort(p)[-k:]
    q[idx] = p[idx]
    return q / q.sum()


def top_p(p, umbral):
    """Conserva el menor conjunto de tokens cuya masa acumulada ≥ umbral; renormaliza."""
    orden = np.argsort(p)[::-1]
    acum = np.cumsum(p[orden])
    n = int(np.searchsorted(acum, umbral) + 1)
    q = np.zeros_like(p)
    q[orden[:n]] = p[orden[:n]]
    return q / q.sum()
