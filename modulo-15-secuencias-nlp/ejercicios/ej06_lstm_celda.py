# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-15-secuencias-nlp

"""Ej 06 — Celda LSTM en NumPy (mismo orden de compuertas que PyTorch: i, f, g, o)."""
import numpy as np

def sig(z):
    """Sigmoide."""
    raise NotImplementedError  # TODO

def lstm_paso(x, h, c, W_ih, W_hh, b_ih, b_hh):
    """W_ih (4H, d), W_hh (4H, H). Devuelve (h_nuevo, c_nuevo)."""
    raise NotImplementedError  # TODO
