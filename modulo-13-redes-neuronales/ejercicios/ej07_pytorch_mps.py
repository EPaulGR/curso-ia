# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-13-redes-neuronales

"""Ej 07 — El mismo MLP en PyTorch usando la GPU de Apple (MPS)."""
import torch
from torch import nn
device = 'mps' if torch.backends.mps.is_available() else 'cpu'

def crear_modelo(d, h, c):
    """nn.Sequential: Linear(d,h) → ReLU → Linear(h,c)."""
    raise NotImplementedError  # TODO

def entrenar_torch(X, y, h=32, epocas=200, lr=0.01, dispositivo=device):
    """Entrena con Adam y CrossEntropyLoss. X, y: tensores CPU. Devuelve (modelo, exactitud_entrenamiento)."""
    raise NotImplementedError  # TODO
