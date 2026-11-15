# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-16-transformers

"""Ej 04 — LayerNorm y RMSNorm."""
import numpy as np

def layer_norm(x, gamma, beta, eps=1e-05):
    """Normaliza sobre la última dimensión: γ·(x-μ)/√(σ²+ε) + β."""
    raise NotImplementedError  # TODO

def rms_norm(x, gamma, eps=1e-06):
    """RMSNorm (usada en Llama): γ·x / √(mean(x²)+ε)."""
    raise NotImplementedError  # TODO
