"""Ej 06 — Celda LSTM en NumPy (mismo orden de compuertas que PyTorch: i, f, g, o)."""
import numpy as np


def sig(z):
    """Sigmoide."""
    return 1 / (1 + np.exp(-z))


def lstm_paso(x, h, c, W_ih, W_hh, b_ih, b_hh):
    """W_ih (4H, d), W_hh (4H, H). Devuelve (h_nuevo, c_nuevo)."""
    z = W_ih @ x + b_ih + W_hh @ h + b_hh
    i, f, g, o = np.split(z, 4)
    c = sig(f) * c + sig(i) * np.tanh(g)
    return sig(o) * np.tanh(c), c
