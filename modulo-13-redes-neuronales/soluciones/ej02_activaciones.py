"""Ej 02 — Activaciones y sus derivadas."""
import numpy as np


def sigmoide(z):
    """σ(z) = 1 / (1 + e^{-z}), numéricamente estable."""
    return np.where(z >= 0, 1 / (1 + np.exp(-np.abs(z))), np.exp(-np.abs(z)) / (1 + np.exp(-np.abs(z))))


def d_sigmoide(z):
    """Derivada de la sigmoide."""
    s = sigmoide(z)
    return s * (1 - s)


def relu(z):
    """max(0, z)."""
    return np.maximum(0, z)


def d_relu(z):
    """1 si z > 0, si no 0."""
    return (z > 0).astype(float)


def softmax(z):
    """Softmax por filas, estable (resta el máximo)."""
    e = np.exp(z - z.max(axis=-1, keepdims=True))
    return e / e.sum(axis=-1, keepdims=True)
