"""Ej 02 — Máscaras causal y de padding."""
import numpy as np


def mascara_causal(T):
    """(T,T) booleana: la posición i puede ver j ≤ i."""
    return np.tril(np.ones((T, T), bool))


def mascara_padding(longitudes, T):
    """(N, T) booleana: True en posiciones reales, False en relleno."""
    return np.arange(T)[None, :] < np.asarray(longitudes)[:, None]
