# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-13-redes-neuronales

"""Ej 02 — Activaciones y sus derivadas."""
import numpy as np

def sigmoide(z):
    """σ(z) = 1 / (1 + e^{-z}), numéricamente estable."""
    raise NotImplementedError  # TODO

def d_sigmoide(z):
    """Derivada de la sigmoide."""
    raise NotImplementedError  # TODO

def relu(z):
    """max(0, z)."""
    raise NotImplementedError  # TODO

def d_relu(z):
    """1 si z > 0, si no 0."""
    raise NotImplementedError  # TODO

def softmax(z):
    """Softmax por filas, estable (resta el máximo)."""
    raise NotImplementedError  # TODO
