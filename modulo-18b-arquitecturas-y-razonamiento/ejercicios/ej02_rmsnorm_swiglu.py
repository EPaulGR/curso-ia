"""Ejercicio 02 — RMSNorm y SwiGLU (bloque de LLaMA y sucesores).

RMSNorm(x) = x / sqrt(mean(x^2) + eps) * g      (sin restar la media)
SwiGLU(x)  = (silu(x W1) * (x W3)) W2,  silu(z) = z * sigmoid(z)
"""
import numpy as np


def rmsnorm(x, g, eps=1e-6):
    """Normaliza por la raíz del cuadrado medio sobre el último eje."""
    raise NotImplementedError  # TODO


def silu(z):
    """z * sigmoid(z)."""
    raise NotImplementedError  # TODO


def swiglu(x, W1, W3, W2):
    """FFN con compuerta: (silu(x W1) * (x W3)) W2."""
    raise NotImplementedError  # TODO
