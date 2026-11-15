# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-17-modelos-generativos

"""Ej 06 — DDPM mínimo: red que predice el ruido sobre datos 2D, entrenamiento y muestreo."""
import torch
from torch import nn
device = 'mps' if torch.backends.mps.is_available() else 'cpu'

class Denoiser(nn.Module):
    """MLP que recibe (x_t, t/T) y predice ε."""

    def __init__(self, d=2, h=128):
        raise NotImplementedError  # TODO

    def forward(self, x, t_norm):
        """x (N,d), t_norm (N,1)."""
        raise NotImplementedError  # TODO

def entrenar_ddpm(X, T=100, pasos=2000, lr=0.002, dispositivo=device):
    """Pérdida simple: ‖ε - ε_θ(x_t, t)‖². Devuelve (modelo, betas, alpha_barras)."""
    raise NotImplementedError  # TODO

@torch.no_grad()
def muestrear(m, betas, ab, n, d=2, dispositivo=device):
    """Muestreo ancestral DDPM: x_{t-1} = (x_t - β_t/√(1-ᾱ_t)·ε_θ)/√α_t + √β_t·z."""
    raise NotImplementedError  # TODO
