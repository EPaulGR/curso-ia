"""Ejercicio 02 — RMSNorm y SwiGLU (bloque de LLaMA y sucesores).

RMSNorm(x) = x / sqrt(mean(x^2) + eps) * g      (sin restar la media)
SwiGLU(x)  = (silu(x W1) * (x W3)) W2,  silu(z) = z * sigmoid(z)
"""
import numpy as np


def rmsnorm(x, g, eps=1e-6):
    """Normaliza por la raíz del cuadrado medio sobre el último eje."""
    x = np.asarray(x, dtype=float)
    rms = np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + eps)
    return x / rms * g


def silu(z):
    """z * sigmoid(z)."""
    return z / (1.0 + np.exp(-z))


def swiglu(x, W1, W3, W2):
    """FFN con compuerta: (silu(x W1) * (x W3)) W2."""
    return (silu(x @ W1) * (x @ W3)) @ W2
