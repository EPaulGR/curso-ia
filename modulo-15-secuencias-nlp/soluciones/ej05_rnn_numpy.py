"""Ej 05 — Forward de una RNN de Elman en NumPy."""
import numpy as np


def rnn_forward(X, h0, Wx, Wh, b):
    """X (T, d), h0 (H,). h_t = tanh(x_t Wx + h_{t-1} Wh + b). Devuelve H_todas (T, H)."""
    h, salida = h0, []
    for x in X:
        h = np.tanh(x @ Wx + h @ Wh + b)
        salida.append(h)
    return np.stack(salida)


def norma_gradiente_bptt(Wh, T):
    """Ilustra gradiente que explota/desaparece: devuelve ‖Wh^T‖₂ (norma espectral de la potencia)."""
    return float(np.linalg.norm(np.linalg.matrix_power(Wh, T), 2))
