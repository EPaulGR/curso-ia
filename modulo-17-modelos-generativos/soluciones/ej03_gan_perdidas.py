"""Ej 03 — Pérdidas de una GAN (Goodfellow et al., 2014)."""
import numpy as np


def bce(p, y):
    """Entropía cruzada binaria media."""
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return float(-(y * np.log(p) + (1 - y) * np.log(1 - p)).mean())


def perdida_discriminador(d_real, d_falso):
    """BCE(D(x), 1) + BCE(D(G(z)), 0)."""
    return bce(d_real, np.ones_like(d_real)) + bce(d_falso, np.zeros_like(d_falso))


def perdida_generador_nosaturante(d_falso):
    """Versión no saturante: -E[log D(G(z))]."""
    return bce(d_falso, np.ones_like(d_falso))


def d_optimo(p_datos, p_gen):
    """Discriminador óptimo D*(x) = p_datos / (p_datos + p_gen)."""
    return p_datos / (p_datos + p_gen)
