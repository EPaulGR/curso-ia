"""Ejercicio 06 — Teoría de la información (log base 2 salvo que se indique)."""
import numpy as np


def entropia(p, base=2):
    """H(p); ignora probabilidades cero."""
    p = np.asarray(p, float); p = p[p > 0]
    return float(-(p * np.log(p)).sum() / np.log(base))


def entropia_cruzada(p, q, base=2):
    """H(p, q)."""
    p = np.asarray(p, float); q = np.asarray(q, float); m = p > 0
    return float(-(p[m] * np.log(q[m])).sum() / np.log(base))


def kl(p, q, base=2):
    """D_KL(p || q)."""
    return entropia_cruzada(p, q, base) - entropia(p, base)


def informacion_mutua(conjunta, base=2):
    """I(X;Y) a partir de la matriz de probabilidad conjunta."""
    P = np.asarray(conjunta, float)
    return entropia(P.sum(1), base) + entropia(P.sum(0), base) - entropia(P.ravel(), base)


def perplejidad(probs_correctas):
    """Perplejidad = exp(-media log p) de las probabilidades asignadas a los tokens correctos."""
    return float(np.exp(-np.mean(np.log(probs_correctas))))
