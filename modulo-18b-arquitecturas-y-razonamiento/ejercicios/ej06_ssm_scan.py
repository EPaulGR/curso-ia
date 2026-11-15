"""Ejercicio 06 — Modelos de espacio de estados (S4/Mamba) simplificados.

SSM discreto diagonal:  h_t = a ⊙ h_{t-1} + b x_t ;  y_t = c · h_t
Si (a, b, c) son fijos (LTI) equivale a una convolución con kernel
K_j = c · (a^j ⊙ b). Mamba hace a, b dependientes de la entrada ("selectivo")
vía un paso delta_t: a_t = exp(delta_t * A), b_t = delta_t * B, y ya no es convolución,
pero sigue siendo lineal en tiempo O(T) (scan).
"""
import numpy as np


def scan_lti(x, a, b, c):
    """x: (T,), a,b,c: (N,). Recurrencia; devuelve y (T,)."""
    raise NotImplementedError  # TODO


def kernel_conv(a, b, c, T):
    """Kernel K_j = c · (a^j ⊙ b), j = 0..T-1."""
    raise NotImplementedError  # TODO


def conv_causal(x, K):
    """y_t = sum_{j<=t} K_j x_{t-j}."""
    raise NotImplementedError  # TODO


def scan_selectivo(x, A, B, c, delta):
    """Mamba simplificado: delta (T,) > 0, A (N,) negativa. a_t = exp(delta_t A), b_t = delta_t B."""
    raise NotImplementedError  # TODO
