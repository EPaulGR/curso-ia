# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-14-vision-cnn

"""Ej 05 — CNN pequeña en PyTorch (estilo LeNet) entrenada en MPS."""
import torch
from torch import nn
device = 'mps' if torch.backends.mps.is_available() else 'cpu'

class CNN(nn.Module):
    """conv(1→8,3,p1)→ReLU→MaxPool2 → conv(8→16,3,p1)→ReLU→MaxPool2 → Flatten → Linear(16·(s/4)²→n_clases)."""

    def __init__(self, n_clases, tam=16):
        raise NotImplementedError  # TODO

    def forward(self, x):
        """x (N,1,tam,tam) → logits (N, n_clases)."""
        raise NotImplementedError  # TODO

def entrenar(X, y, n_clases, epocas=30, lr=0.003, dispositivo=device):
    """Entrena con Adam en mini-batches de 32. Devuelve (modelo, exactitud)."""
    raise NotImplementedError  # TODO
