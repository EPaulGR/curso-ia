"""Ej 03 — Codificación posicional sinusoidal (Vaswani et al., 2017)."""
import numpy as np


def codificacion_posicional(T, d):
    """PE[pos, 2i] = sin(pos / 10000^{2i/d}), PE[pos, 2i+1] = cos(...). Devuelve (T, d)."""
    pos = np.arange(T)[:, None]
    i = np.arange(0, d, 2)[None, :]
    ang = pos / 10000 ** (i / d)
    pe = np.zeros((T, d))
    pe[:, 0::2] = np.sin(ang)
    pe[:, 1::2] = np.cos(ang)
    return pe
