# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-17-modelos-generativos

"""Ej 02 — Autoencoder variacional en PyTorch."""
import torch
from torch import nn
device = 'mps' if torch.backends.mps.is_available() else 'cpu'

class VAE(nn.Module):
    """Encoder MLP → (μ, logvar) de dim z; decoder MLP → reconstrucción."""

    def __init__(self, d, z=2, h=64):
        raise NotImplementedError  # TODO

    def forward(self, x):
        """Devuelve (x_rec, mu, logvar)."""
        raise NotImplementedError  # TODO

def perdida_vae(x, x_rec, mu, logvar, beta=1.0):
    """MSE sumada por muestra + β·KL, promediada en el batch."""
    raise NotImplementedError  # TODO

def entrenar(X, pasos=500, lr=0.003, beta=0.05, dispositivo=device):
    """Entrena con Adam usando perdida_vae con el β dado; devuelve (modelo, historial)."""
    raise NotImplementedError  # TODO
