# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-16-transformers

"""Ej 05 — Atención multi-cabeza causal en PyTorch."""
import math
import torch
from torch import nn

class AtencionMultiCabeza(nn.Module):
    """Proyección qkv conjunta, h cabezas, máscara causal, proyección de salida."""

    def __init__(self, d, h, dropout=0.0):
        raise NotImplementedError  # TODO

    def forward(self, x):
        """x (N, T, d) → (N, T, d)."""
        raise NotImplementedError  # TODO
