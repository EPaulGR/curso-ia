"""Ej 04 — LayerNorm y RMSNorm."""
import numpy as np


def layer_norm(x, gamma, beta, eps=1e-5):
    """Normaliza sobre la última dimensión: γ·(x-μ)/√(σ²+ε) + β."""
    mu = x.mean(-1, keepdims=True)
    var = x.var(-1, keepdims=True)
    return gamma * (x - mu) / np.sqrt(var + eps) + beta


def rms_norm(x, gamma, eps=1e-6):
    """RMSNorm (usada en Llama): γ·x / √(mean(x²)+ε)."""
    return gamma * x / np.sqrt((x ** 2).mean(-1, keepdims=True) + eps)
