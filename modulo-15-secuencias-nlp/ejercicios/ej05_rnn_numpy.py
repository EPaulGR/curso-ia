# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-15-secuencias-nlp

"""Ej 05 — Forward de una RNN de Elman en NumPy."""
import numpy as np

def rnn_forward(X, h0, Wx, Wh, b):
    """X (T, d), h0 (H,). h_t = tanh(x_t Wx + h_{t-1} Wh + b). Devuelve H_todas (T, H)."""
    raise NotImplementedError  # TODO

def norma_gradiente_bptt(Wh, T):
    """Ilustra gradiente que explota/desaparece: devuelve ‖Wh^T‖₂ (norma espectral de la potencia)."""
    raise NotImplementedError  # TODO
