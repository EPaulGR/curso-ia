# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-15-secuencias-nlp

"""Ej 07 — Clasificador de secuencias con Embedding + LSTM en PyTorch."""
import torch
from torch import nn
device = 'mps' if torch.backends.mps.is_available() else 'cpu'

class ClasificadorLSTM(nn.Module):
    """Embedding(V, e, padding_idx=0) → LSTM(e, h, batch_first) → Linear(h, c) sobre el último estado oculto."""

    def __init__(self, V, e, h, c):
        raise NotImplementedError  # TODO

    def forward(self, x):
        """x (N, T) ids → logits (N, c)."""
        raise NotImplementedError  # TODO

def entrenar(X, y, V, c, epocas=40, lr=0.01, dispositivo=device):
    """Adam + entropía cruzada, batch completo. Devuelve (modelo, exactitud)."""
    raise NotImplementedError  # TODO
