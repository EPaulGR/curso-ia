# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-14-vision-cnn

"""Ej 07 — Bloque residual de ResNet (He et al., 2016)."""
import torch
from torch import nn

class BloqueResidual(nn.Module):
    """y = ReLU(BN(conv(ReLU(BN(conv(x))))) + atajo(x)); atajo = conv1x1+BN si cambia canales o stride."""

    def __init__(self, c_in, c_out, stride=1):
        raise NotImplementedError  # TODO

    def forward(self, x):
        """Aplica el bloque."""
        raise NotImplementedError  # TODO
